import streamlit as st
from streamlit_echarts import st_echarts
import socket
import plotly.express as px
import plotly.graph_objects as go
from email_feature import send_email
from car_can import CarCan
from KeyLessEntryAttack import KLE
from utils import *
import joblib
from cryptography.fernet import Fernet
from car import Car

import ard


model = joblib.load('RandomForest.joblib')
st.title("E-Vehicle Cyber Attack")

attack_type = st.selectbox("Select a type of attack", ['KeyFRA', 'Relay Attack', 'Data Breach and malware'])

if attack_type == 'KeyFRA':
    st.subheader("Key FRA attack")

    channel = st.number_input('Enter Car Channel: ')
    max_freq = st.number_input('Max Frequency: ')
    upload = st.button('Attack')
    if upload:
        st.write('Starting KLE Attack')
        try:
            c = CarCan()
            kle = KLE()
            data = kle.attack_algo(channel, 30)
        except:
            data = launch_except(channel, max_freq)
        

        echart_data = {
            'xAxis': {"type" : "category", "data" : data['time']},
            'yAxis' : {"type" : "value"},
            "series" : [{"data" : data['packets'], "type" : "line", "name" : "KLE"}]
        }

        identification = model.predict([data['packets']])
        if identification[0] == 0:
            st.info('KLE Not Found')
            ard.turn_off_relay()
        else:
            st.warning('KLE Found')
            ard.turn_on_relay()
            send_email('me@pankajbhattarai.com.np', 'E Vehicle Warning', 'Keyless entry Breach Detected in E-Vehicle', [])
        st_echarts(options=echart_data, height=400, theme="dark")
    
elif attack_type == 'Relay Attack':
    st.subheader("Relay Attack")
    model = joblib.load('RelayAttack.joblib')
    timedelta = st.number_input("TimeDelta :")
    distance = st.number_input("Distance Between car and device :")
    min_signal_strength = st.number_input(" Minimum Signal Strength :")
    max_signal_strength = st.number_input("Max Signal Strength :")
    upload = st.button('Check')

    if upload:
        st.write('Starting Relay Attack')
        try:
            c = CarCan()
            kle = KLE()
            data = kle.relay_attack(timedelta, distance, max_signal_strength, min_signal_strength)
        except:
            data = launch_relay(timedelta, distance, max_signal_strength, min_signal_strength)

        echart_data = {
            'xAxis': {"type" : "category", "data" : data['frame']},
            'yAxis' : {"type" : "value"},
            "series" : [{"data" : data['strength'], "type" : "line", "name" : "Relay"}]
        }

        detections = []

        for j in data['strength']:
            detections.append(model.predict([[timedelta, distance, j]])[0])
        
        st.dataframe({'time' : [timedelta for _ in range(len(detections))],
                      'distance' : [distance for _ in range(len(detections))],
                      'detections' : detections,
                      'signal' : data['strength']
                      })
        if detections.count(1) > detections.count(0):
            st.warning('Relay Attack Detected')
            ard.turn_on_relay()
            send_email('me@pankajbhattarai.com.np', 'E Vehicle Warning', ' Relay Breach Detected in E-Vehicle', [])
        else:
            st.info('No relay attack detected')
            ard.turn_off_relay()
        st_echarts(options=echart_data, height=400, theme="dark")
else:
    from cryptography.fernet import Fernet

    key = Fernet.generate_key()
    cipher_suite = Fernet(key)

    # st.title('Car Technical Data and Encryption')

    def encrypt_data(data):
        return cipher_suite.encrypt(data.encode())

    def decrypt_data(encrypted_data):
        return cipher_suite.decrypt(encrypted_data).decode()

    car = Car("Tesla", "Model S", 2023, "Electric", 670, 850, 0, 0)

    if st.button('Accelerate'):
        car.accelerate(5)
        car.update_speed()
        st.write(car.get_info())
    if st.button('Brake'):
        car.brake(5)
        car.update_speed()
        st.write(car.get_info())
    
    encrypted_info = None
    st.info('Click the button to send the encrypted data')
    if st.button('Encrypt Car Info'):
        encrypted_info = encrypt_data(car.get_info())
        st.write('Encrypted Car Info:', encrypted_info)
