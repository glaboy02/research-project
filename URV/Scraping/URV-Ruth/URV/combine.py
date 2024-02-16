import os
import pandas as pd

# this file combines the data from the rawdata21 folder, which has all 3 years (even though it has 21 in the title lol)

directory_name = "rawdata21"
files = os.listdir(directory_name)

files.sort()
new_df = pd.DataFrame()

for file in files:
    abs_file_path = os.path.join(directory_name, file)
    df = pd.read_csv(abs_file_path)
    new_df = pd.concat([new_df, df])


filename = f"combinedfiles/rawdata.csv"
new_df.to_csv(filename, index=False)