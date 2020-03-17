#Hermawan - NEVTIK Programming Division
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date
import speech_info

url = requests.get("https://www.worldometers.info/coronavirus/").text
data_parent = bs(url,'html.parser')
today = date.today()
corona_date = pd.DataFrame({'date':today,'cases':int(''.join([i for i in data_parent.find_all('div',id='maincounter-wrap')[0].text if i.isnumeric()]))},index = [0])
try:
    corona_bydate = pd.read_csv('Corona_Case.csv')
    corona_bydate.append(corona_date)
    corona_bydate.drop_duplicates('date',keep=False,inplace=True)
    corona_bydate.to_csv('Corona_Case.csv',index = None,header = True)
except:
    corona_date.to_csv('Corona_Case.csv',index=None,header=True)

table = data_parent.find('tbody').find_all('tr')
table_body = [table_data.find_all('td') for table_data in table]

country_list = [i[0].text.strip() for i in table_body]
total_cases = [int(i[1].text.strip().replace(',','')) for i in table_body]
new_cases = [0 if i[2].text.strip()=='' else int(i[2].text.strip().strip('+').replace(',','')) for i in table_body]
total_deaths = [0 if i[3].text.strip()=='' else int(i[3].text.strip().replace(',','')) for i in table_body]
new_deaths = [0 if i[4].text.strip()=='' else int(i[4].text.strip().strip('+').replace(',','')) for i in table_body]
total_recovered = [0 if i[5].text.strip()=='' else int(i[5].text.strip().replace(',','')) for i in table_body]
active_cases = [int(i[6].text.strip().replace(',','')) for i in table_body]

detail = list(zip(country_list,total_cases,new_cases,total_deaths,new_deaths,total_recovered,active_cases))
detail_dict = {k:v for (k,*v) in detail}
columns = ['Negara','Total_Kasus','Kasus_Baru','Total_Kematian','Kematian_Baru','Total_Disembuhkan','Kasus_Aktif']

dataframe = pd.DataFrame(detail,columns=columns)
dataframe.to_csv('Corona_Case_{}.csv'.format(date.today()),index=None,header=True)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', -1)
print(dataframe)

def graphic(title,list_name,ytitle,sort=False):
    data_frame = dataframe
    if sort==True:
        data_frame = dataframe.sort_values(by=[list_name],ascending=False)
    fig, (ax1, ax2,ax3) = plt.subplots(1, 3,figsize=(15,6))
    plt.figure(figsize=(15,6))
    fig.suptitle(title)
    ax1.bar(data_frame['Negara'][:6], data_frame[list_name][:6],alpha=0.7,color='red')
    ax2.bar(data_frame['Negara'][6:30], data_frame[list_name][6:30],alpha=0.7,color='green')
    ax3.bar(data_frame['Negara'][30:51],data_frame[list_name][30:51],alpha= 0.7,color='blue')
    ax1.set_ylabel(ytitle)
    ax2.tick_params(axis = 'x',labelrotation=90);ax3.tick_params(axis = 'x', labelrotation=90);ax1.tick_params(axis = 'x',labelrotation = 70)
    plt.show()
graphic('50 Highest Corona Cases by Country','Total_Kasus','Total Kasus')
graphic('50 Highest Death Rate by Corona Cases each Country','Total_Kematian','Total Kematian',sort=True)
b = pd.read_csv('Corona_Case.csv')
plt.bar(b['date'],b['cases'])
plt.show()


