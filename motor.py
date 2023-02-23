import constants as c
import numpy as np
import pyrosim.pyrosim as pyrosim
import pybullet as p

class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        print(self.jointName)
        self.Prepare_To_Act()
    
    def Prepare_To_Act(self):
        if (self.jointName == "Torso_BackLeg"):
            self.frequency =  c.backFrequency/2
        else:
            self.frequency = c.backFrequency
        
        self.amplitude = c.backAmplitude
        self.offset = c.backPhaseOffset

        self.radianValues = np.linspace(0, 2*np.pi, num= c.steps)    
        self.motorValues = self.amplitude * np.sin(self.frequency * self.radianValues + self.offset)

    def Set_Value(self, robot, desiredAngle):
        pyrosim.Set_Motor_For_Joint(bodyIndex= robot, 
                                    jointName= self.jointName, 
                                    controlMode = p.POSITION_CONTROL, 
                                    targetPosition = desiredAngle, 
                                    maxForce = c.motorMaxForce)
    
    def Save_Value(self):
        targetAnglesData = open("data/" + self.jointName + ".npy", "w")
        np.save(targetAnglesData, self.motorValues)
        targetAnglesData.close()