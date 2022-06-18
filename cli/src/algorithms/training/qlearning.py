import gym
import numpy as np
import random
import time
import matplotlib.pyplot as plt

env = gym.make('Taxi-v3')

qtable = np.zeros([env.observation_space.n, env.action_space.n])
env.reset()

# params :
epochs = 100001
gamma = 0.1
epsilon = 0.08
decay = 0.1
alfa = 0.8

for ep in range(1, epochs):
	done = False
	state = env.reset()

	errors = 0

	while not done:
		if random.uniform(0, 1) < epsilon:
			action = env.action_space.sample()
		else:
			action = np.argmax(qtable[state])

		nstate, r, done, info = env.step(action) 
		
		print(env.render(mode='ansi'))
		input()

		if r <= -10:
			errors += 1

		qtable[state, action] = (1 - alfa) * qtable[state, action] + alfa * (r + gamma * max(qtable[nstate]))
		state = nstate

	print(f'''| EPOCH n°: {ep} / {epochs} Errors: {errors}''')

with open('qtable.npy', 'wb') as f:
    np.save(f, qtable)

state = env.reset()
epochs, penalties, reward = 0, 0, 0
q_table = qtable
done = False

plt.ion()

while not done:
    print(env.render(mode='ansi'))

    action = np.argmax(q_table[state])
    state, reward, done, info = env.step(action)
