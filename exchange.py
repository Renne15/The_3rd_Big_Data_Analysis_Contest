import pandas as pd

input_path = "./data/exchange/USDJPY_del_header.csv"
output_path = "./data/exchange_USDJPY.csv"

df = pd.read_csv(input_path)
df.columns = ['Date','Open','High','Low','Close']
#print(df)
print(df.shape)

day = '2012/01/03'
day_close = '2017/03/31'
day_frag = False
exchange_data = {}
for num, data in df.iterrows():
    today = data['Date'][0:10]
    if today == day_close :
        today = today.replace('/','')
        exchange_data[today] = data['Close'] - data['Open']
        break
    elif today == day :
        today = today.replace('/','')
        exchange_data[today] = data['Close'] - data['Open']
        day_frag = True
    elif day_frag :
        today = today.replace('/','')
        exchange_data[today] = data['Close'] - data['Open']

exchange_df = pd.DataFrame(exchange_data, index=['Diff'])
exchange_df = exchange_df.T
print(exchange_df)
exchange_df.to_csv(output_path)
