# Import the Maya commands library
from maya import cmds

findString = 'null'
replaceString = 'null'

def showWindow():
    hierarch_window = cmds.window( title="Rename Tool", iconName='RT', widthHeight=(275, 150) )

    # As we add contents to the window, align them vertically
    cmds.columnLayout( adjustableColumn=True )

    cmds.rowLayout(numberOfColumns=2)

    cmds.text( 'Find String: ' )
    findField = cmds.textField()
    cmds.textField( findField, edit=True, aie=True, changeCommand=lambda x: setFindString(findField) )

    cmds.setParent('..')


    cmds.rowLayout(numberOfColumns=2)

    cmds.text( 'Replace String: ' )
    replaceField = cmds.textField()

    cmds.textField( replaceField,edit=True, aie=True, changeCommand=lambda x: setReplaceString(replaceField) )

    cmds.setParent('..')

    cmds.button( label='Search and Replace', command=replaceHiearchy )

    cmds.button( label='Close', command=('cmds.deleteUI(\"' + hierarch_window + '\", window=True)') )

    cmds.setParent( '..' )

 

    # Show the window that we created (window)
    cmds.showWindow( hierarch_window )

def setFindString(*args):
    global findString
    findString = cmds.textField(args[0], q=1, text=1)

def setReplaceString(*args):
    global replaceString
    print(args[0])
    replaceString = cmds.textField(args[0], q=1, text=1)

def replaceHiearchy(*args):
    children_nodes = cmds.listRelatives(allDescendents=True)
    cmds.select(children_nodes, add=True)
    nodes = cmds.ls(sl=True, shapes=False)
    for obj in nodes:
        temp = obj
        temp = temp.replace(findString, replaceString)
        cmds.rename(obj, temp)