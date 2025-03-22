# 💉 Diabetes Predictor Web App

Predict the likelihood of diabetes using health data.  
Built with **scikit-learn** and **Streamlit** for real-time interactive inference.

---

## 📌 Features

- ✅ Trained on [Pima Indians Diabetes Dataset](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database)
- 🧠 Models: Logistic Regression, Decision Tree (using the better-performing one)
- 🌐 Web UI built with [Streamlit](https://streamlit.io/)
- 📈 Predicts based on 8 health indicators:
  - Pregnancies
  - Glucose
  - Blood Pressure
  - Skin Thickness
  - Insulin
  - BMI
  - Diabetes Pedigree Function (DPF)
  - Age

---

## 🚀 Live Demo

🔗 [Click to try the app](https://diabetes-predictor-7kt52pk4h9wuzbfhodjtqc.streamlit.app/)

---

## 🛠 How to run locally

1. **Clone the repo:**

```bash
git clone https://github.com/ncqxm/diabetes-predictor.git
cd diabetes-predictor
```

2. **Install required packages:**
```bash
pip install -r requirements.txt
```

3. **Run the app:**

```bash
streamlit run app.py
```


## 🙋‍♂️ Author
Made with ❤️ by [ncqxm](https://github.com/ncqxm)