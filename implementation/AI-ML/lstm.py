import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

# Generating synthetic CPU load data
np.random.seed(42)
time_steps = 100
cpu_load = np.sin(np.linspace(0, 10, time_steps)) + np.random.normal(0, 0.1, time_steps)

# Normalizing data
scaler = MinMaxScaler()
cpu_load_scaled = scaler.fit_transform(cpu_load.reshape(-1, 1))

# Preparing dataset for LSTM
X, y = [], []
seq_length = 10
for i in range(len(cpu_load_scaled) - seq_length):
    X.append(cpu_load_scaled[i:i+seq_length])
    y.append(cpu_load_scaled[i+seq_length])

X = np.array(X)
y = np.array(y)

# Splitting into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Building LSTM model
model = Sequential([
    LSTM(50, activation='relu', input_shape=(seq_length, 1)),
    Dense(1)
])

model.compile(optimizer='adam', loss='mse')

# Training model
model.fit(X_train, y_train, epochs=50, verbose=0)

# Making predictions
y_pred = model.predict(X_test)

# Inversing transform predictions and actual values
y_pred_inv = scaler.inverse_transform(y_pred)
y_test_inv = scaler.inverse_transform(y_test.reshape(-1, 1))

# Plotting results
plt.plot(y_test_inv, label="Actual CPU Load")
plt.plot(y_pred_inv, label="Predicted CPU Load", linestyle="dashed")
plt.legend()
plt.title("LSTM CPU Load Prediction")
plt.show()
