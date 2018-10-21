from pcbmodezero import PCB, Path


COMPONENT_NAME='mycomponent'

pcb = PCB(board_name ="mycomponent_test", width=30, height=30)



c = PCB.create_config_item()

c.pins['1'].layout.pad = 'smd'
c.pins['1'].layout.location = [-1.8, 0]
c.pins['1'].layout.rotate = 180

c.pads.smd.shapes = [
    {
        "type": "path",
        "value": Path(*PCB.create_square_shape(10,10)).d(),
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


pcb.add_library_component(c, COMPONENT_NAME)

pcb.add_component(COMPONENT_NAME, 'mycomponent1', [0,  0])

pcb.save()