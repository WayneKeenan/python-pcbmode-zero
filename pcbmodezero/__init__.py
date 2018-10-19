from pprint import pformat
from os import chdir
from os.path import join
import sys

import jsontree
from svgpathtools import svg2paths

from pcbmode import pcbmode
from pcbmode.utils.svg import absolute_to_relative_path



class PCBmodEZero:

    def __init__(self, boards_dir, board_name):
        self.boards_root_dir = join(boards_dir, '..')
        self.board_name = board_name
        self.board_json_filepath = "{}/boards/{}/{}.json".format(self.boards_root_dir, self.board_name, self.board_name)
        self.board_shape_dirpath = "{}/boards/{}/shapes".format(self.boards_root_dir, self.board_name)
        self.board_components_dirpath = "{}/boards/{}/components".format(self.boards_root_dir, self.board_name)
        self.configItem = jsontree.mapped_jsontree_class(self.underscore2minus)

        self.components= self.configItem()
        self.config = self.configItem()
        self.distances = self.configItem()
        self.documentation = self.configItem()
        self.layer_control = self.configItem()
        self.gerber = self.configItem()
        self.files = self.configItem()
        self.drills = self.configItem()
        self.drill_index = self.configItem()
        self.outline = self.configItem()
        self.shapes = self.configItem()
        self.soldermask = self.configItem()
        self.solderpaste = self.configItem()
        self.stackup = self.configItem()
        self.vias = self.configItem()

        self.defaults = self.configItem()
        self.defaults.documentaion = self.configItem()
        self.defaults.documentation.font_family = "Overlock-Regular-OTF-webfont"
        self.defaults.documentation.font_size = "1.5mm"
        self.defaults.documentation.letter_spacing = "0mm"
        self.defaults.documentation.line_height = "1.5mm"
        self.defaults.documentation.location = [0, 0]
        self.defaults.documentation.rotate = 0
        self.defaults.documentation.style = "fill"
        self.defaults.documentation.type = "text"
        self.defaults.documentation.value = "Warning: No Text Set"

    def json2py(self, filepath):
        with open(filepath, 'r') as file:
            txt = file.read()
            decoder = jsontree.JSONTreeDecoder()
            decoded = decoder.decode(txt)
            #print(pformat(decoded))
            #print(jsontree.dumps(decoded, indent=4))
            return decoded

    def underscore2minus(self, name):
        if name == '__class__':
            raise ValueError
        return name.replace('_', '-')

    def writeJSON(self, json_obj, filepath):
        json_txt = jsontree.dumps(json_obj, indent=4)
        #print (all_json)

        with open(filepath, 'w') as file:
            file.write(json_txt)


    def clone(self, src):
        return jsontree.clone(src)

    def save(self):
        all = self.configItem()
        all.components = self.clone(self.components)
        all.config = self.clone(self.config)
        all.distances = self.clone(self.distances)
        all.documentation = self.clone(self.documentation)
        all.drill_index = self.clone(self.drill_index)
        all.drills = self.clone(self.drills)
        all.files = self.clone(self.files)
        all.gerber = self.clone(self.gerber)
        all.layer_control = self.clone(self.layer_control)
        all.outline = self.clone(self.outline)
        all.shapes = self.clone(self.shapes)
        all.soldermask = self.clone(self.soldermask)
        all.solderpaste = self.clone(self.solderpaste)
        all.stackup = self.clone(self.stackup)
        all.vias = self.clone(self.vias)

        self.writeJSON(all, self.board_json_filepath)

        chdir(self.boards_root_dir)
        try:
            oldargv = sys.argv
            sys.argv = sys.argv[0::]
            sys.argv.extend(['-b', self.board_name, '-m'])
            #print(sys.argv)
            pcbmode.main()
        finally:
            sys.argv = oldargv


    def readSVG(self, filepath):
        paths, attributes = svg2paths(filepath)

        for path in paths:
            return absolute_to_relative_path(path.d())

    def parseShapeSVG(self, svg_filename):
        return self.readSVG(join(self.board_shape_dirpath, svg_filename))


    def parseComponentSVG(self, svg_filename):
        return self.readSVG(join(self.board_components_dirpath, svg_filename))

    def saveComponent(self, component, component_name):
        return self.writeJSON(component, join(self.board_components_dirpath, component_name + '.json'))
