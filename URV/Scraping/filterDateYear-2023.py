import pandas as pd
import datetime
import matplotlib.pyplot as plt


# df = pd.read_csv('spp_test7.csv', index_col='datetime').rename_axis(None)

# print(df.head())

df = pd.read_csv('Scraping/spp_test7.csv')

# print(df.head())

df['datetime'] = pd.to_datetime(df['datetime'])
avg_intensity_2023 = df[df['datetime'].dt.year == 2023]
print(avg_intensity_2023)

grouped_df = avg_intensity_2023.groupby(df['datetime'].dt.month)['totalAVGIntensity']
print(grouped_df.groups.keys())

mean_df = grouped_df.mean()


std_df = grouped_df.std()

print(mean_df)

mean_df.plot.bar(yerr= std_df, capsize = 4)
plt.xticks(rotation = 360)

# mean_df.plot.pie(yerr = std_df,autopct='%1.1f%%')


savename = 'Scraping/Plots/Yearly-Monthly-2023'

plt.savefig(savename)

plt.close()
exit()
