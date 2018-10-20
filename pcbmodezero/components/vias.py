from pcbmodezero import PCB

via = PCB.create_config_item()

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


default_via = via