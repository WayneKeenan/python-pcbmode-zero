# LED
import pkg_resources
from pcbmodezero import PCB

LED_SVG_RESOURCE = pkg_resources.resource_filename(__name__, "led-1206.svg")


led_1206 = PCB.create_config_item()

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
        "value": PCB.read_svg(LED_SVG_RESOURCE),
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

