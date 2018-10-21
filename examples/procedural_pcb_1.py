from math import sin, radians
from pcbmodezero import PCB

(BOARD_WIDTH, BOARD_HEIGHT) = (60, 60)
LED = 'led-1206'

pcb = PCB(board_name ="procedural_pcb_1", boards_dir='../sandpit/boards', width = BOARD_WIDTH, height = BOARD_HEIGHT)

pcb.use_library_component(LED)

led_id = 0
x_pos = -BOARD_WIDTH/2 + 10

# Create a sine wave arrangement of LED parts on the PCB

while x_pos < BOARD_WIDTH/2 - 10 :
    y_pos = sin(radians(x_pos*5)) * BOARD_HEIGHT/2.2
    pcb.add_component(LED, 'LED_%d' % led_id, [x_pos, y_pos])
    x_pos += BOARD_WIDTH/10

    led_id +=1

# Connect each LED pins 1 and 2 to the previous LED pins in list.

for led_id in range(1, led_id):
    pcb.connect_pins('LED_%d' % (led_id - 1), '1', 'LED_%d' % led_id, '1')
    pcb.connect_pins('LED_%d' % (led_id - 1), '2', 'LED_%d' % led_id, '2', layer='top')

pcb.save()
