from pcbmodezero import PCBmodEZero, Path, Line, CubicBezier
from pcbmodezero.components.leds import led_1206
from pcbmodezero.components.vias import default_via

BOARD_NAME="binco_minified"

pcb = PCBmodEZero(boards_dir='../sandpit/boards', board_name=BOARD_NAME)

# Component Library

pcb.addLibraryComponent(default_via, 'via')
pcb.addLibraryComponent(led_1206, 'led-1206')

# Board Component instances

led1 = pcb.configItem()
led1.footprint = 'led-1206'
led1.layer = "bottom"
led1.location = [-11.535056, 9.321493]
led1.rotate = 90
led1.show = True
led1.silkscreen.refdef.show = True

# Copy LED and modify its location
led10 = pcb.clone(led1)
led10.location = [-3.838085, 9.321493]

pcb.components.LED1 = led1
pcb.components.LED10 = led10

# PCBmodE Board Config

pcb.config.name = 'test1'
pcb.config.no_docs = False
pcb.config.no_drill_index = False
pcb.config.no_flashes = False
pcb.config.no_layer_index = False
pcb.config.rev = "first"
pcb.config.style_layout = "default"
pcb.config.units = "mm"

pcb.documentation.board_details = pcb.clone(pcb.defaults.documentation)
pcb.documentation.board_details.location = [-12.039821, -30.831399]
pcb.documentation.board_details.value = "Board details: ..."

pcb.documentation.manufacturing = pcb.clone(pcb.defaults.documentation)
pcb.documentation.manufacturing.location = [-12.243017, -18.347399]
pcb.documentation.manufacturing.value = "Manufacturing:..."

pcb.documentation.pcbmode = pcb.clone(pcb.defaults.documentation)
pcb.documentation.pcbmode.font_size = "1.2mm"
pcb.documentation.pcbmode.line_height = "1.2mm"
pcb.documentation.pcbmode.location = [-15.849812, -41.294399]
pcb.documentation.pcbmode.value = "Designed with PCBmodE"

pcb.drill_index.location = [-27.971101, -47.126399]

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

# Routing

pcb.addRoute([Line(3+0j, 3-1j), Line(3+0j, 3.5+0j)])
pcb.addRoute([CubicBezier(1+1j, 2+2j, 4+2j, 5+1j)], layer='top')
pcb.addVia([1.5, 2])
pcb.addVia([4.5, 2])

pcb.save()
