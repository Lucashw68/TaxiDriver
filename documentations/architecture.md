---
title: Architecture of the project
description: 'The full architecture of the various layers in the application'
---

# 1. Python program

The entrypoint is: taxi_driver.py

This program can be launched in 2 differents modes:
  - Local: python3 ./taxi_driver.py local [Mode] [Algorithm]
  - Server: python3 ./taxi_driver.py server

# 2. Web application

The web app is an client interface for the Taxi Driver python program.
It allows to have a view on the simulation and to control the execution of differents algorithms step-by-step.
It is also useful to view and compare the results of the differents algorithms implemented in accordance with the seed.
