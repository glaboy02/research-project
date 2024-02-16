import datetime
import requests

import pandas as pd

start_date = datetime.datetime.strptime('20210101', "%Y%m%d")
end_date = datetime.datetime.strptime('20240101', "%Y%m%d")

baseurl = f"https://portal.spp.org"


datelist = pd.date_range(start_date, end_date, freq="D", inclusive='left').strftime("%Y%m%d")
# print(datelist)
# #datelist = pd.date_range(start_date, end_date, freq="D")
# exit()


for dt in datelist:
    
    formatted_date = dt
    formatted_month = formatted_date[4:6]
    formatted_year = formatted_date[0:4]
    formatted_day = formatted_date[6:9]

    # print(formatted_year)
    # print(formatted_month)
    # print(formatted_day)
    # exit()

    # print(datelist.year[count])
    # print(datelist.month[count])
    # print(formatted_date)
    if(formatted_year == 2021):
        url = f"{baseurl}/file-browser-api/download/hourly-generation-capacity-by-fuel-type?path=%2F{formatted_year}%2F{formatted_year}.zip"
    else:
        url = f"{baseurl}/file-browser-api/download/hourly-generation-capacity-by-fuel-type?path=%2F{formatted_year}%2F{formatted_month}%2FHRLY-GEN-CAP-BY-FUEL-TYPE-{formatted_date}.csv"
    # https://portal.spp.org/file-browser-api/download/hourly-generation-capacity-by-fuel-type?path=%2F2021%2F2021.zip
    
    try: 
        r = requests.get(url)
        fileName = f"rawData/spp_{dt}.csv"
        

        with open (fileName, 'w') as f:
            
            f.write(r.text)
            f.close
            
        # print(r)
    except:
        print(dt)

    

                   
# url = f"{baseurl}/file-browser-api/download/hourly-generation-capacity-by-fuel-type?path=%2F{datelist.year}%2F{datelist.month}%2FHRLY-GEN-CAP-BY-FUEL-TYPE-{str(datelist.year) + str(datelist.month) + str(datelist.day)}.csv"
# r = requests.get(url)
# print(r.text)

# print(datelist)
# print(start_date.year)
# print(str(datelist.year) + str(datelist.month) + str(datelist.day))



# month = 0
# day = 1


# month = format(x,"02")
# day = format(y, "02")
# sampleday = f"2022{month}07"



# print(sampleday)

# print(day)

# sampleday = f"2022{month}07"

# datelist = pd.date_range(start_date, end_date, freq="M", inclusive='left').strftime("%H:%M:%S")

# # datelist = pd.date_range(start_date, end_date, freq="D")

# url = f"{baseurl}/file-browser-api/download/hourly-generation-capacity-by-fuel-type?path=%2F2022%2F{month}%2FHRLY-GEN-CAP-BY-FUEL-TYPE-{sampleday}.csv"
# r = requests.get(url)
# print(len(datelist))