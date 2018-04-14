import pandas as pd

dia19=pd.read_csv('k_Dia_19.csv')
dia20=pd.read_csv('k_Dia_20.csv')
dia21=pd.read_csv('k_Dia_21.csv')
dia22=pd.read_csv('k_Dia_22.csv')
dia23=pd.read_csv('k_Dia_23.csv')
result = pd.concat([dia19,dia20,dia21,dia22,dia23],ignore_index=True)
result.drop('Unnamed: 0',1,inplace=True)
result.to_csv('k_Dia_19-23.csv',sep=',')
