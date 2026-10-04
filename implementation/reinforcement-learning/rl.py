import numpy as np
import random

states = ['low_load', 'high_load']  # Example states: low and high load
actions = ['scale_up', 'scale_down']  # Actions: scale up or down
reward_matrix = {'low_load': {'scale_up': -1, 'scale_down': 1},
                 'high_load': {'scale_up': 1, 'scale_down': -1}}

q_table = np.zeros((len(states), len(actions)))

# Parameters
learning_rate = 0.1
discount_factor = 0.9
epsilon = 0.1  # Exploration vs Exploitation

# Q-learning algorithm
def choose_action(state_index):
    if random.uniform(0, 1) < epsilon:
        return random.choice(range(len(actions)))  # Explore
    else:
        return np.argmax(q_table[state_index])  # Exploit

def update_q_value(state_index, action_index, reward, next_state_index):
    q_table[state_index, action_index] = q_table[state_index, action_index] + learning_rate * (reward + discount_factor * np.max(q_table[next_state_index]) - q_table[state_index, action_index])

# Training loop
for episode in range(1000):  # Number of episodes (iterations)
    state_index = random.choice([0, 1])  # Random initial state (low or high load)
    
    action_index = choose_action(state_index)
    next_state_index = random.choice([0, 1])  # Simulating transition to next state
    
    reward = reward_matrix[states[state_index]][actions[action_index]]  # Reward based on state and action
    update_q_value(state_index, action_index, reward, next_state_index)
    
    if episode % 100 == 0:
        print(f"Episode {episode}: Q-table = {q_table}")

print("Final Q-table:", q_table)
