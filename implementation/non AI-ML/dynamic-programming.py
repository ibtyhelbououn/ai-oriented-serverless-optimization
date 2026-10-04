import numpy as np

# Number of servers
servers = 3
# Number of tasks
tasks = [i for i in range(1, 1001)]  # Simulating 1000 tasks

# DP Table Initialization
dp = np.zeros((len(tasks) + 1, servers))

# Assigning tasks dynamically
task_distribution = [[] for _ in range(servers)]
server_loads = [0] * servers

for task in tasks:
    min_server = server_loads.index(min(server_loads))  # Finding the least loaded server
    task_distribution[min_server].append(task)  # Assigning the task to the least loaded server
    server_loads[min_server] += 1  # Update server load

# Displaying the results
print("Task Distribution Among Servers:")
for i, tasks in enumerate(task_distribution):
    print(f"Server {chr(65 + i)}: {len(tasks)} tasks ({len(tasks) / len(tasks) * 100:.2f}%)")
