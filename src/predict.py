import joblib
import requests
import pandas as pd

# 1. Load the model
model = joblib.load('model.joblib')

# 2. Get metrics from the application
try:
    response = requests.get('http://127.0.0.1:5000/anomaly')
    metrics = response.json()
except requests.exceptions.ConnectionError as e:
    print(f"Error connecting to the application: {e}")
    exit(1)


# 3. Predict anomalies
df = pd.DataFrame([metrics])
prediction = model.predict(df[['cpu_usage', 'memory_usage', 'response_time']])

# 4. Exit with a non-zero status code if an anomaly is detected
if prediction[0] == -1:
    print("Anomaly detected!")
    exit(1)
else:
    print("No anomaly detected.")
    exit(0)
