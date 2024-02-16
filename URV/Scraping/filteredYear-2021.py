import pandas as pd
import datetime 
import matplotlib.pyplot as plt

df = pd.read_csv('Scraping/spp_test1.csv')
# C:\Users\glabo\OneDrive\Laptop\Desktop\URV\Scraping\URV-Ruth\cleaned_data3.csv
#print(df.head())
df['datetime'] = pd.to_datetime(df['datetime'])

sources = ['coal', 'gas', 'wind', 'hydro', 'nuclear', 'unknown', 'biomass', 'solar', 'oil']
total = df[sources].sum()

# plt.figure()
# plt.pie(total, labels=sources, autopct='%1.1f%%')
# plt.axis('equal')
# plt.legend(title = f'Sources')
# plt.show()


yearlist = ['2021', '2022', '2023']

for year in yearlist:
    year_df = df[df['datetime'].dt.year == int(year)]
    year_total = year_df[sources].sum()
    # labels=sources
    
    plt.figure()
    
    plt.pie(year_total, hatch = ['.', '\\', 'XX','o','O.'], wedgeprops = {"edgecolor" : "black", 
                      'linewidth': 1, 
                      'antialiased': True})
    # plt.axis('equal')
    percents = year_total.to_numpy() * 100 / year_total.to_numpy().sum()
    
    # plt.legend(title = f'Sources {year}',  labels=sources)
    # plt.legend( bbox_to_anchor=(1.35,1.1), loc='upper right',
    #         labels=['%s, %1.1f %%' % (l, s) for l, s in zip(year_total.index,percents)])

    # plt.legend(title = f'Sources_SPP_{year}',  labels=sources)

    # plt.show()

    savename = f'Scraping/Plots/SourceRatio_SPP_{year}'
    plt.tight_layout()
    plt.savefig(savename, dpi= 500)
    plt.clf()
    
    # plt.savefig(, dpi = 500)
    plt.close()
