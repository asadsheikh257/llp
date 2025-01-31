import streamlit as st
import pickle 
import numpy as np

# Import the model
pipe = pickle.load(open('pipe.pkl', 'rb'))
df = pickle.load(open('df.pkl', 'rb'))

st.title("Laptop Predictor")

# Brand
company = st.selectbox('Brand', df['Company'].unique())

# Type of Laptop
type = st.selectbox('Type', df['TypeName'].unique())

# Ram 
ram = st.selectbox('RAM (in GB)', [2,4,6,8,12,16,24,32,64])

# Weight
weight = st.selectbox('Weight', df['Weight'].unique())

# TouchScreen
touchscreen = st.selectbox('TouchScreen', ['No', 'Yes'])

# IPS
ips = st.selectbox('IPS', ['No', 'Yes'])

# ScreenSize 
screensize = st.number_input('Screen Size')

# Resolution
resolution = st.selectbox('Screen Resolution', ['1920x1080', '1366x768', '1600x900', '3840x2160', '3200x1800', '2880x1800', '2560x1600', '2560x1440', '2304x1440'])

# Cpu
cpu = st.selectbox('CPU', df['cpu_brand'].unique())

# HDD
hdd = st.selectbox('HDD (in GB)', [0, 128, 256, 512, 1024, 2048])

# SDD
ssd = st.selectbox('SDD (in GB)', [0, 8, 128, 256, 512, 1024, 2048])

# GPU
gpu = st.selectbox('GPU', df['Gpu'].unique())

# OS 
os = st.selectbox('OS', df['OpSys'].unique())

if st.button('Predict Price'):

    ppi = None

    if touchscreen == 'Yes':
        touchscreen = 1
    else: 
        touchscreen = 0 
    if ips == 'Yes':
        ips = 1
    else:
        ips = 0

    x_res = int(resolution.split('x')[0])
    y_res = int(resolution.split('x')[1])
    ppi = ((x_res**2) + (y_res**2))**0.5/screensize

    # query
    query = np.array([company, type, ram, gpu, os, weight, ips, ppi, touchscreen, cpu, hdd, ssd], dtype=object)
    # print(query)
    query = query.reshape(1,12)
    st.title('The Predicted Price of this configuration is : ' + str(int(np.exp(pipe.predict(query)))))