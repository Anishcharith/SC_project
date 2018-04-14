import pandas as pd
import numpy as np
'''
xls_data=pd.ExcelFile("COUNT DETAILS 40s -velmurugan for feature selection.xls")
sheet2=xls_data.parse('k Dia 19')
parsed=pd.DataFrame()
sheet=[]
print(sheet2['Unnamed: 1'][2])
for j in range(1,len(sheet2.columns)):
    temp=[]
    for i in range(3,len(sheet2)):
        temp.append(sheet2['Unnamed: '+str(j)][i])
    parsed[sheet2['Unnamed: '+str(j)][2]]=pd.Series(temp[:])
parsed.drop(["Req GSM","Gauge"],axis=1,inplace=True)
gg=sheet2['Unnamed: 13'][0]
noneedles=sheet2['Unnamed: 15'][0]
kdia=sheet2['Unnamed: 11'][0]
gsm=sheet2['Unnamed: 9'][0]
tpi=sheet2['Unnamed: 7'][0]
parsed.insert(2,'GSM',np.zeros(len(parsed))+gsm)
parsed.insert(4,'GG',np.zeros(len(parsed))+gg)
parsed.insert(5,'TPI',np.zeros(len(parsed))+tpi)
parsed.insert(6,'No of Needles',np.zeros(len(parsed))+noneedles)
print(parsed.head())
parsed.to_csv('k_Dia_19.csv',sep=',')
'''

xls_data=pd.ExcelFile("COUNT DETAILS 40s -velmurugan for feature selection.xls")
sheet2=xls_data.parse('k Dia 23')
parsed=pd.DataFrame()
sheet=[]
print(sheet2['Unnamed: 1'][2])
for j in range(1,len(sheet2.columns)):
    temp=[]
    for i in range(3,len(sheet2)):
        temp.append(sheet2['Unnamed: '+str(j)][i])
    parsed[sheet2['Unnamed: '+str(j)][2]]=pd.Series(temp[:])
gg=sheet2['Unnamed: 10'][0]
noneedles=sheet2['Unnamed: 12'][0]
kdia=sheet2['Unnamed: 8'][0]
gsm=sheet2['Unnamed: 6'][0]
tpi=sheet2['Unnamed: 4'][0]
parsed.insert(2,'GSM',np.zeros(len(parsed))+gsm)
parsed.insert(3,'K.Dia',np.zeros(len(parsed))+kdia)
parsed.insert(4,'GG',np.zeros(len(parsed))+gg)
parsed.insert(5,'TPI',np.zeros(len(parsed))+tpi)
parsed.insert(6,'No of Needles',np.zeros(len(parsed))+noneedles)
print(parsed.head())
parsed.to_csv('k_Dia_23.csv',sep=',')
