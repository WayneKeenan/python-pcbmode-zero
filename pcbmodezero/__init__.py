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

    def __init__(self, boards_dir, board_name):
        self.boards_root_dir = join(boards_dir, '..')
        self.board_name = board_name
        self.board_root_filepath = "{}/boards/{}".format(self.boards_root_dir, self.board_name)
        self.board_json_filepath = "{}/boards/{}/{}.json".format(self.boards_root_dir, self.board_name, self.board_name)
        self.board_shape_dirpath = "{}/boards/{}/shapes".format(self.boards_root_dir, self.board_name)
        self.board_components_dirpath = "{}/boards/{}/components".format(self.boards_root_dir, self.board_name)
        self.configItem = jsontree.mapped_jsontree_class(self.underscore2minus)

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

    def underscore2minus(self, name):
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

    def clone(self, src):
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


    def readSVG(self, filepath):
        paths, attributes = svg2paths(filepath)

        for path in paths:
            return absolute_to_relative_path(path.d())

    def parseShapeSVG(self, svg_filename):
        return self.readSVG(join(self.board_shape_dirpath, svg_filename))


    def parseComponentSVG(self, svg_filename):
        return self.readSVG(join(self.board_components_dirpath, svg_filename))

    def saveComponent(self, component, component_name):
        return self.writeJSON(component, join(self.board_components_dirpath, component_name + '.json'))


    def saveRouting(self):
        return self.writeJSON(self.routing, join(self.board_root_filepath, self.board_name + '_routing.json'))

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