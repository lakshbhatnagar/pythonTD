# importing module
import hou

# storing selected node
for sel in hou.selectedNodes():
    pass

# extracting name from selected node
name = str(sel)
    
# parent node 
parent = sel.parent()

# extracting path
path = parent.path()

# creating merge node
mergeNode = hou.node(str(path)).createNode("object_merge")

# setName 
mergeNode.setName("PIPE_" + name)

# selected node path
selPath = sel.path()

# set path in merge node
mergeNode.parm("objpath1").set(str(selPath))

# set Color
colorA = hou.Color((1.0, 0.2, 0.1))
colorB = hou.Color((0.0, 1.0, 0.2))
sel.setColor(colorA)
mergeNode.setColor(colorB)
