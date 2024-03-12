import streamlit as st
import pickle
import numpy as numpy
import pandas as pd


###FUNCTION TO LOAD THE MODEL 
#def load_model():
#    with open ('saved_model.pkl', 'rb') as file:
#        data_load = pickle.load(file)
#    return data_load

#data_load = load_model()
#regressor = data_load.[0] 

# loading in the model to predict on the data 
pickle_in = open("random_forest.pkl", 'rb') 
regressor = pickle.load(pickle_in) 




def show_prediction ():
    # Title and description
    st.image("spe picture.jpg")
    
    st.title("Welcome To CO2 Emission Prediction")
    st.write(" ### Predict CO2 emissions based on location and other factors.")

    st.markdown(
    """
    <style>
    span[data-baseweb="tag"] {
    background-color: blue !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
    )
    

    # User input for prediction
  
    #st.info("Information details of user")

    ### warning 
    st.warning(' Only input numerical values in order to avoid error!')
    # User input for prediction             
    latitude = st.number_input("Latitude:")
    longitude = st.number_input("Longitude:")
    year = st.number_input("Year:")
    week_no = st.number_input("Week number:")

    SulphurDioxide_SO2_column_number_density_amf = st.number_input("SulphurDioxide_SO2_column_number_density_amf:")
    SulphurDioxide_SO2_slant_column_number_density =st.number_input("SulphurDioxide_SO2_slant_column_number_density:")
    SulphurDioxide_cloud_fraction = st.number_input("SulphurDioxide_cloud_fraction:")
                 
    CarbonMonoxide_CO_column_number_density = st.number_input("CarbonMonoxide_CO_column_number_density:")
    CarbonMonoxide_cloud_height =  st.number_input("CarbonMonoxide_cloud_height :")
    CarbonMonoxide_sensor_zenith_angle = st.number_input("CarbonMonoxide_sensor_zenith_angle:")
                 
    NitrogenDioxide_tropospheric_NO2_column_number_density = st.number_input("NitrogenDioxide_tropospheric_NO2_column_number_density:")
    NitrogenDioxide_stratospheric_NO2_column_number_density = st.number_input("NitrogenDioxide_stratospheric_NO2_column_number_density:")
    NitrogenDioxide_tropopause_pressure  = st.number_input("NitrogenDioxide_tropopause_pressure:")
    NitrogenDioxide_cloud_fraction = st.number_input("NitrogenDioxide_cloud_fraction:")
    NitrogenDioxide_sensor_azimuth_angle = st.number_input("NitrogenDioxide_sensor_azimuth_angle:")
                 
    Ozone_O3_column_number_density = st.number_input("Ozone_O3_column_number_density:")
    Ozone_O3_effective_temperature = st.number_input("Ozone_O3_effective_temperature:")
    Ozone_cloud_fraction = st.number_input("Ozone_cloud_fraction:")
    Ozone_solar_zenith_angle = st.number_input("Ozone_solar_zenith_angle:")

    if st.button("Predict"):

        # Prepare prediction data
        prediction_data = pd.DataFrame({
        
        "latitude": [latitude],
        "longitude": [longitude],
        "year": [year],
        "week_no": [week_no],
     
        'SulphurDioxide_SO2_column_number_density_amf' : [ SulphurDioxide_SO2_column_number_density_amf],
        'SulphurDioxide_SO2_slant_column_number_density' : [SulphurDioxide_SO2_slant_column_number_density],
        'SulphurDioxide_cloud_fraction' :[SulphurDioxide_cloud_fraction],
        
        "CarbonMonoxide_CO_column_number_density" :  [CarbonMonoxide_CO_column_number_density],
        "CarbonMonoxide_cloud_height" : [CarbonMonoxide_cloud_height],
        'CarbonMonoxide_sensor_zenith_angle' : [CarbonMonoxide_sensor_zenith_angle],
   
        "NitrogenDioxide_tropospheric_NO2_column_number_density" : [NitrogenDioxide_tropospheric_NO2_column_number_density],
        'NitrogenDioxide_stratospheric_NO2_column_number_density': [NitrogenDioxide_stratospheric_NO2_column_number_density], 
        'NitrogenDioxide_tropopause_pressure'  : [NitrogenDioxide_tropopause_pressure],
        'NitrogenDioxide_cloud_fraction' : [NitrogenDioxide_cloud_fraction],
        'NitrogenDioxide_sensor_azimuth_angle' : [NitrogenDioxide_sensor_azimuth_angle],
        
        'Ozone_O3_column_number_density' : [Ozone_O3_column_number_density],
        'Ozone_O3_effective_temperature' : [Ozone_O3_effective_temperature],
        'Ozone_cloud_fraction' : [ Ozone_cloud_fraction ],
        "Ozone_solar_zenith_angle" : [Ozone_solar_zenith_angle]
        })

        # Make prediction
        predict_CO2 = regressor.predict(prediction_data)[0]
        st.subheader(f"The Predicted Emission Of CO2 Is {predict_CO2:.3f}")
    #return predict_CO2   



