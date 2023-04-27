import pickle
import streamlit as st

model = pickle.load(open('estimasi_lemak.sav', 'rb'))

#Density, Age, Weight , Height, Neck, Chest, Abdomen, Hip, Thigh, Knee, Ankle, Biceps, Forearm ,Wrist
st.title('ESTIMASI PERSENTASE LEMAK TUBUH')
Density = st.number_input('Input kepadatan masa otot Exmpl: 1.0853')
Age = st.number_input('Input Umur (tahun)')
Weight = st.number_input('Input Berat Badan (pound)')
Height = st.number_input('Input Tinggi Badan (inch)')
Neck = st.number_input('Input Lingkar leher (cm)')
Chest = st.number_input('Input Lingkar dada (cm)')
Abdomen = st.number_input('Input Lingkar perut 2 (cm)')
Hip = st.number_input('Input Lingkar Pinggul (cm)')
Thigh = st.number_input('Input Lingkar paha (cm)')
Knee = st.number_input('Input Lingkar lutut (cm)')
Ankle = st.number_input('Input Lingkar pergelangan kaki (cm)')
Biceps = st.number_input('Input lingkar Bisep  (cm)')
Forearm = st.number_input('Input Lingkar lengan bawah (cm)')
Wrist = st.number_input('Input Lingkar pergelangan tangan (cm)')

predict = ''

if st.button('Estimasikan Lemak Tubuh'):
    predict = model.predict(
        [[Density, Age, Weight , Height, Neck, Chest, Abdomen, Hip, Thigh, Knee, Ankle, Biceps, Forearm ,Wrist]]
        )
    st.write ('Estimasi Lemak Tubuh(%) : ', predict)
    