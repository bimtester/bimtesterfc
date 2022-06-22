# BIMTester for FreeCAD
### Screen shot
![BIMTester screen](screen.png "BIMTester in action")


### Installation and run
+ Install BIMTester for FreeCAD via FreeCAD AddOn manager from menu *Edit*
+ BIMTester code from IfcOpenShell repository is included
+ Install missing python dependencies
    + they need to be accessable from within the FreeCAD python console
    + behave (at least 1.2.6)
    + pystache
    + on Windows this may help: https://forum.freecadweb.org/viewtopic.php?f=4&t=49295
    + ifcopenshell (on FreeCAD for Windows this may included already)
+ start FreeCAD, switch to BIMTester
+ start the BIMTester task panel GUI with click on the tool available
+ On the very first start of BIMTester once close the task panel and restart
+ this will initialise the standard example files
+ it is set to the BIMTester included IFC2x3 example and the German feature file
+ click on run
+ :-)

### Running CLI without FreeCad or BlenderBIM

+ Clone the repository
+ Create new python environment (e.g., Conda or venv)
+ Run `pip install -r requirements.txt` in console. 
  Make sure your console is set to the correct path (e.g., `path/to/bimtesterfc` folder)
+ Run CLI tool (e.g.,  ` python .\code_bimtester\cli.py -i .\code_bimtester\examples\01_ifcschema_translated\IFC2X3_col.ifc -f .\code_bimtester\examples\01_ifcschema_translated\features\de_grundlagen.feature -c`)

