import tensorflow as tf
import numpy as np

# Inputs represent workload, Outputs represent resources
np.random.seed(42)
workloads = np.random.rand(1000, 3)  # e.g., CPU usage, memory usage, network usage
resources = np.random.rand(1000, 1)  # e.g., optimal resource allocation

# Splitting data into training and testing sets
train_workloads = workloads[:800]
train_resources = resources[:800]
test_workloads = workloads[800:]
test_resources = resources[800:]

# Defining a simple neural network
model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(3,)),  # Input layer
    tf.keras.layers.Dense(32, activation='relu'),                   # Hidden layer
    tf.keras.layers.Dense(1)                                       # Output layer
])

# Compile the model
model.compile(optimizer='adam', loss='mse', metrics=['mae'])

# Train the model
history = model.fit(
    train_workloads, train_resources,
    epochs=50, batch_size=32, validation_split=0.2, verbose=1
)

# Evaluate the model
test_loss, test_mae = model.evaluate(test_workloads, test_resources, verbose=0)
print(f"Test MAE: {test_mae}")

# Make predictions
predictions = model.predict(test_workloads)
print(f"Sample Predictions: {predictions[:5]}")
