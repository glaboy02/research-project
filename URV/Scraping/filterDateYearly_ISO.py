import pandas as pd
import datetime
import matplotlib.pyplot as plt


# df = pd.read_csv('spp_test7.csv', index_col='datetime').rename_axis(None)

# print(df.head())

# Scraping\spp_test7.csv

df = pd.read_csv('Scraping/ISO_test.csv')

print(df.head())

df['datetime'] = pd.to_datetime(df['datetime'])

grouped_df = df.groupby(df['datetime'].dt.year)['totalAVGIntensity']

print(grouped_df.groups.keys())

mean_df = grouped_df.mean()


std_df = grouped_df.std()

print(mean_df)

mean_df.plot.bar(yerr= std_df, capsize = 4, color='#3B5B92')
plt.xticks(rotation = 360)
plt.tick_params(left = False, bottom = False)
plt.ylabel(r'Average Carbon Intensity (g.CO$_2$eq/kWh)',fontsize = 10)
plt.xlabel(r'Year',fontsize = 10)
plt.ylim([0,600])

# mean_df.plot.pie(yerr = std_df,autopct='%1.1f%%')


savename = 'Scraping/Plots/Yearly_ISO'

plt.savefig(savename)

plt.close()
