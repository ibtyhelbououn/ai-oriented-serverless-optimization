import random
import time

# Simulating an event-driven execution system
class EDXAlgorithm:
    def __init__(self, servers):
        self.servers = servers

    def trigger_event(self, event_type):
        print(f"Event detected: {event_type}")
        selected_server = self.load_balancer()
        self.execute_task(selected_server, event_type)

    def load_balancer(self):
        return random.choice(self.servers)

    def execute_task(self, server, event_type):
        print(f"Executing task for event '{event_type}' on {server}...")
        time.sleep(random.uniform(0.5, 2))  # Simulate execution time
        print(f"Task for event '{event_type}' completed on {server}.")

# List of available servers
servers = ["Server A", "Server B", "Server C"]

# Creating an instance of the EDXAlgorithm
edx = EDXAlgorithm(servers)

# Simulating multiple events
events = ["File Uploaded", "User Login", "API Request", "Database Update"]

for event in events:
    edx.trigger_event(event)
    print("-" * 40)
