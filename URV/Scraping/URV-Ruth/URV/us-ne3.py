import pandas as pd
import numpy as np
from datetime import datetime
import requests
from io import StringIO
from xml import etree

start_date = datetime.strptime('2021-01-01', "%Y-%m-%d")
end_date = datetime.strptime('2023-12-31', "%Y-%m-%d")

datelist = pd.date_range(start_date, end_date, freq="D").strftime("%Y%m%d")
# print(datelist)
# based_df = pd.DataFrame({'Interval': datelist})

baseurl = "https://webservices.iso-ne.com/api/v1.1/genfuelmix/day"
username = "meganwong@umass.edu"
password = "RuthBarasa"

for d in datelist:
    url = f"{baseurl}/{d}"
    r = requests.get(url, auth=(username, password))
    if r.status_code == 200:
        xml_data = StringIO(r.text)
        df = pd.read_xml(xml_data)
        
        filename = f"rawdata21/nesio_{d}.csv"
        df.to_csv(filename, index=False)
        # checks that the file is rendered successfully
        print(filename)
        pass
    else:
        # checks if there's a missing date in the data that needs to be filled
        print(d)