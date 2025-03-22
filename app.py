import streamlit as st
import joblib
import numpy as np

# โหลดโมเดล
model = joblib.load("diabetes_model.pkl")

st.title("Predict Diabetes from Health Data")

st.markdown("กรอกข้อมูลสุขภาพด้านล่างเพื่อประเมินความเสี่ยงเบาหวาน")

# รับค่าจากผู้ใช้
pregnancies = st.number_input("จำนวนครั้งที่ตั้งครรภ์", min_value=0, max_value=20, value=0)
glucose = st.number_input("ระดับน้ำตาลในเลือด (Glucose)", min_value=0, max_value=300, value=120)
blood_pressure = st.number_input("ความดันโลหิต (Blood Pressure)", min_value=0, max_value=200, value=70)
skin_thickness = st.number_input("ความหนาผิวหนัง (Skin Thickness)", min_value=0, max_value=100, value=20)
insulin = st.number_input("ระดับอินซูลิน", min_value=0, max_value=900, value=80)
bmi = st.number_input("BMI", min_value=0.0, max_value=70.0, value=25.0)
dpf = st.number_input("Diabetes Pedigree Function (DPF)", min_value=0.0, max_value=3.0, value=0.5)
age = st.number_input("อายุ", min_value=1, max_value=120, value=30)

if st.button("ทำนายเลย!"):
    # รวมข้อมูลเป็น array
    input_data = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, dpf, age]])

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("เสี่ยงเป็นเบาหวาน! ไปหาหมอด่วนเลย")
    else:
        st.success("ปลอดภัยดี ยังไม่เสี่ยงเบาหวานตอนนี้")