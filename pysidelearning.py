from PySide2 import QtCore
from PySide2 import QtWidgets

from shiboken2 import wrapInstance

from maya import cmds

import maya.OpenMayaUI as omui

from maya.app.general.mayaMixin import MayaQWidgetDockableMixin

import hierachRename
import appendName

def maya_main_window():
    main_window_ptr = omui.MQtUtil.mainWindow()
    return wrapInstance(int(main_window_ptr), QtWidgets.QWidget)

class TestDialog(MayaQWidgetDockableMixin, QtWidgets.QDialog):
    def __init__(self, parent= maya_main_window()):
        super(TestDialog, self).__init__(parent)
        
        self.setWindowTitle("Quick Command Menu")
        self.setMinimumWidth(200)

        self.create_widgets()
        self.create_layouts()
        self.create_connections()

    def create_widgets(self):
        self.lineedit = QtWidgets.QLineEdit()
        self.button1 = QtWidgets.QPushButton("Select Hierarchy")
        self.renameHierarchy = QtWidgets.QPushButton("Rename Hierarchy")
        self.appendNameButton = QtWidgets.QPushButton("Append Name")
        self.button3 = QtWidgets.QPushButton("Curve Combine")
        self.selectRootControl = QtWidgets.QPushButton("Select Root Control")
        self.button2 = QtWidgets.QPushButton("Close Window")


    def create_layouts(self):
        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.addWidget(self.button1)
        main_layout.addWidget(self.renameHierarchy)
        main_layout.addWidget(self.appendNameButton)
        main_layout.addWidget(self.selectRootControl)
        main_layout.addWidget(self.button3)
        main_layout.addWidget(self.button2)

    def create_connections(self):
        self.button1.clicked.connect(self.select_hierarchy)
        self.button3.clicked.connect(self.quick_nurb_parent)
        self.renameHierarchy.clicked.connect(self.call_module_hierarchyRename)
        self.appendNameButton.clicked.connect(self.call_module_appendName)
        self.button2.clicked.connect(self.delete_dialog)
        self.selectRootControl.clicked.connect(self.select_root_control)

    def select_hierarchy(self):
        children_nodes = cmds.listRelatives(allDescendents=True)
        for node in children_nodes:
            if 'Shape' in node:
                pass
            else:
                cmds.select(node, add=True)
        

    def quick_nurb_parent(self):
        curves = cmds.ls(selection=True)
        if len(curves) != 2:
            print('Please select two nurbs curves')
        else:
            curveShapes = cmds.listRelatives(curves, s=True)
            cmds.select(clear=True)
            cmds.delete(curves[0], constructionHistory=True)
            cmds.delete(curves[1], constructionHistory=True)
            cmds.parent(curveShapes[0],curves[1], r=True, s=True)
            cmds.delete(curves[0])
            cmds.delete(curves[1], constructionHistory=True)

    def call_module_hierarchyRename(self):
        hierachRename.showWindow()

    def call_module_appendName(self):
        appendName.showWindow()

    def select_root_control(self):
        cmds.select('pot_root_control')

    def delete_dialog(self):
        self.close()


def showWindow():

    try:
        test.close()
        test.deleteLater()
    except:
        pass

    test = TestDialog()
    test.show(dockable=True)

