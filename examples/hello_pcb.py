from pcbmodezero import PCB

# Hello world example, place an LED in the middle of a 30mm x 30mm PCB

LED_COMPONENT='led-1206'

pcb = PCB(board_name ="hello_pcb", width=30, height=30)

pcb.use_library_component(LED_COMPONENT)

pcb.add_component(LED_COMPONENT, 'LED1', [0,  0])

pcb.save()

