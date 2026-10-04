import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Generating synthetic dataset
np.random.seed(42)
data_size = 100

cpu_usage = np.random.randint(10, 90, data_size)
memory_consumption = np.random.randint(100, 800, data_size)
execution_time = np.random.randint(1, 10, data_size)

# High Load (1) if CPU > 50 and Memory > 400, else Low Load (0)
load_category = np.where((cpu_usage > 50) & (memory_consumption > 400), 1, 0)

# Creating DataFrame
df = pd.DataFrame({'CPU': cpu_usage, 'Memory': memory_consumption, 'Execution Time': execution_time, 'Load': load_category})

# Splitting data
X = df[['CPU', 'Memory', 'Execution Time']]
y = df['Load']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Training the SVM model
svm_model = SVC(kernel='linear')
svm_model.fit(X_train, y_train)

# Predictions
y_pred = svm_model.predict(X_test)

# Accuracy evaluation
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy * 100:.2f}%")

# Testing with a new function request
new_function = np.array([[60, 450, 5]])  # Example function with CPU=60, Memory=450, Execution Time=5
prediction = svm_model.predict(new_function)
print("Predicted Load Category:", "High Load" if prediction[0] == 1 else "Low Load")
