import random
import time

# Defining servers with initial loads
servers = {"Server A": 0, "Server B": 0, "Server C": 0}
task_queue = []

# Functioning to add tasks to the queue
def generate_tasks(num_tasks):
    for _ in range(num_tasks):
        task_queue.append(f"Task {_}")

# Functioning to distribute tasks with backpressure handling
def distribute_tasks():
    global servers
    for task in task_queue:
        # Sorting servers by current load
        sorted_servers = sorted(servers.items(), key=lambda x: x[1])
        least_loaded_server = sorted_servers[0][0]

        # Assigning task to the least loaded server
        servers[least_loaded_server] += 1
        print(f"Assigned {task} to {least_loaded_server}")

    # Clearing queue after distribution
    task_queue.clear()

# Simulating task arrivals and processing
generate_tasks(1000)  # Simulating 1000 incoming tasks
distribute_tasks()

# Printing final server load distribution
print("\nFinal Task Distribution:")
for server, count in servers.items():
    print(f"{server}: {count} tasks")
