from pcbmodezero import PCB, Line

(BOARD_WIDTH, BOARD_HEIGHT) = (30, 30)
BOARD_OUTLINE = PCB.create_square_shape(BOARD_WIDTH, BOARD_HEIGHT)

pcb = PCB(board_name ="simple_pcb_1", boards_dir='../sandpit/boards')

pcb.add_documentation('manufacturing', [0, -BOARD_HEIGHT /2], "Manufacturing:...")
pcb.add_documentation('board_details', [0, -BOARD_HEIGHT ], "Board details: ...")
pcb.add_documentation('pcbmode', [0, -BOARD_WIDTH], "Designed with PCBmodE:...", font_size ="1.2", line_height ="1.2")
pcb.drill_index.location = [0, -BOARD_HEIGHT]

pcb.add_library_component('led-1206')

pcb.add_component('led-1206', 'LED1', [0,  0])
pcb.add_component('led-1206', 'LED2', [5, 10])

pcb.route_pins('LED1', '1', 'LED2', '1')
pcb.route_pins('LED1', '2', 'LED2', '2')

pcb.add_outline_path(BOARD_OUTLINE , width = 40, height = 40 )

pcb.save()

