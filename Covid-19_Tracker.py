#Hermawan - NEVTIK Programming Division
import requests
from bs4 import BeautifulSoup as bs
from module import visual, speech_info

url = requests.get("https://www.worldometers.info/coronavirus/").text
data_parent = bs(url,'html.parser')

total_today = int(''.join([i for i in data_parent.find_all('div',id='maincounter-wrap')[0].text if i.isnumeric()]))
death_today = int(''.join([i for i in data_parent.find_all('div',id='maincounter-wrap')[1].text if i.isnumeric()]))

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
columns = ['negara','total_kasus','kasus_baru','total_kematian','kematian_baru','total_disembuhkan','kasus_aktif']

visual.data_table(total_today,['date','cases','death'],death = death_today)
dataframe = visual.data_table(detail,columns,detail = True)
print("\n\n"+dataframe.to_string())
input("\nPress ENTER\n")
visual.gcase_death(dataframe,'total_kasus','total_kematian')
visual.gcase_date()

while True:
    speech_info.text_to_speech("""
\nInformasi tentang Corona apa yang ingin anda cari : 
-Total Kasus.
-Kasus Baru.
-Total Kematian.
-Kematian Baru.
-Total Disembuhkan.
-Kasus Aktif.""")

    category = '_'.join(str(speech_info.speech_recognize('id-ID')).lower().split())
    inputs = print("\n"+category)
    if category in columns and category != None :
        speech_info.text_to_speech("Dari negara mana?")
        country_input = str(speech_info.speech_recognize('en-US')).title()
        index = columns.index(category)-1
        speech_info.text_to_speech('{cat} di {country} adalah {tot}'.format(cat = category.replace('_',' '),
        country = country_input,tot=detail_dict[country_input][index]))
        break
    else:
        speech_info.text_to_speech('Input tidak valid')

