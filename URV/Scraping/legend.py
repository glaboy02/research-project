import pandas as pd
import datetime 
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('Scraping/spp_test1.csv')
#print(df.head())
df['datetime'] = pd.to_datetime(df['datetime'])

sources = ['coal', 'gas', 'wind', 'hydro', 'nuclear', 'unknown', 'biomass', 'solar', 'oil']
total = df[sources].sum()

yearlist = ['2021', '2022', '2023']

for year in yearlist:
    year_df = df[df['datetime'].dt.year == int(year)]
    year_total = year_df[sources].sum()

    plt.figure()
    plt.pie(year_total)
    plt.axis('equal')
    #plt.legend(sources, frameon = False)

    #plt.show()

    # savename = f'Scraping/Plots/So.png'
    # plt.savefig(savename)
    plt.close()


f = lambda m, c: plt.plot([],[],marker=m, color=c, ls="none")[0]
palette = sns.color_palette("deep", n_colors=len(sources))
handles = [f("s", palette[i]) for i in range(len(sources))]
labels = sources
legend = plt.legend(handles, labels, loc='center', frameon=False)

fig  = legend.figure
fig.canvas.draw()
bbox  = legend.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
fig.savefig("Scraping/Plots/legend.png", dpi=500, bbox_inches=bbox)

#plt.show()
plt.close()
