import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

path = "Temp/"

x_data = np.load(path+"x_data.npy")
y_data = np.load(path+"y_data.npy")

features = ["DATE", "COUNT", "ACT-COUNT", "WEIGHT", "STREN", "TM", "LL", "CPI", "WPI", "L", "W"]

mean_vec = np.mean(x_data, axis=0)
x_c = x_data - mean_vec

cov_mat = (x_data - mean_vec).T.dot((x_data - mean_vec)) / (x_data.shape[0]-1)

cov_df = pd.DataFrame(cov_mat, columns=features)
cov_df.insert(0, "Features", features)
print(cov_df)

eig_vals, eig_vecs = np.linalg.eig(cov_mat)
print('Eigenvectors \n%s' %eig_vecs)
print('\nEigenvalues \n%s' %eig_vals)

total = sum(eig_vals)
var_exp = [(i / total)*100 for i in sorted(eig_vals, reverse=True)]
print("\nExplained Variance of each principal component")
print(var_exp)

x = ["PC-{}".format(i) for i in range(1, len(eig_vals)+1)]
plt.bar(x, var_exp)
plt.savefig("PCA-Components.jpg")