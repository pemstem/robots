import numpy as np

class SOLUTION:
    def __init__(self):
        self.weights = np.random.rand(3,2)
        result = self.weights * 2 - 1