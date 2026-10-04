import numpy as np
from sklearn.tree import DecisionTreeClassifier

# Sample data representing resource usage for servers
# Each row is a server with [CPU usage, Memory usage, Disk usage]
server_data = np.array([
    [50, 60, 70],  # Server 0
    [80, 90, 60],  # Server 1
    [30, 40, 50],  # Server 2
    [60, 70, 80],  # Server 3
])

# Sample data representing the resource needs of a function
# Each row represents a function with [CPU requirement, Memory requirement, Disk requirement]
function_data = np.array([
    [55, 65, 75],  # Function 1
    [85, 95, 65],  # Function 2
    [35, 45, 55],  # Function 3
    [65, 75, 85],  # Function 4
])

# Labels indicating which server is best for each function (0 for Server 0, 1 for Server 1, etc.)
labels = np.array([0, 1, 2, 3])  # For simplicity, each function goes to its corresponding server

# Training a Decision Tree Classifier to predict the best server for each function
clf = DecisionTreeClassifier()
clf.fit(server_data, labels)

# Making predictions for new function requests
def dynamic_function_placement(function_requirements):
    predicted_server = clf.predict([function_requirements])
    print(f"The function should be placed on Server {predicted_server[0]}")

# Example usage
new_function = [60, 70, 80]  # A new function's resource requirements
dynamic_function_placement(new_function)
