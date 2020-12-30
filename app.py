# Get data from john hopkins
# https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/12-27-2020.csv

import pandas as pd
import requests 
from bs4 import BeautifulSoup 


#Global variables
url     = 'https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_daily_reports'
reqs    = requests.get(url) 
soup    = BeautifulSoup(reqs.text, 'html.parser') 
urls    = [] 
denmark = [] 

for link in soup.find_all('a'): 
    if link['href'].endswith('.csv'):
        csv_url = ("https://raw.githubusercontent.com"+link.get('href'))    #Create proper Raw link
        csv_url = csv_url.replace('/blob', '')                              #Create proper Raw link
        date = csv_url[2:-4]
        print (csv_url)                                                     #Print converted URL
        data = pd.read_csv(csv_url, index_col=None, header=0)
        #data = pd.read_csv(csv_url) 
        if 'Denmark' in data.values:
            if 'Country/Region' in data:                                    #Cleanup colum names
                data = data.rename(columns = {'Country/Region': 'Country_Region'}, inplace = False)

            
            data = data[(data['Country_Region'] == 'Denmark') ]             #Add Denmark data
            denmark.append(data)                                            #Add Append data to existing dataframe

        
#Cleanup Dataframe
denmark = pd.concat(denmark, axis=0, ignore_index=True)        
denmark = denmark[(denmark['Country_Region'] == 'Denmark') & (denmark['Province_State'] != 'Faroe Islands') & (denmark['Province_State'] != 'Greenland')]
print (denmark)