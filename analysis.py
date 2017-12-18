import pandas as pd
import csv

input_path_rain = "./data/rain_data.csv"
input_path_exchange = "./data/exchange_USDJPY.csv"
output_path = "./data/output.csv"

data = {}
with open(input_path_rain,'r') as rain_csv :
    rain_data = csv.reader(rain_csv)
    header = next(rain_data)
    for rain in rain_data :
        if rain[2] != '' :
            data[rain[0]] = [float(rain[1]),float(rain[2])]
        else:
            data[rain[0]] = [float(rain[1])]

with open(input_path_exchange,'r') as exchange_csv :
    exchange_data = csv.reader(exchange_csv)
    header = next(exchange_data)
    for exchange in exchange_data :
        data[exchange[0]].append(float(exchange[1]))

data_mk2 = {}
for day, value in data.items() :
    if len(value) == 3 :
        data_mk2[day] = value

data_df = pd.DataFrame(data_mk2, index=['Rain','Lap','Diff'])
data_df = data_df.T
print(data_df)
data_df.to_csv(output_path)
