import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import time
import constants as c
from world import WORLD
from robot import ROBOT

class SIMULATION:
    def __init__(self):
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8)
        self.world = WORLD()
        self.robot = ROBOT()
    
    def __del__(self):
        p.disconnect()

    def Run(self):
        for i in range(c.steps):
            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Act(i)
            time.sleep(1/1000)
            '''
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
            '''