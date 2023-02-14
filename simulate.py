import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
import math
import constants as c
import random

PI = math.pi

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
p.loadSDF("world.sdf")
robotId = p.loadURDF("body.urdf")
pyrosim.Prepare_To_Simulate(robotId)

backLegSensorValues = np.zeros(c.steps)
frontLegSensorValues = np.zeros(c.steps)

radianValues = np.linspace(0, 2*np.pi, num= c.steps)
targetAngles = (np.pi/4)*np.sin(radianValues)

backLegTargetAngles = np.zeros(c.steps)
backLegRadianValues = np.linspace(0, 2*np.pi, num= c.steps)
for i in range(c.steps):
    backLegTargetAngles[i] = c.backAmplitude*np.sin(c.backFrequency*backLegRadianValues[i] + c.backPhaseOffset)

frontLegTargetAngles = np.zeros(c.steps)
frontLegRadianValues = np.linspace(0, 2*np.pi, num= c.steps)
for i in range(c.steps):
    frontLegTargetAngles[i] = c.frontAmplitude*np.sin(c.frontFrequency*frontLegRadianValues[i] + c.frontPhaseOffset)

#np.save("data/backTargetAngleValues.npy", backLegTargetAngles)
#np.save("data/frontTargetAngleValues.npy", frontLegTargetAngles)
#exit()

for i in range(c.steps):
    p.stepSimulation()
    time.sleep(1/60)
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, 
                                jointName = "Torso_BackLeg", 
                                controlMode = p.POSITION_CONTROL, 
                                targetPosition = backLegTargetAngles[i], 
                                maxForce = 40)
    
    pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, 
                                jointName = "Torso_FrontLeg", 
                                controlMode = p.POSITION_CONTROL, 
                                targetPosition = frontLegTargetAngles[i], 
                                maxForce = 40)

#print(backLegSensorValues)
#print(frontLegSensorValues)

#np.save("data/backLegSensorValues.npy", backLegSensorValues)
#np.save("data/frontLegSensorValues.npy", frontLegSensorValues)


p.disconnect()