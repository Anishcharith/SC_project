import pandas as pd
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
print(parsed.head())
parsed.to_csv('k_Dia_19.csv',sep=',')
