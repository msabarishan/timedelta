from datetime import timedelta,datetime
import pandas as pd
#  Provides todays date
today = datetime.now() 
# Provides yesterdays date
yesterday= today-timedelta(1)
# yes_str will be in 25_June_2022 format
yes_str = yesterday.strftime("%d_%m_%Y")
# Passing the date string while reading file using pandas
df = pd.read_excel(f'./finance_{yes_str}.xlsx')
