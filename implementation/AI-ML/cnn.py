import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import numpy as np
import matplotlib.pyplot as plt

# Loading and preprocess the dataset
mnist = keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Normalizing the images
x_train, x_test = x_train / 255.0, x_test / 255.0

# Reshaping the images to fit CNN input (28x28x1)
x_train = x_train.reshape(-1, 28, 28, 1)
x_test = x_test.reshape(-1, 28, 28, 1)

# Defining the CNN model
model = keras.Sequential([
    layers.Conv2D(32, (3,3), activation='relu', input_shape=(28,28,1)),
    layers.MaxPooling2D((2,2)),
    layers.Conv2D(64, (3,3), activation='relu'),
    layers.MaxPooling2D((2,2)),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax')
])

# Compiling the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Training the model
model.fit(x_train, y_train, epochs=10, validation_data=(x_test, y_test))

# Evaluating the model
test_loss, test_acc = model.evaluate(x_test, y_test)
print(f"Test Accuracy: {test_acc * 100:.2f}%")

# Predicting on a sample image
sample_image = np.expand_dims(x_test[0], axis=0)
prediction = np.argmax(model.predict(sample_image))
print(f"Predicted Digit: {prediction}")

# Displaying the sample image
plt.imshow(x_test[0].reshape(28, 28), cmap='gray')
plt.title(f"Predicted: {prediction}")
plt.show()
