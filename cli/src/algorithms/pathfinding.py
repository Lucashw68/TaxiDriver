import cli.src.gym as gym
from cli.src.algorithm import Algorithm

class Pathfinding(Algorithm):
    def step(self, env):
        return env.step(env.action_space.sample())
