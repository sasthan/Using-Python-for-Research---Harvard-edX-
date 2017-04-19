import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pylab

whisky = pd.read_csv("whiskies.txt")

whisky["Region"] = pd.read_csv("regions.txt")

flavors = whisky.iloc[:,2:14]

corr_flavors = pd.DataFrame.corr(flavors)

plt.figure(figsize=(10,10))
plt.pcolor(corr_flavors)
plt.colorbar()
plt.savefig("corr_flavors.pdf")

corr_whisky = pd.DataFrame.corr(flavors.transpose())
plt.figure(figsize=(10,10))
plt.pcolor(corr_whisky)
plt.axis("tight")
plt.colorbar()
plt.savefig("corr_whisky.pdf")




from sklearn.cluster.bicluster import SpectralCoclustering

model = SpectralCoclustering(n_clusters=6, random_state=0)
model.fit(corr_whisky)


whisky['Group']=pd.Series(model.row_labels_, index=whisky.index)
whisky=whisky.ix[np.argsort(model.row_labels_)]

whisky=whisky.reset_index(drop=True)
correlations = pd.DataFrame.corr(whisky.iloc[:,2:14].transpose())
correlations= np.array(correlations)

plt.figure(figsize=(10,10))
plt.pcolor(corr_flavors)
plt.colorbar()
plt.savefig("corr_flavors.pdf")

corr_whisky = pd.DataFrame.corr(flavors.transpose())
plt.figure(figsize=(10,10))
plt.pcolor(corr_whisky)
plt.axis("tight")
plt.colorbar()
plt.savefig("corr_whisky.pdf")


import pandas as pd 
data = pd.Series([1,2,3,4]) 
data = data.ix[[3,0,1,2]] 
data = data.reset_index(drop=True)
