import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Simulating workload data (task execution times in milliseconds)
workloads = np.array([[100], [200], [300], [150], [250], [350], [400], [450], [500]])

# Choosing number of partitions (clusters)
num_clusters = 3

# Applying K-Means clustering
kmeans = KMeans(n_clusters=num_clusters, random_state=42, n_init=10)
kmeans.fit(workloads)

# Assigning each workload to a cluster
labels = kmeans.labels_

# Visualizing the partitions
plt.scatter(workloads, np.zeros_like(workloads), c=labels, cmap='viridis', marker='o', s=100)
plt.xlabel("Workload Execution Time (ms)")
plt.title("K-Means Partitioning of Workloads")
plt.show()

# Displaying workload groups
for i in range(num_clusters):
    cluster_tasks = workloads[labels == i].flatten()
    print(f"Cluster {i+1}: {cluster_tasks}")
