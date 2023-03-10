import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import time
import constants as c
from world import WORLD
from robot import ROBOT

class SIMULATION:
    def __init__(self, directOrGUI):
        if directOrGUI == "GUI":
            self.physicsClient = p.connect(p.GUI)
        else:
            self.physicsClient = p.connect(p.DIRECT)

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
            self.robot.Think(i)
            self.robot.Act(i)
            time.sleep(1/1000)
    
    def Get_Fitness(self):
        self.robot.Get_Fitness()