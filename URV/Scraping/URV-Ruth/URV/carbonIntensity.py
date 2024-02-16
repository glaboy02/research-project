import pandas as pd
import datetime 

# stuff we copied from the other group and modified to fit our region

df = pd.read_csv("combinedfiles/cleaned_data3.csv")

# gets data from mW to kW
df['coal'] *=1000
df['gas'] *=1000
df['wind'] *=1000
df['hydro'] *=1000
df['nuclear'] *=1000
df['unknown'] *=1000
df['biomass'] *=1000
df['solar'] *=1000
df['oil'] *=1000

# creates 2 data frames
df2 = df
df3 = df
df2 = df2.drop('datetime', axis=1)
df3 = df3.drop('datetime', axis=1)


# print(df2['nuclear'])
# exit()


# multiply by ISO NE carbon intensity values
df2['coal'] *=1141
df2['gas'] *=508
df2['wind'] *=11
df2['hydro'] *=24
df2['nuclear'] *=12
df2['unknown'] *=700
df2['biomass'] *=277
df2['solar'] *=28
df2['oil'] *=1026
# print(df3['nuclear'])
# print(df2['nuclear'])
# print(df['nuclear'])

# gives dataframe 
df2.to_csv("carbonemissions/CO2conversions.csv", index = False)

# exit()

# new_df['nuclear'] = df['nuclear']*12

# print(new_df['nuclear'])

# print(new_df['nuclear'])
# x = df['nuclear'].sum()
# print(x)
# intensity_df = df2['nuclear'].sum()
# x = df['nuclear'].sum()
# print(intensity_df)
# print(x)
# print(intensity_df/x)

# intensity_df2 = df2.sum(axis = 1)
# x2 = df3.sum(axis = 1)
# intensity_df3 = intensity_df2.sum()
# y =x2.sum()
# print(intensity_df3)
# print(y)

# print(intensity_df3/y)

# gives average intensity of carbon emissions (mean)
intensity_df4 = df2.sum(axis = 1)/df3.sum(axis = 1)
print(intensity_df4)
# /df.sum(axis = 1)
#exit()


##df4 = df
# print(df4)

##df4['totalAVGIntensity'] = intensity_df4

# intensity_df4.to_csv('spp_test4.csv', index = False)


##intensity_df4['datetime'] = pd.to_datetime(intensity_df4['datetime'])

# creates carbon emissions column in original data frame
df['totalAVGIntensity'] = intensity_df4
#df['datetime'] = pd.to_datetime(df['datetime'])


# avg_intensity_2021 = df[df['datetime'].dt.year == 2021]

##avg_intensity_2021 = df4[df4['datetime'].dt.year == 2021]
# print(avg_intensity_2021)

# print(intensity_df4['datetime'])

df.to_csv("carbonemissions/avgCO2Intensity.csv", index = False)