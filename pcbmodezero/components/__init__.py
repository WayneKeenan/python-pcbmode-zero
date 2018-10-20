import pkg_resources
from os.path import join, exists, isfile

from pcbmode.utils.utils import dictFromJsonFile


from leds import led_1206
from vias import via

COMPONENT_JSON_DIR = pkg_resources.resource_filename(__name__, "json")

# basic static mapping config for now, dynamic package search maybe later...
# (although Python component construction is more for user side)

py_component_mappings = {
    'via': via,
    'led-1206': led_1206
}

def find_library_component(name):

    if name in py_component_mappings:
        return py_component_mappings[name]

    filepath = join(COMPONENT_JSON_DIR, name + ".json")

    if not isfile(filepath):
        raise ValueError("FIle not found: " + filepath)

    return dictFromJsonFile(filepath)
