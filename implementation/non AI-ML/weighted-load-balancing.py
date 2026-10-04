import numpy as np

# Defining servers with their corresponding weights
servers = ["Server A", "Server B", "Server C"]
weights = [5, 3, 2]  # Higher weight means higher processing capacity

# Normalizing weights to get selection probabilities
probabilities = np.array(weights) / sum(weights)

# Function to assign tasks to servers based on weighted probability
def assign_task():
    return np.random.choice(servers, p=probabilities)

# Simulating multiple task allocations
task_count = 1000
allocation_results = {server: 0 for server in servers}

for _ in range(task_count):
    selected_server = assign_task()
    allocation_results[selected_server] += 1

# Displaying results
print("Task Distribution Among Servers:")
for server, count in allocation_results.items():
    print(f"{server}: {count} tasks ({(count/task_count)*100:.2f}%)")
