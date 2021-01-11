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

import os

import FreeCAD


user_path = os.path.expanduser("~")
bimtester_prefs = FreeCAD.ParamGet(
    "User parameter:BaseApp/Preferences/Mod/BIMTester/Defaults"
)


# TODO on first WB startup if pref do not exist
# close task panel and restart task panel to get the initial paths


def get_default_featuresdir():

    featuresdir = bimtester_prefs.GetString("FeaturesDirectory", "")
    if featuresdir == "":
        FreeCAD.ParamGet(
            "User parameter:BaseApp/Preferences/Mod/BIMTester/Defaults"
        ).SetString("FeaturesDirectory", user_path)
    # print(featuresdir)

    return featuresdir


def get_default_ifcfile():

    from code_bimtester.bimtester import package_path
    stdifcfile = os.path.join(
        package_path,
        "..",
        "examples",
        "01_ifcschema_translated",
        "IFC2X3_col.ifc"
    )
    if not os.path.isfile(stdifcfile):
        stdifcfile = user_path

    ifcfile = bimtester_prefs.GetString("IFCFile", "")
    if ifcfile == "":
        FreeCAD.ParamGet(
            "User parameter:BaseApp/Preferences/Mod/BIMTester/Defaults"
        ).SetString("IFCFile", stdifcfile)
    # print(ifcfile)

    return ifcfile
