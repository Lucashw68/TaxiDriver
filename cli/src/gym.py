import gym
import numpy as np
import random
import importlib
import cli.src.results as results

import cli.src.algorithms.genetic as Genetic
import cli.src.algorithms.montecarlo as Montecarlo
import cli.src.algorithms.pathfinding as Pathfinding
import cli.src.algorithms.qlearning as Qlearning
import cli.src.algorithms.random as Random

################################################################################
# GLOBALS
################################################################################

env = None
mode = None
algorithm = None
instanceAlgorithm = None
customSeed = None
maxEpisodes = 1000

modes = ["time", "tune"]
algorithms = ["random", "pathfinding", "qlearning", "montecarlo", "genetic"]

################################################################################
# SETTERS
################################################################################

def set_mode(mode):
    globals()['mode'] = mode

def set_algorithm(algorithm):
    globals()['algorithm'] = algorithm
    globals()['instanceAlgorithm'] = instantiateAlgorithm(algorithm)

def set_max_steps():
    env._max_episode_steps = maxEpisodes

################################################################################
# ALGORITHMS
###########################################################################

def instantiateAlgorithm(algorithm):
    module = importlib.import_module(f'cli.src.algorithms.{algorithm}')
    class_ = getattr(module, algorithm.capitalize())
    instanceAlgorithm = class_(algorithm.capitalize())
    return instanceAlgorithm

################################################################################
# GETTERS
################################################################################

def get_map():
    return env.render(mode='ansi')

def get_seed():
    return customSeed

def get_modes():
    return modes

def get_algorithms():
    return algorithms

################################################################################
# RESULTS
################################################################################

def write_result(steps, reward):
    results.add(algorithm, mode, customSeed, steps, reward)

def get_results():
    allResults = { "results": []}
    for algo in algorithms:
        algoResults = results.get(algo, 0)["results"]
        for res in algoResults:
            allResults["results"].append(res)
    return allResults

################################################################################
# GYM
################################################################################

def init_simulation(seed):
    globals()['env'] = gym.make('Taxi-v3')
    if seed != None:
        globals()['customSeed'] = seed
    else:
        globals()['customSeed'] = randomSeed(0, 100000)
    set_algorithm(algorithms[0])
    print("Seed: [", customSeed, "]")
    print("Algorithm: [", algorithm, "]")
    return env.reset(seed=customSeed)

def stop_simulation():
    env.close()

def step():
    return instanceAlgorithm.step(env)

def reset(seed):
    globals()['customSeed'] = seed
    env.reset(seed=customSeed)
    set_max_steps()

def randomSeed(min, max):
    return random.randint(min, max)
