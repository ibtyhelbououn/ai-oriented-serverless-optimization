import matplotlib.pyplot as plt
import numpy as np

methods = ['RL Only', 'Backpressure Only', 'Hybrid']
servers = ['Server A', 'Server B', 'Server C']

# Task counts for each server per method
task_data = {
    'RL Only': [0, 0, 0],  # RL doesn’t assign tasks in your implementation
    'Backpressure Only': [334, 333, 333],
    'Hybrid': [334, 333, 333]
}

x = np.arange(len(servers))  # [0, 1, 2]
width = 0.25

fig, ax = plt.subplots(figsize=(8, 5))
ax.bar(x - width, task_data['Backpressure Only'], width, label='Backpressure Only')
ax.bar(x, task_data['Hybrid'], width, label='Hybrid')
ax.bar(x + width, task_data['RL Only'], width, label='RL Only')

ax.set_ylabel('Tasks Assigned')
ax.set_title('Task Distribution Across Servers')
ax.set_xticks(x)
ax.set_xticklabels(servers)
ax.legend()
plt.grid(True, axis='y')
plt.tight_layout()
plt.show()
