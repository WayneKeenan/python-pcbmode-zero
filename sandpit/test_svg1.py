from svgpathtools import Path, Line, QuadraticBezier, CubicBezier, Arc, svg2paths, parse_path, wsvg
from pcbmode.utils.svg import absolute_to_relative_path

print("Build SVG Path from lines")


seg1 = CubicBezier(300+100j, 100+100j, 200+200j, 200+300j) # A cubic beginning at (300, 100) and ending at (200, 300)
seg2 = Line(200+300j, 250+350j) # A line beginning at (200, 300) and ending at (250, 350)
path = Path(seg1, seg2) # A path traversing the cubic and then the line

# (svgpathtools only creates absolute path co-ordinates)

print(path.d())



print("Create SVG")
#(svgpathtools only creates absolute path co-ordinates)

outline_path = parse_path("m 10.858333,11 c 2.140681,-0.340482 4.281363,-0.680964 6.422044,-1.0214454 1.69236,-1.0123173 3.384721,-2.0246345 5.077081,-3.0369518 1.2656,-2.1059322 2.531201,-4.2118644 3.796801,-6.31779663 0.663858,-2.34543537 1.327716,-4.69087077 1.991574,-7.03630647 -0.223524,-1.829043 -0.447047,-3.6580857 -0.670571,-5.4871287 -0.600087,-0.758457 -1.200175,-1.516914 -1.800262,-2.275371 -17.1166667,0 -34.2333333,0 -51.35,0 -0.600087,0.758457 -1.200175,1.516914 -1.800262,2.275371 -0.223524,1.829043 -0.447047,3.6580857 -0.670571,5.4871287 0.663858,2.3454357 1.327716,4.6908711 1.991574,7.03630647 1.2656,2.10593223 2.531201,4.21186443 3.796801,6.31779663 1.69236,1.0123173 3.384721,2.0246345 5.077081,3.0369518 2.140681,0.3404814 4.281363,0.6809634 6.422044,1.0214454 7.2388887,0 14.4777773,0 21.716666,0 z", current_pos=0)
wsvg(outline_path, filename='svg/out/output1.svg')

p = parse_path("m 4.6147194,11.014797 c 0.04717,0.459725 -0.00339,0.582458 0.024033,1.056225", current_pos=0)

print p

print("Parse SVG")
paths, attributes = svg2paths('svg/in/triangle_relative.svg')

for path in paths:
    print absolute_to_relative_path(path.d())
