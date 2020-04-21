import numpy as np
import os
import pickle
import collections
import random
import pylab as plt


class Qlearning:

    def __init__(self, alpha=0.5, gamma=0.9, epsilon=0.1, initial_q={}, agent_key='O', oponent_key='X', blank_key='-'):
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.Q = initial_q
        self.agent_key = agent_key
        self.oponent_key = oponent_key
        self.blank_key = blank_key

    def get_action(self, state):
        if state in self.Q:
            actions = self.Q[state]
            max_action = np.max(actions)
            if max_action > 0:  # verifier que c'est bonne action
                index = np.where(actions == max_action)[0][0]
                return int(index / 3), int(index % 3)  # 1D a 2D [0,1,2,3,4...] -> [(0,0), (0,1), (0,2), (1,0), (1,1)...]
        # SINON on va choisir une action aleatoirement
        actions = [i for i, letter in enumerate(state) if letter == self.blank_key]
        index = random.choice(actions)
        return int(index / 3), int(index % 3)

    def update(self, prev_state, new_state, prev_action, new_action, reward):
        if prev_state not in self.Q:
            actions = np.zeros(9)
            self.Q[prev_state] = actions

        actions = self.Q[prev_state]
        index = prev_action[0] * 3 + prev_action[1] # passage de 2D a 1D
        old_q = actions[index]
        new_q = old_q + self.alpha * (reward + self.gamma * np.max(actions) - old_q)  # formule de Bellman
        self.Q[prev_state][index] = new_q
