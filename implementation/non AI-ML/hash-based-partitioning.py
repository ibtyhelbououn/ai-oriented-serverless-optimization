import hashlib

# Defining servers
servers = {"A": [], "B": [], "C": []}
server_list = list(servers.keys())

# Sampling tasks (can be any unique identifiers)
tasks = [f"Task{i}" for i in range(1, 1001)]  # 1000 tasks

# Hashing function to assign tasks to servers
def assign_task(task_id):
    hash_value = int(hashlib.md5(task_id.encode()).hexdigest(), 16)  # Convert hash to integer
    server_index = hash_value % len(server_list)  # Map to server index
    return server_list[server_index]

# Distributing tasks using hashing
for task in tasks:
    assigned_server = assign_task(task)
    servers[assigned_server].append(task)

# Displaying task distribution
for server, task_list in servers.items():
    print(f"Server {server}: {len(task_list)} tasks ({(len(task_list) / len(tasks)) * 100:.2f}%)")
