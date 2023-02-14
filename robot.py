import pybullet as p
import pybullet_data

class ROBOT:
    def __init__(self):
        self.sensors = {}
        self.motors = {}
        self.robotId = p.loadURDF("body.urdf")