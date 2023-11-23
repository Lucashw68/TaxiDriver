# Taxi Driver

The Taxi Problem from “Hierarchical Reinforcement Learning with the MAXQ Value Function Decomposition” by Tom Dietterich

## Description
There are four designated locations in the grid world indicated by R(ed), G(reen), Y(ellow), and B(lue). When the episode starts, the taxi starts off at a random square and the passenger is at a random location. The taxi drives to the passenger’s location, picks up the passenger, drives to the passenger’s destination (another one of the four specified locations), and then drops off the passenger. Once the passenger is dropped off, the episode ends.

```
+---------+
|R: | : :G|
| : | : : |
| : : : : |
| | : | : |
|Y| : |B: |
+---------+
```
## Actions
There are 6 discrete deterministic actions:

- 0: move south
- 1: move north
- 2: move east
- 3: move west
- 4: pickup passenger
- 5: drop off passenger

## Rewards

- -1 per step unless other reward is triggered.
- +20 delivering passenger.
- -10 executing “pickup” and “drop-off” actions illegally.

## How to run

This solution is composed by a Python program that runs the environment and a web application that allow visualization and controls over the environment.
The 2 communicate via Websockets.

---
### The Python program can be launched in 2 differents modes:
  - Local: python3 ./taxy_driver.py local [Mode] [Algorithm]
  - Server: python3 ./taxi.py server

### The web interface (Nuxt.js)
  - npm run dev || npm run generate && npm run start

![Screenshot from 2022-05-13 14-03-15](https://github.com/Lucashw68/TaxiDriver/assets/37588846/1e7fe0f9-70f8-4eb1-a7a3-aebbd88f39ac)


## Algorithms implemented

- Random
- Genetic
- Montecarlo
- Pathfinding
- Qlearning
