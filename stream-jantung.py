import pickle
import numpy as np
import streamlit as st

# load save model
model = pickle.load(open('penyakit_jantung.sav','rb'))

# judul web
st.title('Prediksi Penyakit Jantung')

col1, col2, col3 = st.columns(3)

with col1: 
    age = st.text_input('Umur')
with col2:
    sex = st.text_input('Jenis Kelamin')
with col3:
    cp = st.text_input('Jenis Nyeri Dada')
with col1:
    trestbps = st.text_input('Tekanan Darah')
with col2:
    chol = st.text_input('Nilai Kolesterol')
with col3:
    fbs = st.text_input('Gula Darah')
with col1:
    restecg = st.text_input('Hasil Elektrokadiografi')
with col2:
    thalach = st.text_input('Detak Jantung Maksimum')
with col3:
    exang = st.text_input('Induksi Angina')
with col1:
    oldpeak = st.text_input('ST Depression')
with col2:
    slope = st.text_input('Slope')
with col3:
    ca = st.text_input('Nilai CA')
with col1:
    thal = st.text_input('Nilai Thal')

# code for prediction
heart_diagnosis =''

# membuat tombol prediksi
if st.button('Prediksi Penyakit Jantung'):
    heart_prediction = model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak,slope,ca,thal]])

    if (heart_prediction[0]==1):
        heart_diagnosis = 'Pasien Terkena Penyakit Jantung'
    else:
        heart_diagnosis = 'Pasien Tidak Terkena Penyakit Jantung'
st.success(heart_diagnosis)
