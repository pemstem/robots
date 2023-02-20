import constants as c
import numpy as np
import pyrosim.pyrosim as pyrosim

class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        self.values = np.zeros(c.steps)
    
    def Prepare_To_Act(self):
        self.amplitude = np.pi/3
        self.frequency =  8
        self.offset = 0

        '''
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