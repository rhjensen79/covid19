# Get data from john hopkins
# https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/12-27-2020.csv

import pandas as pd
import requests 
from bs4 import BeautifulSoup 

#Global variables
url = 'https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_daily_reports'
reqs = requests.get(url) 
soup = BeautifulSoup(reqs.text, 'html.parser') 

#Get data
#data = pd.read_csv(url+date+'.csv')

#Filter data to Denmark
#denmark = data[(data['Country_Region'] == 'Denmark') & (data['Province_State'] != 'Faroe Islands') & (data['Province_State'] != 'Greenland')]
#print (denmark)

urls = [] 
denmark = [] 
for link in soup.find_all('a'): 
    if link['href'].endswith('.csv'):
        csv_url = ("https://raw.githubusercontent.com"+link.get('href')) 
        #print (csv_url)
        csv_url = csv_url.replace('/blob', '')
        print (csv_url)
        #print("https://raw.githubusercontent.com"+link.get('href')) 
        data = pd.read_csv(csv_url) 
        denmark.append(data)
        #data = data[(data['Country_Region'] == 'Denmark') & (data['Province_State'] != 'Faroe Islands') & (data['Province_State'] != 'Greenland')]
#denmark = denmark[(data['Country_Region'] == 'Denmark') & (data['Province_State'] != 'Faroe Islands') & (data['Province_State'] != 'Greenland')]
#print (denmark)