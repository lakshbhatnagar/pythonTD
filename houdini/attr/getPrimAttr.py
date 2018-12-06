# storing current node
node = hou.pwd()

# extracting geometry from node
geo = node.geometry()

# getting all primitives in geometry
ballPrim = geo.prims()

# total number of primitives
totalPrim = len(ballPrim)

# getting color from each pritive
loop = 0
while loop < totalPrim:
    getColor = ballPrim[loop].floatListAttribValue("Cd")
    print "Primitive " + str(loop) + " = " + str(getColor)
    loop += 1
