import pkg_resources

from pcbmode.utils.utils import dictFromJsonFile

from os.path import join, exists, isfile

COMPONENT_JSON_DIR = pkg_resources.resource_filename(__name__, "json")


def findLibraryComponent(name):

    filepath = join(COMPONENT_JSON_DIR, name + ".json")

    if not isfile(filepath):
        raise ValueError("FIle not found: " + filepath)

    return dictFromJsonFile(filepath)
