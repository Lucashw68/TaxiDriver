from collections import deque
import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
import torchvision.transforms as T
import gym
import random
from sklearn.preprocessing import StandardScaler
import numpy as np

scaler = StandardScaler()

#############################################
# DEEP Q NETWORK
#############################################
class Model(nn.Module):
	def __init__(self) -> None:
		super(Model, self).__init__()

		self.l1 = nn.Linear(1, 100)
		self.l2 = nn.Linear(100, 100)
		self.l3 = nn.Linear(100, 100)
		self.l4 = nn.Linear(100, 6)

	def forward(self, state: int):
		entry = torch.tensor(scaler.fit_transform(np.array([[state]]))).type(torch.float32)

		out = F.relu(self.l1(entry))
		out = F.relu(self.l2(out))
		out = F.relu(self.l3(out))
		return self.l4(out)

#############################################
# QNET AND TARGET NET + MEMORY
#############################################

Q = Model()
T = Model()
memory = deque(maxlen=10000)

loss = nn.MSELoss()
optimizer = optim.Adam(Q.parameters(), lr = 0.00001)

#############################################
# ALGORITHM PARAMETERS
#############################################
env = gym.make('Taxi-v3')

# params :
EPOCHS = 100001
GAMMA = 0.89
EPSILON = -1.0
DECAY = 0.01
ALPHA = 0.8
BATCH_SIZE = 32

# The environement max episode is 200 range [0-200]
MAX_PLAY_EPISODE = 50

#############################################
# TRAIN MODEL
#############################################
def train():
	if len(memory) < BATCH_SIZE:
		return 0
	
	batch = random.sample(memory, BATCH_SIZE)
	random.shuffle(batch)

	mean = 0

	for el in batch:
		optimizer.zero_grad()

		q_val = Q(el[0])
		t_val = T(el[4])
		
		q_act = q_val[0][el[1]].item()
		t_act = torch.max(t_val).item()

		target_value = t_val.detach().clone()
		target_value[0][el[1]] += ((ALPHA * el[2]) + (GAMMA * t_act))
			
		l = loss(q_val, target_value)

		mean += l.item()

		l.backward()
		optimizer.step()

	return mean / BATCH_SIZE

#############################################
# PLAY
#############################################
def play():
	state = env.reset()
	actions_played = [0, 0, 0, 0, 0, 0]

	for i in range(MAX_PLAY_EPISODE):
		# print(env.render(mode='ansi'))

		actions = Q(state)
		action = torch.argmax(actions).item()
		actions_played[action] += 1
		state, r, done, info = env.step(action) 

	print(env.render(mode='ansi'))
	print(actions_played)

#############################################
# ALGORITHM
#############################################
for ep in range(1, EPOCHS):
	done = False
	state = env.reset()

	errors = 0
	model_called = 0
	random_called = 0

	model_err = 0
	cnt = 0

	score = 0
	actions_played = [0, 0, 0, 0, 0, 0]

	while not done:
		if random.random() <= EPSILON:
			random_called += 1
			action = random.randint(0, 5)

		else:
			model_called += 1
			actions = Q(state)
			action = torch.argmax(actions).item()

		actions_played[action] += 1

		nstate, r, done, info = env.step(action) 

		if r <= -10:
			errors += 1

		score += r
		memory.append((state, action, (r / 100), done, nstate))
		state = nstate

		model_err = train()
		cnt += 1

	T.load_state_dict(Q.state_dict())

	if ep%5 == 0:
		play()
		EPSILON = EPSILON - DECAY if EPSILON > 0.001 else EPSILON

	print(f'''| EPOCH n°: {ep} / {EPOCHS} SCORE: {score} Errors: {errors} RANDOM: {random_called} MODEL: {model_called} EPSILON: {EPSILON} MODEL_ERROR: {model_err/cnt}\nACTION_PLAYED: {actions_played}''')

