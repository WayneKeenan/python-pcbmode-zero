from pcbmodezero import PCB

# Hello world example, place an LED (from the built-in part library)
# in the middle of a 30mm x 30mm PCB

pcb = PCB(board_name ="hello_pcb", width=30, height=30)
pcb.add_component('led-1206', 'LED1', [0,  0])
pcb.save()

