from pprint import pformat
from os import chdir
from sys import argv

import jsontree
from pcbmode import pcbmode


#json2py("../../boards/test1/test1.json")

class pcbmodezero:

    def __init__(self):
        self.json = jsontree.mapped_jsontree_class(self.underscore2minus)

        self.components= self.json()

        self.config = self.json()
        self.distances = self.json()
        self.documentation = self.json()
        self.layer_control = self.json()
        self.gerber = self.json()
        self.files = self.json()
        self.drills = self.json()
        self.drill_index = self.json()
        self.outline = self.json()
        self.shapes = self.json()

        self.soldermask = self.json()
        self.solderpaste = self.json()
        self.stackup = self.json()
        self.vias = self.json()

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


    def clone(self, src):
        return jsontree.clone(src)

    def save(self):
        all = self.json()
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

        all_json = jsontree.dumps(all, indent=4)
        print (all_json)

        boards_root_dir = "../../"
        board_name = 'test_py_1'

        board_json_filepath = "{}/boards/{}/{}.json".format(boards_root_dir, board_name, board_name)

        with open(board_json_filepath, 'w') as file:
            file.write(all_json)

        chdir(boards_root_dir)
        argv.extend(['-b', board_name, '-m'])
        print(argv)
        pcbmode.main()


p = pcbmodezero()

# Components

led1 = p.json()
led1.footprint='led-1206'
led1.layer="bottom"
led1.location = [ -11.535056, 9.321493 ]
led1.rotate = 90
led1.show = True
led1['silkscreen']['refdef']['show'] = True

led10 = p.clone(led1)
led10.location = [ -3.838085, 9.321493]

# PCBmodE Config

p.components.LED1 = led1
p.components.LED10 = led10


p.config.name='test1'
p.config.no_docs = False
p.config.no_drill_index = False
p.config.no_flashes = False
p.config.no_layer_index = False
p.config.rev = "first"
p.config.style_layout = "default"
p.config.units = "mm"


p.distances.from_pour_to.drill = 0.25
p.distances.from_pour_to.outline = 0.4
p.distances.from_pour_to.pad = 0.25
p.distances.from_pour_to.route = 0.25

p.distances.soldermask.circle_buffer = 0.05
p.distances.soldermask.path_scale = 1.05
p.distances.soldermask.rect_buffer = 0.05

p.distances.solderpaste.circle_buffer = -0.1
p.distances.solderpaste.path_scale = 0.9
p.distances.solderpaste.rect_buffer = -0.1


p.documentation.board_details.font_family = "Overlock-Regular-OTF-webfont"
p.documentation.board_details.font_size = "1.5mm"
p.documentation.board_details.letter_spacing = "0mm"
p.documentation.board_details.line_height = "1.5mm"
p.documentation.board_details.location = [ -12.039821, -30.831399]
p.documentation.board_details.rotate = 0
p.documentation.board_details.style = "fill"
p.documentation.board_details.type = "text"
p.documentation.board_details.value = "Board details:\nName: BINCO\nRevision: first\nDescription: a binary counter \nLicense: MIT\nDesigner: Saar Drimer, Boldport, saar@boldport.com"

p.documentation.manufacturing = p.clone(p.documentation.board_details)
p.documentation.manufacturing.location = [ -12.243017, -18.347399 ]
p.documentation.manufacturing.value = "Manufacturing:\nRoHS and lead free compliant manufacturing process\nUnit of length: Millimetre (mm)\nNumber of layers: 2 ('top', 'bottom')\nBoard thickness: 1.6 mm\nMaterial: FR4 35/35 um copper\nSilkscreen: top, bottom, white\nSoldermask: top, bottom (green)\nSurface finish: lead free"

p.documentation.pcbmode = p.clone(p.documentation.board_details)
p.documentation.pcbmode.font_size = "1.2mm"
p.documentation.pcbmode.line_height = "1.2mm"
p.documentation.pcbmode.location =  [ -15.849812, -41.294399 ]
p.documentation.pcbmode.value = "Designed with PCBmodE, an open source software\n     http://pcbmode.com\nStay updated:\n     @boldport @pcbmode http://boldport.com"


p.drill_index.location = [ -27.971101, -47.126399 ]


p.drills = {}


p.files.routing_data = "test1_routing.json"
p.files.routing_svg = "test1.svg"


p.gerber.decimals = 6
p.gerber.digits = 6
p.gerber.min_segment_length = 0.05
p.gerber.steps_per_segment = 100


p.layer_control.assembly = dict(hide=False, lock=False, place=True)
p.layer_control.conductor.hide = False
p.layer_control.conductor.lock = False
p.layer_control.conductor.place = True
p.layer_control.conductor.pads = dict(hide=False, lock=False, place=True)
p.layer_control.conductor.pours = dict(hide=False, lock=True, place=True)
p.layer_control.conductor.routing = dict(hide=False, lock=False, place=True)
p.layer_control.dimensions= dict(hide=False, lock=True, place=True)
p.layer_control.documentation = dict(hide=False, lock=False, place=True)
p.layer_control.drills = dict(hide=False, lock=False, place=True)
p.layer_control.origin= dict(hide=False, lock=True, place=False)
p.layer_control.outline = dict(hide=False, lock=True, place=True)
p.layer_control.placement = dict(hide=False, lock=False, place=True)
p.layer_control.silkscreen = dict(hide=False, lock=False, place=True)
p.layer_control.soldermask = dict(hide=False, lock=False, place=True)
p.layer_control.solderpaste = dict(hide=True, lock=True, place=False)


p.outline.shape.height = 22
p.outline.shape.width = 51
p.outline.shape.radii = dict(bl = 3, br = 3, tl = 3, tr = 3)
p.outline.shape.type = "path"
p.outline.shape.value = "m 10.858333,11 c 2.140681,-0.340482 4.281363,-0.680964 6.422044,-1.0214454 1.69236,-1.0123173 3.384721,-2.0246345 5.077081,-3.0369518 1.2656,-2.1059322 2.531201,-4.2118644 3.796801,-6.31779663 0.663858,-2.34543537 1.327716,-4.69087077 1.991574,-7.03630647 -0.223524,-1.829043 -0.447047,-3.6580857 -0.670571,-5.4871287 -0.600087,-0.758457 -1.200175,-1.516914 -1.800262,-2.275371 -17.1166667,0 -34.2333333,0 -51.35,0 -0.600087,0.758457 -1.200175,1.516914 -1.800262,2.275371 -0.223524,1.829043 -0.447047,3.6580857 -0.670571,5.4871287 0.663858,2.3454357 1.327716,4.6908711 1.991574,7.03630647 1.2656,2.10593223 2.531201,4.21186443 3.796801,6.31779663 1.69236,1.0123173 3.384721,2.0246345 5.077081,3.0369518 2.140681,0.3404814 4.281363,0.6809634 6.422044,1.0214454 7.2388887,0 14.4777773,0 21.716666,0 z"


p.shapes = {}


p.soldermask.circle_buffer = 0.05
p.soldermask.path_scale = 1.05
p.soldermask.rect_buffer = 0.05


p.solderpaste.circle_buffer = -0.1
p.solderpaste.path_scale = 0.9
p.solderpaste.rect_buffer = -0.1


p.stackup.name = "two-layer"


p.vias.default_via = "VIA"

p.save()