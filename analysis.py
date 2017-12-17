import pandas as pd
import csv

input_path_rain = "./data/rain_data.csv"
input_path_exchange = "./data/exchange_USDJPY.csv"

with open(input_path_rain,'r') as rain_csv :
    rain_data = csv.reader(rain_csv)
    header = next(rain_data)
    for rain in rain_data :
        print(rain)

with open(input_path_exchange,'r') as exchange_csv :
    exchange_data = csv.reader(exchange_csv)
    header = next(exchange_data)
    for exchange in exchange_data :
        print(exchange)
