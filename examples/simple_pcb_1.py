from pcbmodezero import PCB, Line

(BOARD_WIDTH, BOARD_HEIGHT) = (30, 30)

pcb = PCB(board_name ="simple_pcb_1", boards_dir='../sandpit/boards')

pcb.add_documentation('manufacturing', [0, -BOARD_HEIGHT /2], "Manufacturing:...")
pcb.add_documentation('board_details', [0, -BOARD_HEIGHT ], "Board details: ...")
pcb.add_documentation('pcbmode', [0, -BOARD_WIDTH], "Designed with PCBmodE:...", font_size ="1.2", line_height ="1.2")

pcb.add_library_component('led-1206')

pcb.components.LED1 = pcb.create_component('led-1206', [0, 0])
pcb.components.LED2 = pcb.create_component('led-1206', [5, 10])


pcb.connect_pins('LED1', '1', 'LED2', '1')
pcb.connect_pins('LED1', '2', 'LED2', '2')


square = [
    Line(complex(           0,            0), complex(           0,   BOARD_HEIGHT)),
    Line(complex(           0, BOARD_HEIGHT), complex( BOARD_WIDTH,   BOARD_HEIGHT)),
    Line(complex( BOARD_WIDTH, BOARD_HEIGHT), complex( BOARD_WIDTH,              0)),
    Line(complex( BOARD_WIDTH,            0), complex(           0,              0)),
]

pcb.add_outline_path(square , width = 40, height = 40 )

pcb.add_route([Line(3 + 0j, 3 - 1j), Line(3 + 0j, 3.5 + 0j)])

pcb.drill_index.location = [0, -BOARD_HEIGHT]


pcb.save()

