import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
p.loadSDF("world.sdf")
robotId = p.loadURDF("body.urdf")
pyrosim.Prepare_To_Simulate(robotId)

backLegSensorValues = np.zeros(1000)
#backLegSensorValues = []
frontLegSensorValues = np.zeros(1000)
#frontLegSensorValues = []

for i in range(1000):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    #backLegSensorValues.append(pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg"))
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    #frontLegSensorValues.append(pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg"))
    time.sleep(1/60)
    
#print(backLegSensorValues)
#print(frontLegSensorValues)

np.save("data/backLegSensorValues.npy", backLegSensorValues)
np.save("data/frontLegSensorValues.npy", frontLegSensorValues)


p.disconnect()