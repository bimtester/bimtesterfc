from os.path import dirname
from os.path import realpath

import FreeCAD


module_path = dirname(realpath(__file__))


FreeCAD.addImportType(
    "1 run BimTester (*.ifc)",
    "freecad.bimtester.import_ifc"
)
