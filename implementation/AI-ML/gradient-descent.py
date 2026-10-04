import numpy as np
import matplotlib.pyplot as plt

# Example: Simple Linear Regression Loss Function (Mean Squared Error)
def loss_function(w, x, y):
    return np.mean((y - (w * x))**2)

# Gradient of the loss function with respect to w
def gradient(w, x, y):
    return -2 * np.mean(x * (y - (w * x)))

# Gradient Descent Algorithm
def gradient_descent(x, y, learning_rate=0.01, epochs=100):
    w = 0  # Starting value of w
    losses = []

    for epoch in range(epochs):
        grad = gradient(w, x, y)
        w = w - learning_rate * grad  # Update the value of w
        loss = loss_function(w, x, y)  # Calculate the loss
        losses.append(loss)

        if epoch % 10 == 0:  # Print loss every 10 iterations
            print(f"Epoch {epoch}, Loss: {loss}, w: {w}")
    
    return w, losses

# Generate some example data
x = np.linspace(0, 10, 100)  # Features (input)
y = 2 * x + 1 + np.random.randn(100) * 2  # Labels (output with some noise)

# Run Gradient Descent
w, losses = gradient_descent(x, y)

# Plotting the results
plt.plot(losses)
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.title('Gradient Descent Loss Function')
plt.show()

print(f"Final value of w: {w}")
