from pprint import pformat
from os import chdir
from os.path import join
import sys
import io

import jsontree

from svgpathtools import Path, Line, QuadraticBezier, CubicBezier, Arc, svg2paths

from pcbmode import pcbmode
from pcbmode.utils import utils
from pcbmode.utils.svg import absolute_to_relative_path



class PCBmodEZero:

    def __init__(self, boards_dir, board_name, rev="first"):
        self.boards_root_dir = join(boards_dir, '..')
        self.board_name = board_name
        self.board_root_filepath = "{}/boards/{}".format(self.boards_root_dir, self.board_name)
        self.board_json_filepath = "{}/boards/{}/{}.json".format(self.boards_root_dir, self.board_name, self.board_name)
        self.board_shape_dirpath = "{}/boards/{}/shapes".format(self.boards_root_dir, self.board_name)
        self.board_components_dirpath = "{}/boards/{}/components".format(self.boards_root_dir, self.board_name)
        self.component_library = {}


        self.components= self.configItem()
        self.config = self.configItem()
        self.distances = self.configItem()
        self.documentation = self.configItem()
        self.layer_control = self.configItem()
        self.gerber = self.configItem()
        self.files = self.configItem()
        self.drills = self.configItem()
        self.drill_index = self.configItem()
        self.outline = self.configItem()
        self.shapes = self.configItem()
        self.soldermask = self.configItem()
        self.solderpaste = self.configItem()
        self.stackup = self.configItem()
        self.vias = self.configItem()

        self.routing = self.configItem()
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
        self.defaults = self.configItem()
        self.defaults.documentaion = self.configItem()
        self.defaults.documentation.font_family = "Overlock-Regular-OTF-webfont"
        self.defaults.documentation.font_size = "1.5mm"
        self.defaults.documentation.letter_spacing = "0mm"
        self.defaults.documentation.line_height = "1.5mm"
        self.defaults.documentation.location = [0, 0]
        self.defaults.documentation.rotate = 0
        self.defaults.documentation.style = "fill"
        self.defaults.documentation.type = "text"
        self.defaults.documentation.value = "Warning: No Text Set"




        self.preinit_pcbmode()

    @classmethod
    def configItem(cls):
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

    def json2py(self, filepath):
        with open(filepath, 'r') as file:
            txt = file.read()
            decoder = jsontree.JSONTreeDecoder()
            decoded = decoder.decode(txt)
            #print(pformat(decoded))
            #print(jsontree.dumps(decoded, indent=4))
            return decoded

    @classmethod
    def underscore2minus(cls, name):
        if name == '__class__':
            raise ValueError
        return name.replace('_', '-')

    def writeJSON(self, json_obj, filepath):
        json_txt = jsontree.dumps(json_obj, indent=4)
        #print (all_json)

        with open(filepath, 'w') as file:
            file.write(json_txt)

    def dumpJSON(self, json_obj):
        print(jsontree.dumps(json_obj, indent=4))

    @classmethod
    def clone(cls, src):
        return jsontree.clone(src)

    def save(self):
        all = self.configItem()
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

        self.writeJSON(all, self.board_json_filepath)

        self.saveComponents()
        self.saveRouting()
        chdir(self.boards_root_dir)
        try:
            oldargv = sys.argv
            sys.argv = sys.argv[0::]
            sys.argv.extend(['-b', self.board_name, '-m'])
            #print(sys.argv)
            pcbmode.main()
        finally:
            sys.argv = oldargv


    @classmethod
    def readSVG(cls, filepath):
        paths, attributes = svg2paths(filepath)

        for path in paths:
            return absolute_to_relative_path(path.d())


    def parseShapeSVG(self, svg_filename):
        return self.readSVG(join(self.board_shape_dirpath, svg_filename))


    def parseComponentSVG(self, svg_filename):
        return self.readSVG(join(self.board_components_dirpath, svg_filename))

    def addComponent(self, component, component_name):
        if component_name in self.component_library:
            raise ValueError("%s already exists.".format(component_name))
        self.component_library[component_name] = component


    def addLibraryComponent(self, component_name):
        self.addComponent(findLibraryComponent(component_name), component_name)


    def saveComponent(self, component, component_name):
        return self.writeJSON(component, join(self.board_components_dirpath, component_name + '.json'))

    def saveComponents(self):
        for name, component in self.component_library.items():
            self.saveComponent(component, name)


    def saveRouting(self):
        return self.writeJSON(self.routing, join(self.board_root_filepath, self.board_name + '_routing.json'))

    @classmethod
    def createComponent(cls, footprint, location, layer="bottom", rotate=0, show=True, silkscreen_refdef_show=True):
        c = PCBmodEZero.configItem()
        c.footprint = footprint
        c.layer = layer
        c.location = location
        c.rotate = rotate
        c.show = show
        c.silkscreen.refdef.show = silkscreen_refdef_show
        return c


    def createVia(self, location, layer='top', footprint='via'):
        via = self.configItem()
        via.footprint = footprint
        via.layer = layer
        via.location = location
        via.rotate = 0
        via.show = True
        via.assembly.refdef.show = False
        via.silkscreen.refdef.show = False
        return via

    def _addRouteToLayer(self, route, layer='bottom'):
        style = route['style'] if 'style' in route else ''
        key = utils.digest("%s%s" % (route['value'], style))

        self.routing.routes[layer][key] = route

    def addRoute(self, paths, layer='bottom', stroke_width=0.4, style="stroke", type="path"):

        path = Path(*paths)

        self._addRouteToLayer({
            "stroke-width": stroke_width,
            "style": style,
            "type": type,
            "value": absolute_to_relative_path(path.d())
        }, layer=layer)

    def addVia(self, location, layer='top', footprint='via'):
        via = self.createVia(location, layer, footprint)
        key = utils.digest("%s%s" % (via.location[0], via.location[1]))
        self.routing.vias[key] = via


    def addDocumentation(self, section, location, text, font_size="1.5mm", line_height="1.5mm"):
        self.documentation[section] = self.clone(self.defaults.documentation)
        self.documentation[section].location = location
        self.documentation[section].value =text
        self.documentation[section].font_size = font_size
        self.documentation[section].line_height = line_height


    def addOutline(self, shape_name, width, height, radii, type="path"):
        self.outline.shape.height = height
        self.outline.shape.width = width
        self.outline.shape.radii = radii
        self.outline.shape.type = type
        self.outline.shape.value=self.parseShapeSVG(shape_name)

from pcbmodezero.components import findLibraryComponent
