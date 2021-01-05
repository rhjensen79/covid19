import streamlit as st
import pandas as pd

#Read CSV
data = pd.read_csv("/app/data.csv", index_col=None, header=0) 

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

#Copy relavant DF to data
chart['Confirmed'] = data['Confirmed'].copy()
chart['Deaths'] = data['Deaths'].copy()
chart['Recovered'] = data['Recovered'].copy()
chart['Active'] = data['Active'].copy()
print (chart)

#Convert and sort by date
chart['Date'] = pd.to_datetime(data['Date'], format='%m-%d-%Y')
chart = chart.sort_values(by='Date')


#Streamlit config
st.set_page_config(
    page_title="CMP Value",
    layout="wide",
    initial_sidebar_state="collapsed",
)

#Present
st.title('COVID-19 data for Denmark')

st.write ('Data gathered from Johns Hopkins University github repo')
st.write ('filtered to only show Denmarks data')
st.write ('url : https://github.com/CSSEGISandData/COVID-19')
st.write ('')


#Split into colums
col1, col2 = st.beta_columns(2)

with col1:
    st.write('Confirmed - Last number : ',chart['Confirmed'].iloc[-1])
    chart = chart.set_index('Date')
    st.line_chart(chart['Confirmed'])

with col2:
    st.write('Deaths - Last number : ',chart['Deaths'].iloc[-1])
    st.line_chart(chart['Deaths'])

with col1:
    st.write('Recovered - Last number : ',chart['Recovered'].iloc[-1])
    st.line_chart(chart['Recovered'])

with col2:
    st.write('Active - Last number : ',chart['Active'].iloc[-1])
    st.line_chart(chart['Active'])

st.write ('All info around this page, can be found here : https://github.com/rhjensen79/covid19')