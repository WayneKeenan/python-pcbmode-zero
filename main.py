from pprint import pformat


import jsontree
from jsontree import clone as clone



def json2py(filepath):
    with open(filepath, 'r') as file:
        txt = file.read()
        decoder = jsontree.JSONTreeDecoder()
        decoded = decoder.decode(txt)
        #print(pformat(decoded))
        #print(jsontree.dumps(decoded, indent=4))
        return decoded


#json2py("../../boards/test1/test1.json")




def underscore2minus(name):
    if name == '__class__':
        raise ValueError
    return name.replace('_', '-')

json = jsontree.mapped_jsontree_class(underscore2minus)


# Components


led1 = json()
led1.footprint='led-1206'
led1.layer="bottom"
led1.location = [ -11.535056, 9.321493 ]
led1.rotate = 90
led1.show = True
led1['silkscreen']['refdef']['show'] = True

led10 = clone(led1)
led10.location = [ -3.838085, 9.321493]


components= json()
components.LED1 = led1
components.LED10 = led10



# Config

config = json()
config.name='test1'
config.no_docs = False
config.no_drill_index = False
config.no_flashes = False
config.no_layer_index = False
config.rev = "first"
config.style_layout = "default"
config.units = "mm"


# Distances

distances = json()

distances.from_pour_to.drill = 0.25
distances.from_pour_to.outline = 0.4
distances.from_pour_to.pad = 0.25
distances.from_pour_to.route = 0.25

distances.soldermask.circle_buffer = 0.05
distances.soldermask.path_scale = 1.05
distances.soldermask.rect_buffer = 0.05

distances.solderpaste.circle_buffer = -0.1
distances.solderpaste.path_scale = 0.9
distances.solderpaste.rect_buffer = -0.1


# Documentation

documentation = json()

documentation.board_details.font_family = "Overlock-Regular-OTF-webfont"
documentation.board_details.font_size = "1.5mm"
documentation.board_details.letter_spacing = "0mm"
documentation.board_details.line_height = "1.5mm"
documentation.board_details.location = [ -12.039821, -30.831399]
documentation.board_details.rotate = 0
documentation.board_details.style = "fill"
documentation.board_details.type = "text"
documentation.board_details.value = "Board details:\nName: BINCO\nRevision: first\nDescription: a binary counter \nLicense: MIT\nDesigner: Saar Drimer, Boldport, saar@boldport.com"


documentation.manufacturing.font_family = "Overlock-Regular-OTF-webfont"
documentation.manufacturing.font_size = "1.5mm"
documentation.manufacturing.letter_spacing = "0mm"
documentation.manufacturing.line_height = "1.5mm"
documentation.manufacturing.location = [ -12.243017, -18.347399 ]
documentation.manufacturing.rotate = 0
documentation.manufacturing.style = "fill"
documentation.manufacturing.type = "text"
documentation.manufacturing.value = "Manufacturing:\nRoHS and lead free compliant manufacturing process\nUnit of length: Millimetre (mm)\nNumber of layers: 2 ('top', 'bottom')\nBoard thickness: 1.6 mm\nMaterial: FR4 35/35 um copper\nSilkscreen: top, bottom, white\nSoldermask: top, bottom (green)\nSurface finish: lead free"


documentation.pcbmode.font_family = "Overlock-Regular-OTF-webfont"
documentation.pcbmode.font_size = "1.2mm"
documentation.pcbmode.letter_spacing = "0mm"
documentation.pcbmode.line_height = "1.2mm"
documentation.pcbmode.location = [ -15.849812, -41.294399 ]
documentation.pcbmode.rotate = 0
documentation.pcbmode.style = "fill"
documentation.pcbmode.type = "text"
documentation.pcbmode.value = "Designed with PCBmodE, an open source software\n     http://pcbmode.com\nStay updated:\n     @boldport @pcbmode http://boldport.com"





# Drill Index

drill_index = json()

drill_index.location = [ -27.971101, -47.126399 ]

# Drills

drills = json()


# Files

files = json()

files.routing_data = "test1_routing.json"
files.routing_svg = "test1.svg"

# Gerber

gerber = json()

gerber.decimals = 6
gerber.digits = 6
gerber.min_segment_length = 0.05
gerber.steps_per_segment = 100

# Layer Control

layer_control = json()

layer_control.assembly = dict(hide = False, lock= False, place = True)
layer_control.conductor.hide = False
layer_control.conductor.lock = False
layer_control.conductor.place = True
layer_control.conductor.pads = dict(hide = False, lock= False, place = True)
layer_control.conductor.pours = dict(hide = False, lock= True, place = True)
layer_control.conductor.routing = dict(hide = False, lock= False, place = True)
layer_control.dimensions= dict(hide = False, lock= True, place = True)
layer_control.documentation = dict(hide = False, lock= False, place = True)
layer_control.drills = dict(hide = False, lock= False, place = True)
layer_control.origin= dict(hide = False, lock= True, place = False)
layer_control.outline = dict(hide = False, lock= True, place = True)
layer_control.placement = dict(hide = False, lock= False, place = True)
layer_control.silkscreen = dict(hide = False, lock= False, place = True)
layer_control.soldermask = dict(hide = False, lock= False, place = True)
layer_control.solderpaste = dict(hide = True, lock= True, place = False)


# OUtline

outline = json()

outline.shape.height = 22
outline.shape.width = 51
outline.shape.radii = dict(bl = 3, br = 3, tl = 3, tr = 3)
outline.shape.type = "path"
outline.shape.value = "m 10.858333,11 c 2.140681,-0.340482 4.281363,-0.680964 6.422044,-1.0214454 1.69236,-1.0123173 3.384721,-2.0246345 5.077081,-3.0369518 1.2656,-2.1059322 2.531201,-4.2118644 3.796801,-6.31779663 0.663858,-2.34543537 1.327716,-4.69087077 1.991574,-7.03630647 -0.223524,-1.829043 -0.447047,-3.6580857 -0.670571,-5.4871287 -0.600087,-0.758457 -1.200175,-1.516914 -1.800262,-2.275371 -17.1166667,0 -34.2333333,0 -51.35,0 -0.600087,0.758457 -1.200175,1.516914 -1.800262,2.275371 -0.223524,1.829043 -0.447047,3.6580857 -0.670571,5.4871287 0.663858,2.3454357 1.327716,4.6908711 1.991574,7.03630647 1.2656,2.10593223 2.531201,4.21186443 3.796801,6.31779663 1.69236,1.0123173 3.384721,2.0246345 5.077081,3.0369518 2.140681,0.3404814 4.281363,0.6809634 6.422044,1.0214454 7.2388887,0 14.4777773,0 21.716666,0 z"


# Shapes

shapes = json()


# Solder Mask

soldermask = json()

soldermask.circle_buffer = 0.05
soldermask.path_scale = 1.05
soldermask.rect_buffer = 0.05

# Solder Paste

solderpaste = json()

solderpaste.circle_buffer = -0.1
solderpaste.path_scale = 0.9
solderpaste.rect_buffer = -0.1


# Stack Up

stackup = json()
stackup.name = "two-layer"

# Vias

vias = json()
vias.default_via = "VIA"

all= json()
all.components = clone(components)
all.config = clone(config)
all.distances = clone(distances)
all.documentation = clone(documentation)
all.drill_index = clone(drill_index)
all.drills = clone(drills)
all.files = clone(files)
all.gerber = clone(gerber)
all.layer_control = clone(layer_control)
all.outline = clone(outline)
all.shapes = clone(shapes)
all.soldermask = clone(soldermask)
all.solderpaste = clone(solderpaste)
all.stackup = clone(stackup)
all.vias = clone(vias)




all_json = jsontree.dumps(all, indent=4)
print (all_json)

boards_root_dir = "../../"
board_name = 'test_py_1'

board_json_filepath= "{}/boards/{}/{}.json".format(boards_root_dir, board_name, board_name)

with open(board_json_filepath, 'w') as file:
    file.write(all_json)


from pcbmode import pcbmode

from os import chdir
from sys import argv
chdir(boards_root_dir)
argv.extend(['-b', board_name, '-m'])
print(argv)
pcbmode.main()


