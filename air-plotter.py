'''
You have been provided with ‘leeds-central-air-quality.csv’ which is a file containing air quality data for Leeds from the last few years. There are 4 values – particulate matter (25), particulate matter (10), Ozone and Nitrous Oxide which are all different measures of air quality – which are recorded against the date.
Load this file into a suitable data structure.

From this data, create a line plot of the average of the 4 data points against the date.

For example, for the row:
07/09/2024,68,20,25,5

You would plot a point at (68+20+25+5)/4 = 29.5

The X-axis should be the date, the Y-axis should be the average pollution.
'''
import pandas as pd
import matplotlib.pyplot as plt
base_infor=pd.read_csv("leeds-centre-air-quality")
base_infor["date"]=pd.datetime(base_infor["date"], dayfirst=True)
pollution=["pm25", "pm10", "o3", "no2"]
base_infor["average_pollution"]=base_infor[pollution].mean(axis=1)
plt.figure(figsize(12,5))
plt.plot(base_infor["date"], base_infor["average_pollution"])
plt.xlabel("date")
plt.ylabel("average pollution")
plt.title("Leeds centre air quality by 刘智嘉(Liu Zhijia)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()