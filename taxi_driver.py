import  sys
import  json
import  socketio
import  eventlet

import cli.src.gym as gym
import cli.src.utils as utils
import cli.src.signal as signal
import cli.src.exceptions as exceptions

################################################################################
# GLOBALS
################################################################################

sio = socketio.Server(cors_allowed_origins='*')
app = socketio.WSGIApp(sio)

################################################################################
# MODES
################################################################################

def local_mode():
    print("Local mode in progress\n")

def server_mode():
    state = gym.init_simulation(None)
    eventlet.wsgi.server(eventlet.listen(('', 8000)), app, log_output=False)

################################################################################
# OPTIONS
################################################################################

def launch_mode(mode):
    modes = { 'local', 'server' }
    args = { 'local': 3, 'server': 2 }
    if mode in modes and args[mode] == len(sys.argv):
        print(f"== {mode.capitalize()} mode ==\n")
        eval(mode+"_mode")(*sys.argv[2:])
        return 0
    else:
        raise exceptions.InvalidParams

################################################################################
# EVENTS
################################################################################

@sio.event
def connect(sid, env):
    print("==== New client ====")
    print(sid, "Connected", end="\n\n")

@sio.event
def disconnect(sid):
    print("==== Client disconnected ====")
    print(sid, "Disconnected", end="\n\n")

@sio.event
def map(sid):
    print("==== Map requested from", sid, "====")
    map = gym.get_map()
    print(map)
    sio.emit('map', map)

@sio.event
def modes(sid):
    print("==== Modes requested from", sid, "====")
    modes = gym.get_modes()
    print(modes)
    sio.emit('modes', modes)

@sio.event
def algorithms(sid):
    print("==== Algorithms requested from", sid, "====")
    algorithms = gym.get_algorithms()
    print(algorithms)
    sio.emit('algorithms', algorithms)

@sio.event
def mode(sid, data):
    print("==== Request set mode [", data, "] from", sid, "====")
    gym.set_mode(data)

@sio.event
def algorithm(sid, data):
    print("==== Request set algorithm [", data, "] from", sid, "====")
    gym.set_algorithm(data)

@sio.event
def seed(sid):
    print("==== Seed requested from", sid, "====")
    sio.emit('seed', gym.get_seed())

@sio.event
def results(sid):
    print("==== Results requested from", sid, "====")
    sio.emit('results', gym.get_results())

@sio.event
def step(sid):
    print("==== Request step from", sid, "====")
    state, reward, done, info = gym.step()
    map = gym.get_map()
    print(map)
    step = {
        "state": state,
        "reward": reward,
        "done": done,
        "info": info
    }
    sio.emit('map', map)
    sio.emit('step', step)

@sio.event
def reset(sid, data):
    print("==== Request reset from", sid, "====")
    print("Seed: ", data)
    gym.reset(data)
    sio.emit('map', gym.get_map())

################################################################################
# MAIN
################################################################################

def main():
    try:
        nb_args = len(sys.argv)
        if (nb_args < 2 and nb_args > 3 or sys.argv[1] == "-h"):
            raise exceptions.InvalidParams
        signal.catch()
        return launch_mode(sys.argv[1])
    except exceptions.InvalidParams:
        print("Invalid mode or parameters")
        utils.print_help()
        return 84
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        return 84

if __name__ == '__main__':
   sys.exit(main())
