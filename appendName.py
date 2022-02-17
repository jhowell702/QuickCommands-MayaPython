# Import the Maya commands library
from maya import cmds

appendString = 'null'

def showWindow():
    append_window = cmds.window( title="Name Append Tool", iconName='NAT', widthHeight=(275, 150) )

    # As we add contents to the window, align them vertically
    cmds.columnLayout( adjustableColumn=True )

    cmds.rowLayout(numberOfColumns=2)

    cmds.text( 'Append String: ' )
    appendField = cmds.textField()
    cmds.textField( appendField, edit=True, aie=True, cc=lambda x: set_append_string(appendField) )

    cmds.setParent('..')


    cmds.rowLayout(numberOfColumns=2)


    cmds.button( label='Append String to Hierarchy', command=append_string )

    cmds.button( label='Close', command=('cmds.deleteUI(\"' + append_window + '\", window=True)') )

    cmds.setParent( '..' )

    cmds.showWindow( append_window )

def set_append_string(*args):
    global appendString
    appendString = cmds.textField(args[0], q=1, text=1)


def append_string(*args):
    children_nodes = cmds.listRelatives(allDescendents=True, s=False)
    cmds.select(children_nodes, add=True )
    nodes = cmds.ls(s=False, sl=True)
    for obj in nodes:
        if 'Shape' in obj:
            pass
        else:
            newName = obj + appendString
            cmds.rename(obj, newName)

    cmds.deleteUI('Name Append Tool')      