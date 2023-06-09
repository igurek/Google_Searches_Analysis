# -*- coding: utf-8 -*-
"""Data_Sci_Searches.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15oNyekmek7NZ3EfiyWsF_noJzrrgIDse
"""

pip install pytrends

import pandas as pd
from pytrends.request import TrendReq
import matplotlib.pyplot as plt
trends = TrendReq()

trends.build_payload(kw_list=["Data Science"])
data = trends.interest_by_region()
data = data.sort_values(by="Data Science", ascending=False)
data = data.head(10)
print(data)

data.reset_index().plot(x="geoName", 
                        y="Data Science", 
                        figsize=(15,12), kind="bar")
plt.style.use('fivethirtyeight')
plt.show()

data = TrendReq(hl='en-US', tz=360)
data.build_payload(kw_list=['Data Science'])
data = data.interest_over_time()
fig, ax = plt.subplots(figsize=(15, 12))
data['Data Science'].plot()
plt.style.use('fivethirtyeight')
plt.title('Total Google Searches for Data Science', 
          fontweight='bold')
plt.xlabel('Year')
plt.ylabel('Total Count')
plt.show()

