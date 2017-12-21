import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

input_path = "./data/sfc/sfc_47662.tsv"
output_path = "data/flu/flu0.csv"

df = pd.read_csv(input_path, delimiter='\t')
print(df.shape)
weather_df = df.ix[:,['datetime','pr', 'max_tp', 'min_tp']]
print(weather_df.shape)

Frag = False
count = 0
rain_week = 0.
max_tp_ave = 0.
min_tp_ave =0.
max_count = 0
min_count = 0
weather_data = {'rain':[], 'max_tp':[], 'min_tp':[]}
for num, data in weather_df.iterrows():
    day = str(data['datetime'])[0:8]
    if day == '20120102' : #'20120102' : #2012年第1週は2日からなので
        Frag = True
    elif day == '20170327' : #'20170327' : #2017年第12週は26日までなので
        Frag = False
    if Frag :
        #if data['pr'] is not None :
        rain_week += data['pr']
        #if data['max_tp'] is not None :
        max_tp_ave += data['max_tp']
        max_count += 1
        #if data['min_tp'] is not None :
        min_tp_ave += data['min_tp']
        min_count += 1
        count += 1
        if count == 1008 :
            weather_data['rain'].append(rain_week)
            max_tp_ave = max_tp_ave/max_count
            min_tp_ave = min_tp_ave/min_count
            weather_data['max_tp'].append(max_tp_ave)
            weather_data['min_tp'].append(min_tp_ave)
            count = 0
            rain_week = 0.
            max_tp_ave = 0.
            min_tp_ave =0.
            max_count = 0
            min_count = 0

print(len(weather_data['rain']))
print(len(weather_data['max_tp']))
print(len(weather_data['min_tp']))

weather_df = pd.DataFrame(weather_data, columns=["rain","max_tp","min_tp"])
weather_df.to_csv(output_path)
