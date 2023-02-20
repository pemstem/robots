import constants as c
import numpy as np
import pyrosim.pyrosim as pyrosim
import pybullet as p

class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        self.values = np.zeros(c.steps)
    
    # HELP
    def Prepare_To_Act(self):
        self.amplitude = np.pi/3
        self.frequency =  8
        self.offset = 0

        backLegTargetAngles = np.zeros(c.steps)
        backLegRadianValues = np.linspace(0, 2*np.pi, num= c.steps)    
        for i in range(c.steps):
            backLegTargetAngles[i] = self.amplitude*np.sin(self.frequency*backLegRadianValues[i] + self.offset)

        frontLegTargetAngles = np.zeros(c.steps)
        frontLegRadianValues = np.linspace(0, 2*np.pi, num= c.steps)
        for i in range(c.steps):
            frontLegTargetAngles[i] = self.amplitude*np.sin(self.frequency*frontLegRadianValues[i] + self.offset)

    def Set_Value(self, robot, time):
        self.robot= robot
        pyrosim.Set_Motor_For_Joint(robot, 
                                    self.jointName, 
                                    controlMode = p.POSITION_CONTROL, 
                                    targetPosition = backLegTargetAngles[i], 
                                    maxForce = 40)