import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
import math
import random

PI = math.pi

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
p.loadSDF("world.sdf")
robotId = p.loadURDF("body.urdf")
pyrosim.Prepare_To_Simulate(robotId)

backLegSensorValues = np.zeros(1000)
frontLegSensorValues = np.zeros(1000)

radianValues = np.linspace(0, 2*np.pi, num= 1000)
targetAngles = (np.pi/4)*np.sin(radianValues)

#np.save("data/targetAngles.npy", targetAngles)

for i in range(0,1000):
    p.stepSimulation()
    time.sleep(1/60)
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, 
                                jointName = "Torso_BackLeg", 
                                controlMode = p.POSITION_CONTROL, 
                                targetPosition = targetAngles[i], 
                                maxForce = 40)
    
    pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, 
                                jointName = "Torso_FrontLeg", 
                                controlMode = p.POSITION_CONTROL, 
                                targetPosition = targetAngles[i], 
                                maxForce = 40)

print(backLegSensorValues)
print(frontLegSensorValues)

np.save("data/backLegSensorValues.npy", backLegSensorValues)
np.save("data/frontLegSensorValues.npy", frontLegSensorValues)


p.disconnect()