import os
from os.path import join
import FreeCAD


user_path = os.path.expanduser("~")
bimtester_prefs = FreeCAD.ParamGet(
    "User parameter:BaseApp/Preferences/Mod/BIMTester/Defaults"
)


# TODO on first WB startup if pref do not exist
# close task panel and restart task panel to get the initial paths


def get_bimtester_code_path():

    from code_bimtester.bimtester import package_path
    return join(package_path, "..")


def get_default_args():

    args = {
        "action": "",
        "advanced_arguments": "",
        "console": False,  # has to be False to get a report file
        "feature": "",
        "ifc": "",
        "path": "",
        "report": "",
        "steps": "",
        "schema_file": "",
        "schema_name": "",
        "lang": "",
    }
    # print(args)

    return args


def get_default_featurefile():

    stdfeaturefile = os.path.join(
        get_bimtester_code_path(),
        "examples",
        "01_ifcschema_translated",
        "features",
        "de_grundlagen.feature"
    )
    if not os.path.isfile(stdfeaturefile):
        stdfeaturefile = user_path

    featurefile = bimtester_prefs.GetString("FeatureFile", "")
    if featurefile == "":
        FreeCAD.ParamGet(
            "User parameter:BaseApp/Preferences/Mod/BIMTester/Defaults"
        ).SetString("FeatureFile", stdfeaturefile)
    # print(featurefile)

    return featurefile


def get_default_ifcfile():

    stdifcfile = os.path.join(
        get_bimtester_code_path(),
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
