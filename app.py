import streamlit as st
import pandas as pd

data = pd.read_csv("data.csv", index_col=None, header=0) 

print (data)

# Replace missing values with a number
data['Confirmed'].fillna(0, inplace=True)
data['Deaths'].fillna(0, inplace=True)
data['Active'].fillna(0, inplace=True)
data['Incident_Rate'].fillna(0, inplace=True)
data['Case_Fatality_Ratio'].fillna(0, inplace=True)
data['Incidence_Rate'].fillna(0, inplace=True)
data['Case-Fatality_Ratio'].fillna(0, inplace=True)

#Remove colums
data = data.drop(columns=['Province/State', 'Last Update', 'Latitude', 'Longitude','FIPS','Admin2','Province_State','Last_Update','Combined_Key','Lat','Long_'])

print (data)