from math import sin, radians
from pcbmodezero import PCB

(BOARD_WIDTH, BOARD_HEIGHT) = (60, 60)

pcb = PCB(board_name ="procedural_pcb_1", boards_dir='../sandpit/boards', width = BOARD_WIDTH, height = BOARD_HEIGHT)

pcb.use_library_component('led-1206')

led_id = 0
x_pos = -BOARD_WIDTH/2 + 10
x_step = BOARD_WIDTH/10

while x_pos < BOARD_WIDTH/2 - 10 :
    y_pos = sin(radians(x_pos*5)) * BOARD_HEIGHT/2.2
    pcb.add_component('led-1206', 'LED_' + str(led_id), [x_pos, y_pos])
    x_pos += x_step
    led_id +=1


for led_id in range(1, led_id):
    pcb.route_pins('LED_' + str(led_id-1), '1', 'LED_' + str(led_id), '1')
    pcb.route_pins('LED_' + str(led_id-1), '2', 'LED_' + str(led_id), '2', layer='top')

pcb.save()
