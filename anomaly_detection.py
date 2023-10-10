#Anomaly detection

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest

# Generate a synthetic dataset (you can replace this with your own data)
np.random.seed(42)
n_samples = 200
n_features = 2
data = np.random.randn(n_samples, n_features)

# Create a DataFrame from the data (optional)
df = pd.DataFrame(data, columns=["Feature1", "Feature2"])

# Train the Isolation Forest model
model = IsolationForest(contamination=0.05, random_state=42)
model.fit(data)

# Predict anomaly scores (-1 for anomalies, 1 for normal points)
anomaly_scores = model.predict(data)

# Identify anomalies
anomalies = df[anomaly_scores == -1]

# Display the data frame
print("Data Frame:")
print(df)

# Visualize anomalies and normal points (customize based on your dataset)
plt.scatter(df["Feature1"], df["Feature2"], c="blue", label="Normal")
plt.scatter(anomalies["Feature1"], anomalies["Feature2"], c="red", label="Anomaly")
plt.xlabel("Feature1")
plt.ylabel("Feature2")
plt.title("Anomaly Detection")
plt.legend()
plt.show()
