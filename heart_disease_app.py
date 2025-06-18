import joblib
import pandas as pd

# Load the trained model
model = joblib.load("heart_model.pkl")

# Input prompts
print("🔍 Please enter the following details:")

age = int(input("Enter your age: "))
sex = int(input("Enter your sex (1 = male, 0 = female): "))
cp = int(input("Enter chest pain type (0-3): "))
trestbps = int(input("Enter resting blood pressure (e.g., 130): "))
chol = int(input("Enter serum cholesterol (e.g., 240): "))
fbs = int(input("Fasting blood sugar > 120 mg/dl (1 = yes, 0 = no): "))
restecg = int(input("Enter resting electrocardiographic result (0-2): "))
thalach = int(input("Enter max heart rate achieved: "))
exang = int(input("Exercise-induced angina (1 = yes, 0 = no): "))
oldpeak = float(input("Enter ST depression value: "))
slope = int(input("Enter slope of peak exercise ST segment (0-2): "))
ca = int(input("Enter number of major vessels (0-3): "))
thal = int(input("Enter thalassemia value (1 = normal, 2 = fixed defect, 3 = reversible defect): "))

# Prepare input data
input_data = [[age, sex, cp, trestbps, chol, fbs, restecg,
               thalach, exang, oldpeak, slope, ca, thal]]

# Use DataFrame to include feature names
feature_names = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg',
                 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']
input_df = pd.DataFrame(input_data, columns=feature_names)

# Make prediction
prediction = model.predict(input_df)

# Output result
print("\n🩺 Prediction result:")
if prediction[0] == 1:
    print("🔴 The patient is likely to have heart disease.")
else:
    print("🟢 The patient is likely to NOT have heart disease.")
