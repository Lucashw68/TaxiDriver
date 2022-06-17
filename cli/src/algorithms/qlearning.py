import cli.src.gym as gym
from cli.src.algorithm import Algorithm
import numpy as np

class Qlearning(Algorithm):
    def __init__(self, name):
        super().__init__(name)
        
        self.qtable = np.load('./cli/src/algorithms/qtable.npy')

    def step(self, env):
        action = np.argmax(self.qtable[env.s])
        
        return env.step(action)