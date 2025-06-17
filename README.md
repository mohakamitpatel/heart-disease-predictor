# 🫀 Heart Disease Predictor

[![Python](https://img.shields.io/badge/Python-3.10-blue.svg)](https://www.python.org/)
[![Model Accuracy](https://img.shields.io/badge/Model%20Accuracy-85%25-green)]()

> 🎯 Predict the likelihood of heart disease using clinical data and machine learning.

---

## 📸 Demo Preview

![Terminal Demo](https://via.placeholder.com/800x400.png?text=Terminal+Prediction+Demo)

> 🔧 Predict heart disease risk right from your terminal in under 2 minutes!

---

## 🔍 Features

- 🧠 Predicts risk of heart disease using a trained Random Forest Classifier  
- ⚡ Simple and interactive **command-line interface**
- 📈 Uses the UCI Heart Disease dataset (Cleveland subset)
- 🔄 Full pipeline: model training, saving, and real-time inference
- 🧪 Easy to adapt for any binary classification task

---

## 🗂️ Project Structure

```
📂 heart-disease-predictor
 ├── 📁 data/                # Dataset folder (heart.csv)
 ├── 🧠 model.py             # Script to train and save the model
 ├── 🧪 evaluation.py        # Evaluation metrics and confusion matrix
 ├── 🧠 heart_disease_app.py # Command-line prediction script
 ├── 🗂️ heart_model.pkl       # Trained ML model
 ├── 📜 requirements.txt     # Python dependencies
 └── 📘 README.md            # Project overview and instructions
```

---

## ⚙️ Installation

1. **Clone the repository**  
   ```bash
   git clone https://github.com/yourusername/heart-disease-predictor.git
   cd heart-disease-predictor
   ```

2. **Install dependencies**  
   Make sure Python 3.10+ and pip are installed on your system.  
   Then run:
   ```bash
   pip install -r requirements.txt
   ```

3. **Train the model**  
   This will train and save the model to `heart_model.pkl`:
   ```bash
   python model.py
   ```

4. **Run the prediction app**  
   This will ask for clinical inputs and give a prediction:
   ```bash
   python heart_disease_app.py
   ```

---

## 📊 Dataset

This project uses the **Cleveland subset** of the [UCI Heart Disease dataset](https://archive.ics.uci.edu/ml/datasets/Heart+Disease), a well-known dataset for binary heart disease classification.

The dataset contains 13 clinical features such as age, sex, chest pain type, cholesterol, max heart rate, and more.

You should place the dataset as `heart.csv` inside the `data/` folder.

---

## 📦 Model

We use a `RandomForestClassifier` from scikit-learn trained on the UCI dataset.

The trained model is serialized using `joblib` and saved as `heart_model.pkl`, which can be reused without retraining.

You can use this model to make predictions with any compatible input using:

```python
import joblib
model = joblib.load("heart_model.pkl")
prediction = model.predict([your_input])
```

---

## ✅ Requirements

All required libraries are listed in `requirements.txt`. Here's what's included:

```
pandas
numpy
scikit-learn
joblib
matplotlib
seaborn
```

To install them, run:

```bash
pip install -r requirements.txt
```

---

## 📄 License

This project is **not licensed**.  
You are free to use, modify, and share this code for personal or academic purposes.

---

## 🙌 Acknowledgements

- [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/index.php)
- Built using Python, scikit-learn, pandas, matplotlib, and joblib

---

> Created with ❤️ by [Your Name or GitHub Username]
