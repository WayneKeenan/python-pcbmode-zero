from pcbmodezero import PCBmodEZero, Line, CubicBezier

BOARD_NAME="binco_minified"

pcb = PCBmodEZero(boards_dir='../sandpit/boards', board_name=BOARD_NAME)

# Import from built-in Component Library

pcb.addLibraryComponent('via')
pcb.addLibraryComponent('led-1206')
pcb.addLibraryComponent('555-SOIC8')

# Create Component instances

pcb.components.LED1 = pcb.createComponent('led-1206', [-11.5, 9.5], rotate=90)
pcb.components.LED10 = pcb.createComponent('led-1206', [-5, 9.5], rotate=90)
pcb.components.timer = pcb.createComponent('555-SOIC8', [5,  9])

# PCBmodE Board Config

pcb.addDocumentaion('board_details',  [-12.039821, -30.831399],   "Board details: ...")
pcb.addDocumentaion('manufacturing',  [-12.243017, -18.347399],  "Manufacturing:...")
pcb.addDocumentaion('pcbmode',  [-12.243017, -18.347399],  "Designed with PCBmodE:...", font_size = "1.2mm", line_height = "1.2mm")

pcb.drill_index.location = [-27.971101, -47.126399]

pcb.outline.shape.height = 22
pcb.outline.shape.width = 51
pcb.outline.shape.radii = dict(bl=3, br=3, tl=3, tr=3)
pcb.outline.shape.type = "path"
pcb.outline.shape.value=pcb.parseShapeSVG('outline.svg')

# Routing

pcb.addRoute([Line(3+0j, 3-1j), Line(3+0j, 3.5+0j)])
pcb.addRoute([CubicBezier(1+1j, 2+2j, 4+2j, 5+1j)], layer='top')
pcb.addVia([1.5, 2])
pcb.addVia([4.5, 2])

pcb.save()
