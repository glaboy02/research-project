import pandas as pd
from datetime import datetime

# this file cleans the data

filename = f"combinedfiles/rawdata.csv"
df = pd.read_csv(filename)

start_date = datetime.strptime('2021-01-01', "%Y-%m-%d")
end_date = datetime.strptime('2023-12-31', "%Y-%m-%d")

datelist = pd.date_range(start_date, end_date, freq="D").strftime("%Y%m%d")
df['BeginDate'] = df['BeginDate'].str.slice(stop = -6)
df['BeginDate'] = pd.to_datetime(df['BeginDate'])

df['BeginDate'] = df['BeginDate'].astype(str)
df[['date', 'time']] = df['BeginDate'].str.split(" ", expand=True)

df[['hour', 'min', 'sec']] = df['time'].str.split(":", expand=True)
group_date = df.groupby('date')

# new dataframe for the cleaned data
new_df = pd.DataFrame(columns=['datetime', 'Coal', 'Natural Gas', 'Wind', 'Hydro', 'Nuclear', 'Other', 'Biomass', 'Solar', 'Oil', 'Renewables'])
new_df['datetime'] = df['date'] + " " + df['hour'] + ":00:00"
new_df = new_df.groupby('datetime').sum().reset_index()


# group by fuel category again, and specify wind and solar so that you can get data for wind and solar renewable energy

for day in group_date.groups.keys():
    day_df = group_date.get_group(day)
    group_hour = day_df.groupby('hour')
    for hour in group_hour.groups.keys():
        hour_df = group_hour.get_group(hour)
        group_fuel = hour_df.groupby('FuelCategoryRollup')
        group_category = hour_df.groupby('FuelCategory')
        for fuel in group_fuel.groups.keys():
            for category in group_category.groups.keys():
                fuel_df = group_fuel.get_group(fuel)
                category_df = group_category.get_group(category)

                # sums the generation mix for each fuel category at that hour
                summed_mix = fuel_df['GenMw'].values.sum()
                # updates the new dataframe with the summed generation mix at the specific index of the datetime and fuel category
                new_df.loc[(new_df['datetime'] == day + " " + hour + ":00:00"), fuel] = summed_mix

                if fuel == 'Renewables' and category == 'Solar':
                    summed_mix3 = category_df['GenMw'].values.sum()
                    new_df.loc[(new_df['datetime'] == day + " " + hour + ":00:00"), 'Solar'] = summed_mix3
                    
                if fuel == 'Renewables' and category == 'Wind':
                    summed_mix2 = category_df['GenMw'].values.sum()
                    new_df.loc[(new_df['datetime'] == day + " " + hour + ":00:00"), 'Wind'] = summed_mix2
                    
                
        
# based dataframe
datetime_list = pd.DataFrame()
datetime_list['datetime'] = pd.date_range(start_date, datetime(2023, 12, 31, 23, 0, 0), freq="H").strftime("%Y-%m-%d %H:00:00")

# merge the two dataframes
merged_df = pd.merge(datetime_list, new_df, on='datetime', how='left')
merged_df = merged_df.ffill().bfill()

mapper = {
    'datetime': 'datetime',
    'Coal': 'coal',
    'Natural Gas': 'gas',
    'Wind': 'wind',
    'Hydro': 'hydro',
    'Nuclear': 'nuclear',
    'Other': 'unknown',
    'Biomass': 'biomass',
    'Solar': 'solar',
    'Oil': 'oil',
    'Renewables': 'renewables'
}

merged_df.rename(columns=mapper, inplace=True)

filename = f"combinedfiles/cleaned_data3.csv"
merged_df.to_csv(filename, index=False)