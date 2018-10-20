from pcbmodezero import PCBmodEZero, Path, Line, CubicBezier

# The PCBmodE 'binco' board turned into Python config (massively simplified from original)

BOARD_NAME="binco_simplified"


pcb = PCBmodEZero(boards_dir='../sandpit/boards', board_name=BOARD_NAME)


# Components

# VIA

via = pcb.configItem()

via.pins['VIA'].layout.pad = 'via'
via.pins['VIA'].layout.location = [0, 0]
via.pads.via.shapes = [
    {
        "type": "circle",
        "layers": ["top", "internal", "bottom"],
        "style": "fill",
        "diameter": 0.95,
        "soldermask": {},
        "solderpaste": {}
    }
]
via.pads.drill.drills = [
    {
        "diameter": 0.5
    }
]

pcb.saveComponent(via, 'via')


# LED


led_1206 = pcb.configItem()

led_1206.pins['1'].layout.pad = 'smd'
led_1206.pins['1'].layout.location = [-1.8, 0]
led_1206.pins['1'].layout.rotate = 180

led_1206.pins['2'].layout.pad = 'smd'
led_1206.pins['2'].layout.location = [1.8, 0]
led_1206.pins['2'].layout.rotate = 0

led_1206.pins['DRILL'].layout.pad = 'drill'
led_1206.pins['DRILL'].layout.location = [0, 0]

led_1206.layout.silkscreen.shapes = []

led_1206.layout.assembly.shapes = [
    {
        "type": "rect",
        "style": "stroke",
        "stroke-width": 0.1,
        "width": 3.2,
        "height": 1.6
    },
    {
        "type": "circle",
        "style": "fill",
        "diameter": 1.6
    }
]

led_1206.pads.smd.shapes = [
    {
        "type": "path",
        "value": pcb.parseComponentSVG('led-1206.svg'),
        "rotate": 90,
        "width": 1.5,
        "height": 1.6,
        "radii": {
            "bl": 0,
            "br": 0.3,
            "tl": 0,
            "tr": 0.3
        }
    }
]

led_1206.pads.drill.shapes = [
    {
        "type": "circle",
        "layers": ["top", "bottom"],
        "style": "fill",
        "diameter": 0.5,
        "buffer-to-pour": 0.8,
        "solderpaste": {}
    }
]

led_1206.pads.drill.drills = [
    {
        "diameter": 1.8
    }
]

#print(led_1206)

pcb.saveComponent(led_1206, 'led-1206')

# Instatiated Boards Components

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


# Routing

pcb.addRoute(Path(Line(3+0j, 3-1j), Line(3+0j, 3.5+0j)))
pcb.addRoute(Path(CubicBezier(1+1j, 2+2j, 4+2j, 5+1j)), layer='top')
pcb.addVia([1.5, 2])
pcb.addVia([4.5, 2])


pcb.save()
