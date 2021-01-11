# BIMTester for FreeCAD
### Screen shot
![BIMTester screen](screen.png "BIMTester in action")


### Installation and run
+ Install BIMTester for FreeCAD via FreeCAD AddOn manager
    + start FreeCAD, use Edit AddOn manager to install
+ Install BIMTester suorce code
    + download this directory https://github.com/IfcOpenShell/IfcOpenShell/tree/v0.6.0/src/ifcbimtester
    + may be use https://downgit.github.io/#/home?url=https:%2F%2Fgithub.com%2FIfcOpenShell%2FIfcOpenShell%2Ftree%2Fv0.6.0%2Fsrc%2Fifcbimtester
    + paste this directory in FreeCAD_User_Mod/bimtester/ and rename it to code_bimtester
+ Install missing dependencies
    + behave (at least 1.2.6)
    + pystache
    + ifcopenshell (on Windows FreeCAD this may included already)
+ start FreeCAD, switch to BIMTester, the Gui will start
+ On the very first start of BIMTester once close the TaskPanelit and restart it to initialise the standard directories
+ the ifc file is set to a very simple included example
+ click on feature files beside ifc
+ the feature files directory will be empty
+ click on run
+ :-)
