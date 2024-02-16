import pandas as pd
import datetime
import matplotlib.pyplot as plt


# df = pd.read_csv('spp_test7.csv', index_col='datetime').rename_axis(None)

# print(df.head())

df = pd.read_csv('Scraping/spp_test7.csv')

# print(df.head())

df['datetime'] = pd.to_datetime(df['datetime'])
avg_intensity_2021 = df[df['datetime'].dt.year == 2021]
print(avg_intensity_2021)

grouped_df = df.groupby(df['datetime'].dt.month)['totalAVGIntensity']
print(grouped_df.groups.keys())

mean_df = grouped_df.mean()


std_df = grouped_df.std()

print(mean_df)

mean_df.plot.bar(yerr= std_df, capsize = 4, color = '#BABABA')
plt.xticks(rotation = 360)
plt.tick_params(left = False, bottom = False)
plt.ylabel(r'Average Carbon Intensity (g.CO$_2$eq/kWh)',fontsize = 10)
plt.xlabel(r'Month',fontsize = 10)
plt.ylim([0,600])

# mean_df.plot.pie(yerr = std_df,autopct='%1.1f%%')


savename = 'Scraping/Plots/Yearly-Monthly-2021_SPP'

plt.savefig(savename)

plt.close()
exit()

