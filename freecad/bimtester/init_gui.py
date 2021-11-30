# import importlib
import os

# import FreeCAD
import FreeCADGui as Gui


try:
    from code_bimtester.bimtester import package_path
    icon_path = os.path.join(package_path, "resources", "icons", "bimtester.ico")
except:
    icon_path = ""
    print("BIMTester source code is missing.")


wbname = "BIMTester"


class BIMTester(Gui.Workbench):
    """
    Class which gets initiated at startup of the FreeCAD GUI.
    """

    if icon_path != "":
        Icon = icon_path
    MenuText = wbname
    ToolTip = "ToolTip for {}".format(wbname)

    def Initialize(self):
        """
        Called when the workbench is first activated.
        """
        tool_count = 1
        tool_specifier_list = []
        for i in range(tool_count):
            tool_specifier_list.append("{}_{}".format(wbname, i+1))
        self.appendToolbar(wbname, tool_specifier_list)
        self.appendMenu(wbname, tool_specifier_list)

        # start bimtester panel
        from freecad.bimtester import task_panel
        task_panel.show_panel()

    def GetClassName(self):
        return "Gui::PythonWorkbench"


Gui.addWorkbench(BIMTester())


class TOOL1():

    def Activated(self):
        from freecad.bimtester import task_panel
        task_panel.show_panel()

    def GetResources(self):
        return {
            "Pixmap": icon_path,
            "MenuText": "BIMTester GUI",
            "ToolTip": "Start BIMTester task panel"
        }


Gui.addCommand("{}_1".format(wbname), TOOL1())
