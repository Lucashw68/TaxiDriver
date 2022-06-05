import  requests
import  cli.src.exceptions as exceptions

################################################################################
# UTILS
################################################################################

def print_help():
    print("USAGE\n\t./taxi_driver [mode]\n\nDESCRIPTION\tmode mode "
        "of the simulation (server, local)")

def print_error(msg):
    print(msg)

def display_graph(graph):
    for v in graph:
        for w in v.get_connections():
            vid = v.get_id()
            wid = w.get_id()
            print('(%s|%s|%d)' % (vid, wid, v.get_weight(w)))

def open_file(path):
    try:
        file = open(path)
        return file.readlines()
    except:
        raise exceptions.OpenFile

def check_connection():
    try:
        requests.get("http://google.com", timeout=5)
    except (requests.ConnectionError, requests.Timeout) as exception:
        print("No internet connection")
        return False
    return True

class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
