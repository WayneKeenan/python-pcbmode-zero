from pcbmodezero import PCBmodEZero

# The PCBmodE 'binco' board turned into Python config (massively simplified from original)

BOARD_NAME="binco_simplified"


pcb = PCBmodEZero(boards_parent_dir='../sandpit', board_name=BOARD_NAME)

# Boards Components

led1 = pcb.configItem()
led1.footprint='led-1206'
led1.layer="bottom"
led1.location = [-11.535056, 9.321493]
led1.rotate = 90
led1.show = True
led1.silkscreen.refdef.show = True


# Copy LED and modify it by location
led10 = pcb.clone(led1)
led10.location = [-3.838085, 9.321493]



# PCBmodE Config

pcb.components.LED1 = led1
pcb.components.LED10 = led10


pcb.config.name= 'test1'
pcb.config.no_docs = False
pcb.config.no_drill_index = False
pcb.config.no_flashes = False
pcb.config.no_layer_index = False
pcb.config.rev = "first"
pcb.config.style_layout = "default"
pcb.config.units = "mm"


pcb.distances.from_pour_to.drill = 0.25
pcb.distances.from_pour_to.outline = 0.4
pcb.distances.from_pour_to.pad = 0.25
pcb.distances.from_pour_to.route = 0.25

pcb.distances.soldermask.circle_buffer = 0.05
pcb.distances.soldermask.path_scale = 1.05
pcb.distances.soldermask.rect_buffer = 0.05

pcb.distances.solderpaste.circle_buffer = -0.1
pcb.distances.solderpaste.path_scale = 0.9
pcb.distances.solderpaste.rect_buffer = -0.1


pcb.documentation.board_details = pcb.clone(pcb.defaults.documentation)
pcb.documentation.board_details.location = [-12.039821, -30.831399]
pcb.documentation.board_details.value = """Board details:
Name: BINCO
Revision: first
Description: a binary counter
License: MIT
Designer: Saar Drimer, Boldport, saar@boldport.com"""

pcb.documentation.manufacturing = pcb.clone(pcb.defaults.documentation)
pcb.documentation.manufacturing.location = [-12.243017, -18.347399]
pcb.documentation.manufacturing.value = """Manufacturing:
RoHS and lead free compliant manufacturing process
Unit of length: Millimetre (mm)
Number of layers: 2 ('top', 'bottom')
Board thickness: 1.6 mm
Material: FR4 35/35 um copper
ilkscreen: top, bottom, white
Soldermask: top, bottom (green)
Surface finish: lead free!"""

pcb.documentation.pcbmode = pcb.clone(pcb.defaults.documentation)
pcb.documentation.pcbmode.font_size = "1.2mm"
pcb.documentation.pcbmode.line_height = "1.2mm"
pcb.documentation.pcbmode.location = [-15.849812, -41.294399]
pcb.documentation.pcbmode.value = """Designed with PCBmodE, an open source software
     http://pcbmode.com
Stay updated:
     @boldport @pcbmode http://boldport.com"""


pcb.drill_index.location = [-27.971101, -47.126399]


pcb.drills = {}

pcb.files.routing_data = BOARD_NAME + "_routing.json"
pcb.files.routing_svg = BOARD_NAME + ".svg"


pcb.gerber.decimals = 6
pcb.gerber.digits = 6
pcb.gerber.min_segment_length = 0.05
pcb.gerber.steps_per_segment = 100


pcb.layer_control.assembly = dict(hide=False, lock=False, place=True)
pcb.layer_control.conductor.hide = False
pcb.layer_control.conductor.lock = False
pcb.layer_control.conductor.place = True
pcb.layer_control.conductor.pads = dict(hide=False, lock=False, place=True)
pcb.layer_control.conductor.pours = dict(hide=False, lock=True, place=True)
pcb.layer_control.conductor.routing = dict(hide=False, lock=False, place=True)
pcb.layer_control.dimensions= dict(hide=False, lock=True, place=True)
pcb.layer_control.documentation = dict(hide=False, lock=False, place=True)
pcb.layer_control.drills = dict(hide=False, lock=False, place=True)
pcb.layer_control.origin= dict(hide=False, lock=True, place=False)
pcb.layer_control.outline = dict(hide=False, lock=True, place=True)
pcb.layer_control.placement = dict(hide=False, lock=False, place=True)
pcb.layer_control.silkscreen = dict(hide=False, lock=False, place=True)
pcb.layer_control.soldermask = dict(hide=False, lock=False, place=True)
pcb.layer_control.solderpaste = dict(hide=True, lock=True, place=False)


pcb.outline.shape.height = 22
pcb.outline.shape.width = 51
pcb.outline.shape.radii = dict(bl=3, br=3, tl=3, tr=3)
pcb.outline.shape.type = "path"
pcb.outline.shape.value=pcb.parseShapeSVG('outline.svg')


pcb.shapes = {}


pcb.soldermask.circle_buffer = 0.05
pcb.soldermask.path_scale = 1.05
pcb.soldermask.rect_buffer = 0.05


pcb.solderpaste.circle_buffer = -0.1
pcb.solderpaste.path_scale = 0.9
pcb.solderpaste.rect_buffer = -0.1


pcb.stackup.name = "two-layer"


pcb.vias.default_via = "VIA"


pcb.save()