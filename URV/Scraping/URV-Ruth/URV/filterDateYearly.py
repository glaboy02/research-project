import pandas as pd
import datetime
import matplotlib.pyplot as plt

# copied from other group, modified to fit our region data


df = pd.read_csv("carbonemissions/avgCO2Intensity.csv")

#print(df.head())

df['datetime'] = pd.to_datetime(df['datetime'])

grouped_df = df.groupby(df['datetime'].dt.year)['totalAVGIntensity']

#print(grouped_df.groups.keys())

mean_df = grouped_df.mean()

std_df = grouped_df.std()

print(mean_df)

mean_df.plot.bar(yerr= std_df, capsize = 4)
plt.xticks(rotation = 360)


savename = 'plots/Yearly'

plt.savefig(savename)

plt.close()