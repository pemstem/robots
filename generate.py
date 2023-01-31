import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")
length = 1
width = 1
height = 1
x = 0
y = 0
z = 0.5
x2 = 0
y2 = 1
z2 = 1.5
#pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length,width,height])
#pyrosim.Send_Cube(name="Box2", pos=[x2,y2,z2] , size=[length,width,height])
#pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length,width,height])
# pyrosim.Send_Cube(name="Box2", pos=[x2,y2,z2] , size=[length,width,height])

# Modify the position of each 1x1x1 block so that it starts sitting directly on the one below it
#for i in range (0,10):
    #pyrosim.Send_Cube(name="Box"+str(i), pos=[x,y,z] , size=[length,width,height])
    #z = z + 1

# modify the blocks' sizes so that each block has 90% the width, height, and length of the block below it
for i in range (5):    
    for j in range (5):
        for k in range (10):
            pyrosim.Send_Cube(name="Box"+str(k), pos=[x,y,z] , size=[length,width,height])
            z = z + 1
            length = length * 0.9
            width = width * 0.9
            height = height * 0.9
        y = y + 1
        length = 1
        width = 1
        height = 1
        z = 0.5
    x = x + 1
    y = 0
    length = 1
    width = 1
    height = 1
    z = 0.5
pyrosim.End()