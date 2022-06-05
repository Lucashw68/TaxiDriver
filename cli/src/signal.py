import signal
import time
import readchar
import cli.src.gym as gym
import cli.src.utils as utils

def catch():
    signal.signal(signal.SIGINT, handler)

def handler(signum, frame):
    msg = utils.colors.WARNING + "\nCtrl-c was pressed. Do you really want to exit? [y/n]: " + utils.colors.ENDC
    print(msg, end="", flush=True)
    res = readchar.readchar()
    if res == 'y':
        print("")
        gym.stop_simulation()
        exit(1)
    else:
        print("", end="\r", flush=True)
        print(" " * len(msg), end="", flush=True)
        print("    ", end="\r", flush=True)
