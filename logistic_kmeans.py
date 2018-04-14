import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

from sklearn.metrics import mean_squared_error, r2_score


path = "Temp/"


n_classes = 11


x_data = np.load(path+"x_data.npy")
y_data = np.load(path+"y_data.npy")


y_data = y_data.reshape(-1,1)
kmeans = KMeans(n_clusters = n_classes)
kmeans.fit(y_data)
y_data = kmeans.fit_predict(y_data)



x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size=0.33)


clf = LogisticRegression(solver = 'lbfgs',multi_class = 'multinomial')

clf.fit(x_train, y_train)

y_pred = clf.predict(x_test)
print("No PCA")

print("Mean squared error: ", mean_squared_error(y_test, y_pred))

print("Variance score: ", r2_score(y_test, y_pred))

for i in range(np.shape(x_data)[1]-1):
	pca = PCA(n_components = i+1)
	pca.fit(x_train)
	x_pca_train = pca.transform(x_train)
	x_pca_test = pca.transform(x_test)
	
	clf = LogisticRegression(solver = 'lbfgs',multi_class = 'multinomial')

	clf.fit(x_pca_train, y_train)

	y_pred = clf.predict(x_pca_test)
	print("\nPCA with n_components = ",i+1)

	print("Mean squared error: ", mean_squared_error(y_test, y_pred))

	print("Variance score: ", r2_score(y_test, y_pred))

