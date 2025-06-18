# evaluation.py

import pandas as pd
import joblib
from sklearn.metrics import classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Load dataset
data_path = os.path.join("data", "heart.csv")
df = pd.read_csv(data_path)

# Load trained model
model = joblib.load("heart_model.pkl")

# Separate features and target
X = df.drop("target", axis=1)
y = df["target"]

# Predict using the trained model
y_pred = model.predict(X)

# Print classification report
print("\n🧾 Classification Report:\n")
print(classification_report(y, y_pred))

# Create confusion matrix
print("📉 Confusion Matrix:\n")
cm = confusion_matrix(y, y_pred)

# Visualize confusion matrix
plt.figure(figsize=(6, 4))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", cbar=False,
            xticklabels=["No Disease", "Disease"], yticklabels=["No Disease", "Disease"])
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")
plt.tight_layout()
plt.show()
