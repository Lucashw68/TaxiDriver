#!/bin/bash

# ==============================================================================
# Install TaiDriver required modules
# ==============================================================================

# Check if python is installed
command -v python3 >/dev/null 2>&1 && echo Python 3 is installed

# virtual env
python -m venv ../.env
source ../.env/bin/activate

# install server utility
pip install python-socketio
pip install eventlet

# install signal utility
pip install readchar

# install gym
pip install gym
