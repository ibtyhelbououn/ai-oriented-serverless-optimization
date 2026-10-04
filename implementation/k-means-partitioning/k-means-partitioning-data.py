import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Simulated workload data: (execution time, memory usage)
np.random.seed(42)
workloads = np.array([
    (np.random.randint(1, 20), np.random.randint(50, 500)) for _ in range(30)
])

# Apply KMeans clustering (partitioning)
num_clusters = 3
kmeans = KMeans(n_clusters=num_clusters, random_state=42, n_init=10)
kmeans.fit(workloads)
labels = kmeans.labels_

# Scatter plot with clusters
plt.figure(figsize=(8, 6))
for i in range(num_clusters):
    cluster_points = workloads[labels == i]
    plt.scatter(cluster_points[:, 0], cluster_points[:, 1], label=f'Cluster {i+1}')

# Plot cluster centroids
centroids = kmeans.cluster_centers_
plt.scatter(centroids[:, 0], centroids[:, 1], c='black', marker='x', s=200, label='Centroids')

# Labels and styling
plt.xlabel('Execution Time')
plt.ylabel('Memory Usage')
plt.title('Workload Partitioning Using KMeans')
plt.legend()
plt.show()
