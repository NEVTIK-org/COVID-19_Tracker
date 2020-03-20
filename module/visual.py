import pandas as pd
import matplotlib.pyplot as plt
from datetime import date
from time import sleep

today = str(date.today()).split('-')
today = "{}/{}/{}".format(today[1].lstrip('0'),today[2].lstrip('0'),today[0])

def data_table(data,columns,death=None,detail=False):
    if detail == True:
        dataframe = pd.DataFrame(data,columns=columns)
        dataframe.to_csv('data/Corona_Case_{}.csv'.format(date.today()),index=None,header=True)
    else:
        try:
            corona_date = pd.DataFrame({'date':today,'cases':data,'death':death},columns = columns, index = [0])
            corona_bydate = pd.read_csv('data/Corona_Case.csv')
            dataframe = corona_bydate.append(corona_date)
            dataframe.drop_duplicates('date',inplace=True)
            print(dataframe)
            dataframe.to_csv('data/Corona_Case.csv',index = None,header = True)
        except:
            corona_date.to_csv('data/Corona_Case.csv',index = None,header = True)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', -1)
    return dataframe

def gcase_death(data,list_name,list_name2):
    data_frame = data
    death_frame = data.sort_values(by=[list_name2],ascending=False)
    fig, (ax1, ax2) = plt.subplots(1, 2,figsize=(15,6))
    fig.suptitle('10 Negara dengan Kasus dan Kematian Terbanyak akibat Corona (Realtime)')
    ax1.bar(data_frame['negara'][:11], data_frame[list_name][:11],alpha=0.7,color='orange')
    ax2.bar(death_frame['negara'][:11], death_frame[list_name2][:11],alpha=0.7,color='red')
    ax1.set_ylabel('Total Kasus');ax2.set_xlabel('Total Kematian')
    ax1.title.set_text('Total Kasus / Negara');ax2.title.set_text('Total Kematian / Negara')
    ax2.tick_params(axis = 'x',labelrotation=70);ax1.tick_params(axis = 'x',labelrotation = 70)
    plt.show()

def gcase_date():
    b = pd.read_csv('data/Corona_Case.csv')
    plt.style.use('seaborn')
    plt.figure(figsize=(15,6))
    plt.title("Grafik Perkembangan Kasus Corona / Hari")
    plt.ylabel('Jumlah Kasus');plt.xlabel("Waktu")
    plt.bar(b['date'],b['cases'],alpha=0.9)
    plt.bar(b['date'],b['death'],alpha=0.9,color='orange')
    plt.xticks(rotation='-70')
    plt.show()
