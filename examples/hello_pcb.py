from pcbmodezero import PCB, Line

pcb = PCB(board_name ="hello_pcb", boards_dir='../sandpit/boards', width=30, height=30)

pcb.use_library_component('led-1206')
pcb.add_component('led-1206', 'LED1', [0,  0])
pcb.save()

