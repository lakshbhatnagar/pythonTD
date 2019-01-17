import hou

class pp:
   prim = ""
   def __init__(self, prim, name, radius):
     self.name = name
     self.prim = prim
     self.radius = radius
   def create(self, path):
     hou.node(path).createNode(self.prim)



myNode = pp("sphere", "hello", 1)
myNode.create("/obj/sphere1")
