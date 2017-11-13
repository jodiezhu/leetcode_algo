import pandas as pd
import missingno as msno
import matplotlib.pyplot as plt
import numpy as np

df=pd.read_csv("C:/Users/jodie.zhu/Desktop/Book1.csv")
df.columns=["Time","Age","Sex","Health","Education","Income","Employment","Address",
                            "Travel_distance","Commute_time","Transportation","Vehicle","Support_sts",
                            "Multi_use_tails","Multi_use_tails_speed","collision","punishment","Multi_use_tails_pedal",
                            "bike_lane","bike_lane_pedal","sidewalk","Bylaw"]
#print(df.shape)
print(df.info())
#msno.heatmap(df)
#print(df["Vehicle"].unique())

keyword1 = ['yes','car','cars','motorcycle','atv','motor','truck']
keyword2 = ['share','rental','sharing','zip','Car2Go','Cars2Go',"borrow","rent",'carshare']
pat1 = '|'.join(keyword1)
pat2 = '|'.join(keyword2)

df['Response'] = pd.np.where(df['Vehicle'].str.lower().str.contains(pat1), 1, 0)
df['Response'] [df['Vehicle'].str.lower().str.contains(pat2)]=0

#one-way frequency table
my_tab = pd.crosstab(index=df['Response'],columns="count") 

#2-way frequency table
survived_sex = pd.crosstab(index=df['Response'], columns=df["Travel_distance"])
print(survived_sex)
#df.to_csv('C:/Users/jodie.zhu/Desktop/test.csv', index=False)
