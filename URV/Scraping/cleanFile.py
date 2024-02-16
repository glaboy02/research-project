import pandas as pd
import datetime


df = pd.read_csv('spp_combined.csv')
# print(df)
# print(df[' Hydro'])
# exit()
datetime_col = df['GMT TIME']
datetime_col = datetime_col.str.replace("T", " ")
datetime_col = datetime_col.str.replace("Z", "")
# print(datetime_col)
# print(df)

df['GMT TIME'] = pd.to_datetime(datetime_col)

# print(df)
df.columns = [c.strip() for c in df.columns]

df['Coal'] = df['Coal Market'] + df['Coal Self']
df['Unknown'] = df['Waste Disposal Services'] + df['Waste Heat'] + df['Other']
df['Biomass'] = 0.0

df = df[['GMT TIME', 'Coal', 'Coal Market', 'Coal Self', 'Natural Gas', 'Wind', 'Hydro',  'Nuclear',  'Waste Disposal Services',  'Waste Heat', 'Other', 'Unknown', 'Biomass', 'Solar','Diesel Fuel Oil']]

df = df.drop(['Coal Market', 'Coal Self', 'Waste Disposal Services', 'Waste Heat', 'Other'], axis = 1)

formatted_column_names = {'GMT TIME': 'datetime', 'Coal': 'coal', 'Natural Gas': 'gas', 'Wind': 'wind', 'Hydro': 'hydro', 'Nuclear': 'nuclear', 'Unknown': 'unknown', 'Biomass':'biomass', 'Solar': 'solar', 'Diesel Fuel Oil':'oil'}
df.rename(columns=formatted_column_names, inplace=True)

start_date = datetime.datetime.strptime('2021-01-01', '%Y-%m-%d')
end_date = datetime.datetime.strptime('2024-01-01', '%Y-%m-%d')

datelist = pd.date_range(start_date, end_date, freq='H', inclusive='left')
print(len(datelist))
based_df = pd.DataFrame({'datetime': datelist})

# print(based_df)

based_df['datetime'] = pd.to_datetime(based_df['datetime'])

combined_df = pd.merge(based_df, df, on='datetime', how='left')
# print(combined_df)
combined_df = combined_df.ffill().bfill()
print(combined_df.shape[0])

#print(combined_df)
#
# print(combined_df['hydro'])

# exit()

# df.to_csv('spp_cleaned5.csv', index = False)
combined_df.to_csv('spp_test1.csv', index= False)