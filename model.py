# model.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib
import os

# Load the dataset

data_path = os.path.join("data", "heart.csv")
df = pd.read_csv(data_path)

# Separate features and condition
X = df.drop("condition", axis=1)
y = df["condition"]

# Split the dataset into training and testing (80/20)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Initialize the model
model = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the model
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"✅ Model trained successfully! Accuracy on test set: {accuracy:.2f}")

# Save the model to a file
joblib.dump(model, "heart_model.pkl")
print("📦 Model saved to 'heart_model.pkl'")
