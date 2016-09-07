__author__ = 'se00075'

import pandas as pd
from sklearn.cross_validation import train_test_split
#####
import matplotlib.pyplot as plt
import numpy as np
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

class test():
    def process(self,data,clusterSize):
        data=pd.DataFrame(data)
        iot = data.iloc[:,:].dropna()
        pc_toarray = iot.values
        hpc_fit, hpc_fit1 = train_test_split(pc_toarray, train_size=.01)
        iot.head()

        hpc = PCA(n_components=2).fit_transform(hpc_fit)
        k_means = KMeans()
        k_means.fit(hpc)

        x_min, x_max = hpc[:, 0].min() - 5, hpc[:, 0].max() - 1
        y_min, y_max = hpc[:, 1].min(), hpc[:, 1].max() + 5
        xx, yy = np.meshgrid(np.arange(x_min, x_max, .02), np.arange(y_min, y_max, .02))
        Z = k_means.predict(np.c_[xx.ravel(), yy.ravel()])
        Z = Z.reshape(xx.shape)

        plt.figure(1)
        plt.clf()
        plt.imshow(Z, interpolation='nearest',
          extent=(xx.min(), xx.max(), yy.min(), yy.max()),
          cmap=plt.cm.Paired,
          aspect='auto', origin='lower')

        plt.plot(hpc[:, 0], hpc[:, 1], 'k.', markersize=4)
        centroids = k_means.cluster_centers_
        inert = k_means.inertia_
        plt.scatter(centroids[:, 0], centroids[:, 1],
           marker='x', s=169, linewidths=3,
           color='w', zorder=8)
        plt.xlim(x_min, x_max)
        plt.ylim(y_min, y_max)
        plt.xticks(())
        plt.yticks(())
        plt.show()