import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

input_path = "./data/sfc/sfc_47662.tsv"

df = pd.read_csv(input_path, delimiter='\t')
print(df.shape)
weather_df = df.ix[:,['datetime','pr','lap','max_tp', 'rhm']]
print(weather_df.shape)

hour = '2012010100'
rain_hour = 0.
lap_ave = 0.
tp_ave = 0.
rhm_ave = 0.
weather_data = {'rain':[], 'lap':[], 'tp':[], 'rhm':[]}
for num, data in weather_df.iterrows():
    now = str(data['datetime'])[0:10]
    if now != hour :
        weather_data['rain'].append(rain_hour)
        lap_ave = lap_ave/6.
        tp_ave = tp_ave/6.
        rhm_ave = rhm_ave/6.
        weather_data['lap'].append(lap_ave)
        weather_data['tp'].append(tp_ave)
        weather_data['rhm'].append(rhm_ave)
        hour = now
        rain_hour = data['pr']
        lap_ave = data['lap']
        tp_ave = data['max_tp']
        rhm_ave = data['rhm']
    else:
        rain_hour += data['pr']
        lap_ave += data['lap']
        tp_ave += data['max_tp']
        rhm_ave += data['rhm']
#20170331の分
weather_data['rain'].append(rain_hour)
lap_ave = lap_ave/6.
tp_ave = tp_ave/6.
rhm_ave = rhm_ave/6.
weather_data['lap'].append(lap_ave)
weather_data['tp'].append(data['max_tp'])
weather_data['rhm'].append(rhm_ave)

### グラフ
plt.scatter(weather_data['tp'], weather_data['rain'], s=1)#, c=weather_data['rhm'], cmap='Blues')
#plt.colorbar()
plt.show()
