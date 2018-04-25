import csv
import numpy as np

from sklearn import preprocessing
path = "Dataset/"
savepath = "Temp/"

data_raw = [];

with open(path+"k_Dia_19-23.csv",'r',encoding = "utf8") as f:
	for l in  csv.reader(f, quotechar='"', delimiter=',', quoting=csv.QUOTE_ALL, skipinitialspace=True):
			data_raw.append(l)

del data_raw[0]


data_raw = np.array(data_raw)

date = data_raw[:,1]
min_date = np.datetime64(min(date))
max_date = np.datetime64(max(date))

date = np.array([(np.datetime64(x) - min_date)*1.0/(max_date - min_date) for x in date])


le = preprocessing.LabelEncoder()
le.fit(data_raw[:,2])
count = le.transform(data_raw[:,2])
print(count)

x_data = np.column_stack((count, np.float64(data_raw[:,4]), np.float64(data_raw[:,7:15])))
y_data = np.float64(data_raw[:,-1])


x_data = preprocessing.scale(x_data)

x_data = np.column_stack((date, x_data))

np.save(savepath+"x_data_.npy",x_data)
np.save(savepath+"y_data_.npy",y_data)
