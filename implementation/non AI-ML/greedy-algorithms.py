# Greedy Load Balancing Algorithm

import random

# Defining servers and initialize their load
servers = {"A": 0, "B": 0, "C": 0}

# Generating a list of tasks (simulating random task loads)
num_tasks = 1000  # Total number of tasks to distribute

for _ in range(num_tasks):
    # Finding the server with the least load
    least_loaded_server = min(servers, key=servers.get)
    
    # Assigning the task to the least loaded server
    servers[least_loaded_server] += 1

# Printing the task distribution results
print("Task Distribution Among Servers:")
for server, count in servers.items():
    print(f"Server {server}: {count} tasks ({(count / num_tasks) * 100:.2f}%)")
