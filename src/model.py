import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib
import random

# 1. Generate synthetic data
print("Generating synthetic data...")
data = {
    'cpu_usage': [],
    'memory_usage': [],
    'response_time': [],
    'anomaly': []
}

for _ in range(1000):
    # Normal data
    data['cpu_usage'].append(random.uniform(10, 50))
    data['memory_usage'].append(random.uniform(200, 1024))
    data['response_time'].append(random.uniform(0.1, 0.5))
    data['anomaly'].append(0)

for _ in range(100):
    # Anomalous data
    data['cpu_usage'].append(random.uniform(10, 50) * random.uniform(2, 4))
    data['memory_usage'].append(random.uniform(200, 1024) * random.uniform(1.5, 3))
    data['response_time'].append(random.uniform(0.1, 0.5) * random.uniform(3, 5))
    data['anomaly'].append(1)

df = pd.DataFrame(data)

# 2. Train the model
print("Training the model...")
X = df[['cpu_usage', 'memory_usage', 'response_time']]
model = IsolationForest(contamination=0.1, random_state=42)
model.fit(X)

# 3. Save the model
print("Saving the model...")
joblib.dump(model, 'model.joblib')

print("Model training complete.")
