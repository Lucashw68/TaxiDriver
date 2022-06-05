import json
import os
from datetime import datetime

def check_file(filepath):
    if os.path.exists(filepath) and os.path.getsize(filepath) > 0:
        return True
    else:
        return False

def get_timestamp():
    now = datetime.now()
    return datetime.timestamp(now)

def init_file(filename):
    results = { "results": []}
    with open(filename, 'w') as file:
        json.dump(results, file, indent=4)

def append_to_file(filename, obj):
    with open(filename, '+r', encoding='utf-8') as file:
        file_data = json.load(file)
        obj["id"] = len(file_data["results"])
        file_data["results"].append(obj)
        file.seek(0)
        json.dump(file_data, file, indent=4)

def add(algorithm, mode, seed, steps, reward):
    filename = f'results/{algorithm}/{algorithm}.json'
    result = {
        "id": 0,
        "algorithm": algorithm,
        "seed": seed,
        "mode": mode,
        "steps": steps,
        "reward": reward,
        "timestamp": get_timestamp()
    }
    exists = check_file(filename)
    if not exists:
        init_file(filename)
    append_to_file(filename, result)

def get(algorithm, amount):
    filename = f'results/{algorithm}/{algorithm}.json'
    exists = check_file(filename)
    if not exists:
        init_file(filename)
    with open(filename, 'r', encoding='utf-8') as file:
        jsonData = json.load(file)
        return jsonData

# add('random', 'time', 3456, 345, 20)
# add('genetic', 'time', 2323423, 876, 20)
# add('montecarlo', 'time', 42, 543, 50)
# add('qlearning', 'time', 135, 234, 90)
# add('pathfinding', 'time', 34567, 20100, 10)
