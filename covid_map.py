import streamlit as st
import pandas as pd
import numpy as np

st.title('Covid-19 Cases')

DATE_COLUMN = 'date/time'
DATA_URL = ('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/07-26-2020.csv')

#@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL)
    #lowercase = lambda x: str(x).lower()
    #data.rename(lowercase, axis='columns', inplace=True)
    data.rename({'Long_':'lon'}, axis='columns', inplace=True)
    data.rename({'Lat':'lat'}, axis='columns', inplace=True)
    data.lon.dtype
    data.lat.dtype 
    #data[last_update] = pd.to_datetime(data[DATE_COLUMN])
    return data

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data(10000)
# Notify the reader that the data was successfully loaded.
data_load_state.text("Done! (using st.cache)") 

#Show Raw data
if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

#st.map(data)
#st.bar_chart(data)
chart_data = data[['lon', 'lat']]
st.write(chart_data)
chart_data.lon.dtype
chart_data.lat.dtype 
#st.bar_chart(chart_data)
st.map(chart_data)