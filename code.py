# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
path
data = pd.read_csv(path)
data.rename(columns={'Total':'Total_Medals'},inplace=True)
print(data.head())
#Code starts here



# --------------
#Code starts here
data['Better_Event'] = np.where(data['Total_Summer'] > data['Total_Winter'] , 'Summer', 'Winter')
data['Better_Event'] =np.where(data['Total_Summer'] ==data['Total_Winter'],'Both',data['Better_Event'])
better_event =data['Better_Event'].value_counts().index.values[0]
print(better_event)



# --------------
#Code starts here
top_countries = data[['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']]

top_countries.drop(top_countries.index[-1],inplace=True)
#print(top_countries)
def top_ten(top_countries,col_name):
    country_list =[]
    top_10 =top_countries.nlargest(10,col_name)
   # print(top_10)
    country_list=list(top_10['Country_Name'])
    return country_list

top_10_summer=[]
top_10_summer=top_ten(top_countries,'Total_Summer')
print(top_10_summer)

top_10_winter=[]
top_10_winter=top_ten(top_countries,'Total_Winter')

top_10=[]
top_10=top_ten(top_countries,'Total_Medals')

# def common_elements(top_10,top_10_summer,top_10_winter):
#     for elements in top_10:
#         if elements in top_10_summer:
#             if elements in top_10_winter:
#                 return elements


# common =list(common_elements(top_10,top_10_summer,top_10_winter))
common = list(set(top_10)&set(top_10_summer)&set(top_10_winter))
print(common)





# --------------
#Code starts here

summer_df = data[data['Country_Name'].isin(top_10_summer)]
winter_df = data[data['Country_Name'].isin(top_10_winter)]
top_df =data[data['Country_Name'].isin(top_10)]


summer_df[['Country_Name','Total_Summer']].plot(kind='bar')
plt.show()

winter_df[['Country_Name','Total_Winter']].plot(kind='bar')
plt.show()

top_df[['Country_Name','Total_Medals']].plot(kind='bar')
plt.show()


# --------------
#Code starts here
summer_df['Golden_Ratio']=summer_df['Gold_Summer']/summer_df['Total_Summer'] 
summer_max_ratio=summer_df.loc[summer_df['Golden_Ratio'].idxmax(),'Golden_Ratio']
summer_country_gold=summer_df.loc[summer_df['Golden_Ratio'].idxmax(),'Country_Name']
#print(summercountrygold)

winter_df['Golden_Ratio']=winter_df['Gold_Winter']/winter_df['Total_Winter'] 
winter_max_ratio=winter_df.loc[winter_df['Golden_Ratio'].idxmax(),'Golden_Ratio']
winter_country_gold=winter_df.loc[winter_df['Golden_Ratio'].idxmax(),'Country_Name']

top_df['Golden_Ratio']=top_df['Gold_Total']/top_df['Total_Medals'] 
top_max_ratio=top_df.loc[top_df['Golden_Ratio'].idxmax(),'Golden_Ratio']
top_country_gold=summer_df.loc[top_df['Golden_Ratio'].idxmax(),'Country_Name']


# --------------
#Code starts here
data_1 = data
data_1.drop(data_1.index[-1],inplace=True)
#print(data_1)

data_1['Total_Points']= (data_1['Gold_Total']*3)+(data_1['Silver_Total']*2)+data_1['Bronze_Total']

most_points = data_1.loc[data_1['Total_Points'].idxmax(),'Total_Points']
best_country = data_1.loc[data_1['Total_Points'].idxmax(),'Country_Name']
print(most_points)


# --------------
#Code starts here

best = data_1[data_1['Country_Name']==best_country]

best = best[['Gold_Total','Silver_Total','Bronze_Total']]

best.plot.bar()

plt.xlabel('United States')
plt.ylabel('Medals Tally')
plt.xticks(rotation = 45)


