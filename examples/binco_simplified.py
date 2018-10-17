from pcbmodezero import PCBmodEZero

p = PCBmodEZero(boards_parent_dir='../sandpit', board_name='test_py_1')

# Components

led1 = p.json()
led1.footprint='led-1206'
led1.layer="bottom"
led1.location = [-11.535056, 9.321493]
led1.rotate = 90
led1.show = True
led1.silkscreen.refdef.show = True


# Copy LED and modify it by location
led10 = p.clone(led1)
led10.location = [-3.838085, 9.321493]



# PCBmodE Config

p.components.LED1 = led1
p.components.LED10 = led10


p.config.name='test1'
p.config.no_docs = False
p.config.no_drill_index = False
p.config.no_flashes = False
p.config.no_layer_index = False
p.config.rev = "first"
p.config.style_layout = "default"
p.config.units = "mm"


p.distances.from_pour_to.drill = 0.25
p.distances.from_pour_to.outline = 0.4
p.distances.from_pour_to.pad = 0.25
p.distances.from_pour_to.route = 0.25

p.distances.soldermask.circle_buffer = 0.05
p.distances.soldermask.path_scale = 1.05
p.distances.soldermask.rect_buffer = 0.05

p.distances.solderpaste.circle_buffer = -0.1
p.distances.solderpaste.path_scale = 0.9
p.distances.solderpaste.rect_buffer = -0.1


p.documentation.board_details = p.clone(p.defaults.documentation)
p.documentation.board_details.location = [ -12.039821, -30.831399]
p.documentation.board_details.value = '\n'.join(["Board details:",
                                                 "Name: BINCO",
                                                 "Revision: first",
                                                 "Description: a binary counter",
                                                 "License: MIT",
                                                 "Designer: Saar Drimer, Boldport, saar@boldport.com"])

p.documentation.manufacturing = p.clone(p.defaults.documentation)
p.documentation.manufacturing.location = [ -12.243017, -18.347399 ]
p.documentation.manufacturing.value =  '\n'.join(["Manufacturing:",
                                       "RoHS and lead free compliant manufacturing process",
                                       "Unit of length: Millimetre (mm)",
                                       "Number of layers: 2 ('top', 'bottom')",
                                       "Board thickness: 1.6 mm",
                                       "Material: FR4 35/35 um copper",
                                       "Silkscreen: top, bottom, white",
                                       "Soldermask: top, bottom (green)",
                                       "Surface finish: lead free!"])

p.documentation.pcbmode = p.clone(p.defaults.documentation)
p.documentation.pcbmode.font_size = "1.2mm"
p.documentation.pcbmode.line_height = "1.2mm"
p.documentation.pcbmode.location =  [ -15.849812, -41.294399 ]
p.documentation.pcbmode.value = '\n'.join(["Designed with PCBmodE, an open source software",
                                           "     http://pcbmode.com",
                                           "Stay updated:",
                                           "     @boldport @pcbmode http://boldport.com"])


p.drill_index.location = [-27.971101, -47.126399]


p.drills = {}


p.files.routing_data = "test1_routing.json"
p.files.routing_svg = "test1.svg"


p.gerber.decimals = 6
p.gerber.digits = 6
p.gerber.min_segment_length = 0.05
p.gerber.steps_per_segment = 100


p.layer_control.assembly = dict(hide=False, lock=False, place=True)
p.layer_control.conductor.hide = False
p.layer_control.conductor.lock = False
p.layer_control.conductor.place = True
p.layer_control.conductor.pads = dict(hide=False, lock=False, place=True)
p.layer_control.conductor.pours = dict(hide=False, lock=True, place=True)
p.layer_control.conductor.routing = dict(hide=False, lock=False, place=True)
p.layer_control.dimensions= dict(hide=False, lock=True, place=True)
p.layer_control.documentation = dict(hide=False, lock=False, place=True)
p.layer_control.drills = dict(hide=False, lock=False, place=True)
p.layer_control.origin= dict(hide=False, lock=True, place=False)
p.layer_control.outline = dict(hide=False, lock=True, place=True)
p.layer_control.placement = dict(hide=False, lock=False, place=True)
p.layer_control.silkscreen = dict(hide=False, lock=False, place=True)
p.layer_control.soldermask = dict(hide=False, lock=False, place=True)
p.layer_control.solderpaste = dict(hide=True, lock=True, place=False)


p.outline.shape.height = 220
p.outline.shape.width = 51
p.outline.shape.radii = dict(bl=3, br=3, tl=3, tr=3)
p.outline.shape.type = "path"
p.outline.shape.value=p.parseShapeSVG('outline.svg')


p.shapes = {}


p.soldermask.circle_buffer = 0.05
p.soldermask.path_scale = 1.05
p.soldermask.rect_buffer = 0.05


p.solderpaste.circle_buffer = -0.1
p.solderpaste.path_scale = 0.9
p.solderpaste.rect_buffer = -0.1


p.stackup.name = "two-layer"


p.vias.default_via = "VIA"


p.save()