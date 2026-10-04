import numpy as np
import random
import time

# Define states and actions
states = ['low_load', 'high_load']  # Server load levels
actions = ['scale_up', 'scale_down']  # Scaling decisions
reward_matrix = {'low_load': {'scale_up': -1, 'scale_down': 1},
                 'high_load': {'scale_up': 1, 'scale_down': -1}}

q_table = np.zeros((len(states), len(actions)))

# RL Parameters
learning_rate = 0.1
discount_factor = 0.9
epsilon = 0.1  # Exploration vs Exploitation

# Server and task queue initialization
servers = {"Server A": 0, "Server B": 0, "Server C": 0}
task_queue = []

# Generate tasks

def generate_tasks(num_tasks):
    for _ in range(num_tasks):
        task_queue.append(f"Task {_}")

# Choose action based on Q-table or exploration
def choose_action(state_index):
    if random.uniform(0, 1) < epsilon:
        return random.choice(range(len(actions)))  # Explore
    else:
        return np.argmax(q_table[state_index])  # Exploit

# Update Q-value
def update_q_value(state_index, action_index, reward, next_state_index):
    q_table[state_index, action_index] += learning_rate * (
        reward + discount_factor * np.max(q_table[next_state_index]) - q_table[state_index, action_index]
    )

# Distribute tasks with backpressure
def distribute_tasks():
    global servers
    for task in task_queue:
        sorted_servers = sorted(servers.items(), key=lambda x: x[1])
        least_loaded_server = sorted_servers[0][0]
        servers[least_loaded_server] += 1
        print(f"Assigned {task} to {least_loaded_server}")
    task_queue.clear()

# RL + Backpressure Training Loop
for episode in range(1000):  # Simulated episodes
    state_index = random.choice([0, 1])  # Initial state: low or high load
    action_index = choose_action(state_index)
    next_state_index = random.choice([0, 1])
    reward = reward_matrix[states[state_index]][actions[action_index]]
    update_q_value(state_index, action_index, reward, next_state_index)
    
    if episode % 100 == 0:
        print(f"Episode {episode}: Q-table =\n{q_table}")

# Simulate real workload
generate_tasks(1000)  # Generate 1000 incoming tasks
print("\nDistributing tasks using RL-optimized backpressure scheduling...")
distribute_tasks()

# Print final results
print("\nFinal Task Distribution:")
for server, count in servers.items():
    print(f"{server}: {count} tasks")

print("\nFinal Q-Table:")
print(q_table)