import numpy as np
import random

# Possible states (simplified): Low load, Medium load, High load
states = ["low", "medium", "high"]
actions = ["increase_threshold", "decrease_threshold", "maintain"]

# Q-table for learning optimal decisions
q_table = np.zeros((len(states), len(actions)))

# Parameters
learning_rate = 0.1
discount_factor = 0.9
epsilon = 0.1  # Exploration probability

# Reward function for different states and actions
reward_matrix = {
    "low": {"increase_threshold": 1, "decrease_threshold": -1, "maintain": 0},
    "medium": {"increase_threshold": 1, "decrease_threshold": -1, "maintain": 1},
    "high": {"increase_threshold": -1, "decrease_threshold": 1, "maintain": 0}
}

def choose_action(state_index):
    if random.uniform(0, 1) < epsilon:
        return random.choice(range(len(actions)))  # Explore
    else:
        return np.argmax(q_table[state_index])  # Exploit

def update_q_value(state_index, action_index, reward, next_state_index):
    q_table[state_index, action_index] += learning_rate * (
        reward + discount_factor * np.max(q_table[next_state_index]) - q_table[state_index, action_index]
    )

# Training loop
for episode in range(1000):
    state_index = random.choice([0, 1, 2])  # Randomly choose initial state (low, medium, high)
    
    action_index = choose_action(state_index)
    next_state_index = random.choice([0, 1, 2])  # Simulate next state

    reward = reward_matrix[states[state_index]][actions[action_index]]
    update_q_value(state_index, action_index, reward, next_state_index)

    if episode % 100 == 0:
        print(f"Episode {episode}: Q-table = {q_table}")

print("Final Q-table:", q_table)
