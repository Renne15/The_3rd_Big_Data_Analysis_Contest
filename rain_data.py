import pandas as pd

input_path = "./data/sfc/sfc_47662.tsv"
output_path = "./data/rain_data.csv"

df = pd.read_csv(input_path, delimiter='\t')
print(df.shape)
pr = df.ix[:,[0,1]]
print(pr.shape)

day = '20120101'
rain_sum = 0
rain_data = {}
for num, data in pr.iterrows():
    today = str(data['datetime'])[0:8]
    if today != day :
        rain_data[day] = rain_sum
        day = today
        rain_sum = data['pr']
    else:
        rain_sum += data['pr']
rain_data[day] = rain_sum #20170331の分

rain_df = pd.DataFrame(rain_data, index=['Rain'])
rain_df = rain_df.T
print(rain_df)
rain_df.to_csv(output_path)
