import wget
from datetime import datetime
import json
from pathlib import Path

# ►►Пример изменений для отслживания в Git (19.09.2022)◄◄

# ▼ Загрузка файла с сайта

new_date = datetime.now()

n = open('upload_date.txt','r')
old_date = n.read()
n.close()

old_change_date = datetime.strptime(old_date, "%Y-%m-%d %H:%M:%S.%f")
period = new_date - old_change_date

def file_download (url):
    wget.download(url,  f'C:\DJ_space_virtual_environment\DJ_space\cod_python\satellite_data\satellite_data_{new_date}.json')

def sorting_and_recording (n_d): # ◄ Функция сортировки и записи данных
    outpath = Path.cwd() / 'satellite_data' / f'satellite_data_{n_d}.json'

    with open(outpath, "r") as read_file:
        data = json.load(read_file)
        
    print (type(data))
    print (data[1]['satellite'])
    print (data[1])
    print (len(data))

    list_satellite_17 = []
    list_satellite_16 = []
    list_satellite_x = []

    for i in range(len(data)):
        if data[i]['satellite']==17:
            list_satellite_17.append(data[i])
        elif data[i]['satellite']==16:
            list_satellite_16.append(data[i])
        else:
            list_satellite_x.append(data[i])

    satellite_17 = Path.cwd() / 'satellite_data' / 'satellite_17' / f"satellite_17_data_{n_d}.json"
    with open(satellite_17,"w") as st_17: 
        json.dump(list_satellite_17,st_17)
        
    satellite_16 = Path.cwd() / 'satellite_data' / 'satellite_16' / f"satellite_16_data_{n_d}.json"
    with open(satellite_16,"w") as st_16: 
        json.dump(list_satellite_16,st_16)
        
    satellite_x = Path.cwd() / 'satellite_data' / 'satellite_x' / f"satellite_x_data_{n_d}.json"
    with open(satellite_x,"w") as st_x: 
        json.dump(list_satellite_x,st_x)

if period.days == 0:
    print ("Сегодня показания спутника уже скачивались")
else:
    k = open('upload_date.txt','w')
    k.write(f'{new_date}')
    new_date = new_date.strftime("%Y-%m-%d_%H.%M")
    k.close()
    
    print('Начало загрузки файла с помощью модуля wget')
    file_download ('https://services.swpc.noaa.gov/json/goes/secondary/differential-protons-1-day.json')
        
    # ▼ Сортировка и запись данных
    sorting_and_recording (new_date)