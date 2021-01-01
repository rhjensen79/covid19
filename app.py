import streamlit as st
import pandas as pd

#Read CSV
data = pd.read_csv("data.csv", index_col=None, header=0) 


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


#Initialise Chart DF
chart = pd.DataFrame()


#Copy relavant DF data
chart['Confirmed'] = data['Confirmed'].copy()
chart['Deaths'] = data['Deaths'].copy()
chart['Recovered'] = data['Recovered'].copy()
chart['Active'] = data['Active'].copy()


#Present
st.text('COVID-19 data for Denmark')
st.line_chart(chart)