import pandas as pd
import os

folder = "C:\\Users\\glabo\\OneDrive\\Desktop\\URV\\Scraping\\rawData"

all_dfs = []
for file in os.listdir(folder):
    read = pd.read_csv(folder + '\\'+ file)
    all_dfs.append(read)
    
    
# spp = pd.read_csv('rawData/spp_20231231.csv')
# print(spp)
# print(len(all_dfs))

# print(all_dfs)
combine = pd.concat(all_dfs)
# print(combine.shape)
combine.to_csv('spp_combined.csv', index = False)