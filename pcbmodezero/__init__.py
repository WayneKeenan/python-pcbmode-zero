from pprint import pformat
from os import chdir, makedirs
from os.path import join, exists
import sys
import io

import jsontree

from svgpathtools import Path, Line, QuadraticBezier, CubicBezier, Arc, svg2paths

from pcbmode import pcbmode
from pcbmode.utils import utils
from pcbmode.utils.svg import absolute_to_relative_path

class PCB:

    def __init__(self, board_name, boards_dir="boards", rev="first", width=None, height=None):
        self.boards_root_dir = join(boards_dir, '..')
        self.board_name = board_name
        self.board_root_filepath = "{}/boards/{}".format(self.boards_root_dir, self.board_name)
        self.board_json_filepath = "{}/boards/{}/{}.json".format(self.boards_root_dir, self.board_name, self.board_name)
        self.board_shape_dirpath = "{}/boards/{}/shapes".format(self.boards_root_dir, self.board_name)
        self.board_components_dirpath = "{}/boards/{}/components".format(self.boards_root_dir, self.board_name)
        self.component_library = {}

        self.components= self.create_config_item()
        self.config = self.create_config_item()
        self.distances = self.create_config_item()
        self.documentation = self.create_config_item()
        self.layer_control = self.create_config_item()
        self.gerber = self.create_config_item()
        self.files = self.create_config_item()
        self.drills = self.create_config_item()
        self.drill_index = self.create_config_item()
        self.outline = self.create_config_item()
        self.shapes = self.create_config_item()
        self.soldermask = self.create_config_item()
        self.solderpaste = self.create_config_item()
        self.stackup = self.create_config_item()
        self.vias = self.create_config_item()

        self.routing = self.create_config_item()
        self.routing.routes.bottom = {}
        self.routing.routes.top = {}
        self.routing.vias = {}

        self.config.name = self.board_name
        self.config.no_docs = False
        self.config.no_drill_index = False
        self.config.no_flashes = False
        self.config.no_layer_index = False
        self.config.rev = rev
        self.config.style_layout = "default"
        self.config.units = "mm"

        # Board config baseline defaults (TODO: read from PCBmodE config?)

        self.layer_control.assembly = dict(hide=False, lock=False, place=True)
        self.layer_control.conductor.hide = False
        self.layer_control.conductor.lock = False
        self.layer_control.conductor.place = True
        self.layer_control.conductor.pads = dict(hide=False, lock=False, place=True)
        self.layer_control.conductor.pours = dict(hide=False, lock=True, place=True)
        self.layer_control.conductor.routing = dict(hide=False, lock=False, place=True)
        self.layer_control.dimensions = dict(hide=False, lock=True, place=True)
        self.layer_control.documentation = dict(hide=False, lock=False, place=True)
        self.layer_control.drills = dict(hide=False, lock=False, place=True)
        self.layer_control.origin = dict(hide=False, lock=True, place=False)
        self.layer_control.outline = dict(hide=False, lock=True, place=True)
        self.layer_control.placement = dict(hide=False, lock=False, place=True)
        self.layer_control.silkscreen = dict(hide=False, lock=False, place=True)
        self.layer_control.soldermask = dict(hide=False, lock=False, place=True)
        self.layer_control.solderpaste = dict(hide=True, lock=True, place=False)

        self.gerber.decimals = 6
        self.gerber.digits = 6
        self.gerber.min_segment_length = 0.05
        self.gerber.steps_per_segment = 100

        self.distances.from_pour_to.drill = 0.25
        self.distances.from_pour_to.outline = 0.4
        self.distances.from_pour_to.pad = 0.25
        self.distances.from_pour_to.route = 0.25

        self.distances.soldermask.circle_buffer = 0.05
        self.distances.soldermask.path_scale = 1.05
        self.distances.soldermask.rect_buffer = 0.05

        self.distances.solderpaste.circle_buffer = -0.1
        self.distances.solderpaste.path_scale = 0.9
        self.distances.solderpaste.rect_buffer = -0.1

        self.files.routing_data = self.board_name + "_routing.json"
        self.files.routing_svg = self.board_name + ".svg"

        self.soldermask.circle_buffer = 0.05
        self.soldermask.path_scale = 1.05
        self.soldermask.rect_buffer = 0.05
        self.solderpaste.circle_buffer = -0.1
        self.solderpaste.path_scale = 0.9
        self.solderpaste.rect_buffer = -0.1
        self.stackup.name = "two-layer"
        self.vias.default_via = "VIA"

        # Defaults users can clone into their config
        self.defaults = self.create_config_item()
        self.defaults.documentaion = self.create_config_item()
        self.defaults.documentation.font_family = "Overlock-Regular-OTF-webfont"
        self.defaults.documentation.font_size = "1.5mm"
        self.defaults.documentation.letter_spacing = "0mm"
        self.defaults.documentation.line_height = "1.5mm"
        self.defaults.documentation.location = [0, 0]
        self.defaults.documentation.rotate = 0
        self.defaults.documentation.style = "fill"
        self.defaults.documentation.type = "text"
        self.defaults.documentation.value = "Warning: No Text Set"


        # Default based on PCB constructor parameters

        if width and height:
            self.board_width = width
            self.board_height = width

            outline = PCB.create_square_shape(width, height)

            self.add_documentation('manufacturing', [0, -height / 2], "Manufacturing:...")
            self.add_documentation('board_details', [0, -height], "Board details: ...")
            self.add_documentation('pcbmode', [0, -width], "Designed with PCBmodE:...")
            self.drill_index.location = [0, -height]
            self.add_outline_path(outline, width=width + 10, height=height + 10)


        self.preinit_pcbmode()

    @classmethod
    def create_config_item(cls):
        return jsontree.mapped_jsontree_class(cls.underscore2minus)()


    def preinit_pcbmode(self):
        pcbmode.config.cfg['digest-digits'] = 10

    # def preinit_pcbmode(self):
    #     # ABORTIVE: Hacks to avoid modifying the internal PCBmodE source, for now.
    #
    #     # Get PCBmodE to initialise it's config
    #     # so we can re-use some of the internal helpers (e.g. 'digest' digits)
    #
    #     try:
    #         oldargv = sys.argv
    #         oldexit = sys.exit
    #         oldstdout = sys.stdout
    #         oldstderr = sys.stderr
    #         sys.stdout = io.BytesIO()
    #         sys.stderr = io.BytesIO()
    #         sys.argv = sys.argv[0::]
    #         sys.exit = lambda x: x
    #         sys.argv.extend(['-h'])
    #         pcbmode.main()
    #     except Exception:
    #         pass
    #     finally:
    #         sys.argv = oldargv
    #         sys.exit = oldexit
    #         sys.stdout = oldstdout
    #         sys.stderr = oldstderr

    # JSON Tree functions

    @classmethod
    def underscore2minus(cls, name):
        if name == '__class__':
            raise ValueError
        return name.replace('_', '-')

    @classmethod
    def clone(cls, src):
        return jsontree.clone(src)

    @classmethod
    def json2py(cls, filepath):
        with open(filepath, 'r') as file:
            txt = file.read()
            decoder = jsontree.JSONTreeDecoder()
            decoded = decoder.decode(txt)
            #print(pformat(decoded))
            #print(jsontree.dumps(decoded, indent=4))
            return decoded


    @classmethod
    def write_json(cls, json_obj, filepath):
        json_txt = jsontree.dumps(json_obj, indent=4)
        #print (all_json)

        with open(filepath, 'w') as file:
            file.write(json_txt)

    @classmethod
    def dumpJSON(cls, json_obj):
        print(jsontree.dumps(json_obj, indent=4))

    # Library Component Functions

    def add_library_component(self, component, component_name):
        if component_name in self.component_library:
            raise ValueError("%s already exists.".format(component_name))
        self.component_library[component_name] = component

    def use_library_component(self, component_name):
        self.add_library_component(find_library_component(component_name), component_name)


    def save_routing(self):
        return self.write_json(self.routing, join(self.board_root_filepath, self.board_name + '_routing.json'))

    # Board Component Functions

    @classmethod
    def create_component(cls, footprint, location, layer="bottom", rotate=0, show=True, silkscreen_refdef_show=True):
        c = PCB.create_config_item()
        c.footprint = footprint
        c.layer = layer
        c.location = location
        c.rotate = rotate
        c.show = show
        c.silkscreen.refdef.show = silkscreen_refdef_show
        return c

    def parse_component_svg(self, svg_filename):
        return self.read_svg(join(self.board_components_dirpath, svg_filename))

    def add_component(self, library_component_name, board_component_name, location, **kwargs):
        # Auto use library component
        if library_component_name not in self.component_library:
            self.use_library_component(library_component_name)

        self.components[board_component_name]=  self.create_component(library_component_name, location, **kwargs)

    def save_component(self, component, component_name):
        return self.write_json(component, join(self.board_components_dirpath, component_name + '.json'))

    def save_components(self):
        for name, component in self.component_library.items():
            self.save_component(component, name)

    # Documentation Functions

    def add_documentation(self, section, location, text, font_size="1.5mm", line_height="1.5mm"):
        self.documentation[section] = self.clone(self.defaults.documentation)
        self.documentation[section].location = location
        self.documentation[section].value =text
        self.documentation[section].font_size = font_size
        self.documentation[section].line_height = line_height

    def add_outline(self, shape_name, width, height, radii, type="path"):
        self.outline.shape.height = height
        self.outline.shape.width = width
        self.outline.shape.radii = radii
        self.outline.shape.type = type
        self.outline.shape.value=self.parse_shape_svg(shape_name)

    def add_outline_path(self, paths, width, height, radii=dict(bl=3, br=3, tl=3, tr=3), type="path"):

        path = Path(*paths)

        self.outline.shape.height = height
        self.outline.shape.width = width
        self.outline.shape.radii = radii
        self.outline.shape.type = type
        self.outline.shape.value= absolute_to_relative_path(path.d())

    # Routing Functions

    def _add_route_to_layer(self, route, layer='bottom'):
        style = route['style'] if 'style' in route else ''
        key = utils.digest("%s%s" % (route['value'], style))

        self.routing.routes[layer][key] = route

    def add_route(self, paths, layer='bottom', stroke_width=0.4, style="stroke", type="path"):

        path = Path(*paths)

        self._add_route_to_layer({
            "stroke-width": stroke_width,
            "style": style,
            "type": type,
            "value": absolute_to_relative_path(path.d())
        }, layer=layer)

    def create_via(self, location, layer='top', footprint='via'):
        via = self.create_config_item()
        via.footprint = footprint
        via.layer = layer
        via.location = location
        via.rotate = 0
        via.show = True
        via.assembly.refdef.show = False
        via.silkscreen.refdef.show = False
        return via

    def add_via(self, location, layer='top', footprint='via'):
        via = self.create_via(location, layer, footprint)
        key = utils.digest("%s%s" % (via.location[0], via.location[1]))
        self.routing.vias[key] = via

    def board_component_pin_location(self, component_name, pin_name):
        board_component = self.components[component_name]
        board_component_footprint = board_component.footprint
        board_component_location = board_component.location

        library_component = self.component_library[board_component_footprint]
        library_component_pin_location = library_component.pins[pin_name].layout.location

        # TODO: Handle board_component.rotate
        location = [library_component_pin_location[0] + board_component_location[0],
                    library_component_pin_location[1] - board_component_location[1]]

        return location

    def connect_pins(self, c1, p1, c2, p2, **kwargs):
        start_pin = self.board_component_pin_location(c1, p1)
        end_pin = self.board_component_pin_location(c2, p2)

        self.add_route([Line(complex(start_pin[0], start_pin[1]), complex(end_pin[0], end_pin[1]))], **kwargs)

    # SVG Functions

    @classmethod
    def read_svg(cls, filepath):
        paths, attributes = svg2paths(filepath)

        for path in paths:
            return absolute_to_relative_path(path.d())

    def parse_shape_svg(self, svg_filename):
        return self.read_svg(join(self.board_shape_dirpath, svg_filename))

    @classmethod
    def create_square_shape(cls, w, h):
        return [
            Line(complex( 0, 0), complex( 0, h)),
            Line(complex( 0, h), complex( w, h)),
            Line(complex( w, h), complex( w, 0)),
            Line(complex( w, 0), complex( 0, 0)),
        ]

    def save(self):

        if not exists( self.board_components_dirpath):
            makedirs(self.board_components_dirpath)


        all = self.create_config_item()
        all.components = self.clone(self.components)
        all.config = self.clone(self.config)
        all.distances = self.clone(self.distances)
        all.documentation = self.clone(self.documentation)
        all.drill_index = self.clone(self.drill_index)
        all.drills = self.clone(self.drills)
        all.files = self.clone(self.files)
        all.gerber = self.clone(self.gerber)
        all.layer_control = self.clone(self.layer_control)
        all.outline = self.clone(self.outline)
        all.shapes = self.clone(self.shapes)
        all.soldermask = self.clone(self.soldermask)
        all.solderpaste = self.clone(self.solderpaste)
        all.stackup = self.clone(self.stackup)
        all.vias = self.clone(self.vias)

        self.write_json(all, self.board_json_filepath)

        self.save_components()
        self.save_routing()
        chdir(self.boards_root_dir)
        try:
            oldargv = sys.argv
            sys.argv = sys.argv[0::]
            sys.argv.extend(['-b', self.board_name, '-m',  '--make-board', '--fab', '--make-pngs'])
            #print(sys.argv)
            pcbmode.main()
        except Exception as e:
            print ("Warning: PCBmodE error ignored!")
        finally:
            sys.argv = oldargv

# Cyclic import dependencies go here...
from pcbmodezero.components import find_library_component
