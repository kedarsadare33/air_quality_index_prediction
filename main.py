# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 02:55:00 2023

@author: Sony
"""

import numpy as np
import streamlit as st  
import pickle

# Loading the saved model
model = pickle.load(open("lasso_model.sav",'rb'))

# creating a function for Prediction

def aqi_prediction(input_data):
    

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0]>0 and prediction[0]<50):
        return 'Good'
    elif (prediction[0]>51 and prediction[0]<100):
        return 'Moderate'
    elif (prediction[0]>101 and prediction[0]<150):
        return 'Unhealthy for Sensitive Groups'
    elif (prediction[0]>151 and prediction[0]<200):
        return 'Unhealthy'
    elif (prediction[0]>201 and prediction[0]<150):
        return 'Very Unhealthy'
    elif (prediction[0]>300):
        return 'Hazardous'


def main():
    
    
    # giving a title
    st.title('Air Quality Index Prediction App')
    
    
    # getting the input data from the user
    
    
    PM2_5 = st.number_input('Fine Particulate Matter (PM2.5)')
    PM10 = st.number_input('Fine Particular Matter (PM10)')
    NO = st.number_input('Nitric Oxide (NO)')
    NO2 = st.number_input('Nitrogen Dioxide (NO2)')
    NOx = st.number_input('Nitrogen Oxides (NOx)')
    NH3 = st.number_input('Ammonia Pollution (NH3)')
    CO = st.number_input('Carbon Monoxide (CO)')
    SO2 = st.number_input('Sulfur Dioxide (SO2)')
    O3 = st.number_input('Ozone at Ground Level (O3)')
    Benzene = st.number_input('Benzene level in Air')
    Toluene = st.number_input('Toluene level in Air')
    Xylene = st.number_input('Xylene level in Air')

    
    
    # code for Prediction
    result = ''
    
    # creating a button for Prediction
    
    if st.button('Submit'):
        result = aqi_prediction([PM2_5, PM10, NO, NO2, NOx, NH3, CO, SO2, O3, Benzene, Toluene, Xylene])
        
        
    st.success(result)
    
    
    
    
    
if __name__ == '__main__':
    main()
