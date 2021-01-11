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

# import os

import FreeCAD


if open.__module__ == "io":
    # because we'll redefine open below
    pyopen = open


def open(filename):

    # feature files path
    from .utils_gui import get_default_featuresdir
    featuresdir = get_default_featuresdir()

    if FreeCAD.GuiUp:
        from freecad.bimtester import task_panel
        task_panel.show_panel(featuresdir, filename)
    else:
        from code_bimtester.bimtester.run import run_all
        status = run_all(
            featuresdir,
            filename
        )
