import pandas as pd
import datetime
import matplotlib.pyplot as plt

# df = pd.read_csv('spp_test7.csv', index_col='datetime').rename_axis(None)

df = pd.read_csv('Scraping/spp_test7.csv')

#print(df.head())

df['datetime'] = pd.to_datetime(df['datetime'])

yearlist = ['2021', '2022', '2023']

for year in yearlist:
    year_df = df[df['datetime'].dt.year == int(year)]
    grouped_df = year_df.groupby(df['datetime'].dt.month)['totalAVGIntensity']

    mean_df = grouped_df.mean()
    std_df = grouped_df.std()
    
    #print(year_df)
    #print(grouped_df)
    #print(mean_df)
    fig, ax = plt.subplots(1,1, figsize=(5,4))
    mean_df.plot.bar(yerr=std_df, capsize=4,ax=ax, color='#BABABA')
    plt.xticks(rotation=360)
    plt.tick_params(left = False, bottom = False)
    plt.ylabel(r'Average Carbon Intensity (g.CO$_2$eq/kWh)',fontsize = 10)
    plt.xlabel(r'Month',fontsize = 10)
    plt.ylim([0,600])
    
    savename = f'Scraping/Plots/Monthly_{year}v2'
    plt.savefig(savename, dpi = 500)
    plt.close()
