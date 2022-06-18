from cli.src.algorithm import Algorithm
import numpy as np
import random
from IPython.display import clear_output

class Montecarlo(Algorithm):
    def __init__(self, name):
        super().__init__(name)
        self.qtable = np.load('./cli/src/algorithms/qtable_montecarlo.npy')

    def step(self, env):
        action = np.argmax(self.qtable[env.s])
        return env.step(action)
