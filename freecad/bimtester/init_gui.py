# ***************************************************************************
# *   Copyright (c) 2020 Bernd Hahnebach <bernd@bimstatik.org>              *
# *                                                                         *
# *   This program is free software; you can redistribute it and/or modify  *
# *   it under the terms of the GNU Lesser General Public License (LGPL)    *
# *   as published by the Free Software Foundation; either version 2 of     *
# *   the License, or (at your option) any later version.                   *
# *   for detail see the LICENCE text file.                                 *
# *                                                                         *
# *   This program is distributed in the hope that it will be useful,       *
# *   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
# *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
# *   GNU Library General Public License for more details.                  *
# *                                                                         *
# *   You should have received a copy of the GNU Library General Public     *
# *   License along with this program; if not, write to the Free Software   *
# *   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  *
# *   USA                                                                   *
# *                                                                         *
# ***************************************************************************

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
