import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
import math
import random

PI = math.pi
frontAmplitude = PI/3
backAmplitude = PI/4
frontFrequency = 8
backFrequency = 10
frontPhaseOffset = 0
backPhaseOffset = 0

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

backLegTargetAngles = np.zeros(1000)
backLegRadianValues = np.linspace(0, 2*np.pi, num= 1000)
for i in range(1000):
    backLegTargetAngles[i] = backAmplitude*np.sin(backFrequency*backLegRadianValues[i] + backPhaseOffset)

frontLegTargetAngles = np.zeros(1000)
frontLegRadianValues = np.linspace(0, 2*np.pi, num= 1000)
for i in range(1000):
    frontLegTargetAngles[i] = frontAmplitude*np.sin(frontFrequency*frontLegRadianValues[i] + frontPhaseOffset)

#np.save("data/backTargetAngleValues.npy", backLegTargetAngles)
#np.save("data/frontTargetAngleValues.npy", frontLegTargetAngles)
#exit()

for i in range(0,1000):
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