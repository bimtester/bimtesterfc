import sys
from os.path import join

from PySide import QtCore
from PySide import QtGui

# import FreeCAD
import FreeCADGui

from .utils_gui import get_default_args
from .utils_gui import get_bimtester_code_path
from .utils_gui import get_default_featurefile
from .utils_gui import get_default_ifcfile

sys.path.append(get_bimtester_code_path())  # before all bimtester imports
from code_bimtester.bimtester.guiwidget import GuiWidgetBimTester as TaskPanel


"""
from freecad.bimtester import task_panel as tp
tp.show_panel()

"""


def show_panel(featurefile="", ifcfile=""):

    if featurefile == "":
        featurefile = get_default_featurefile()
    if ifcfile == "":
        ifcfile = get_default_ifcfile()
    # print(featurefile)
    # print(ifcfile)

    args = get_default_args()
    args["feature"] = featurefile
    args["ifc"] = ifcfile

    QtGui.QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
    mw = FreeCADGui.getMainWindow()
    awidget = QtGui.QDockWidget("BIMTesterGui", mw)
    awidget.setWidget(TaskPanel(args))
    mw.addDockWidget(QtCore.Qt.RightDockWidgetArea, awidget)
    QtGui.QApplication.restoreOverrideCursor()
