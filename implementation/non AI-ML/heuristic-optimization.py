import random

# Defining servers with their current loads
servers = {'A': 0, 'B': 0, 'C': 0}

# Number of tasks to distribute
num_tasks = 1000

# Heuristic function: Assigning task to the server with the least load
for _ in range(num_tasks):
    selected_server = min(servers, key=servers.get)  # Selecting the server with the least load
    servers[selected_server] += 1  # Assigning a task to that server

# Displaying results
total_tasks = sum(servers.values())
for server, count in servers.items():
    percentage = (count / total_tasks) * 100
    print(f"Server {server}: {count} tasks ({percentage:.2f}%)")
