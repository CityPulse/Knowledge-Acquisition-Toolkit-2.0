__author__ = 'shirin'
import time

import numpy as np
import pylab as pl
import pandas as pd
from sklearn.cluster import DBSCAN
from PyQt4 import QtCore, QtGui
from scipy.cluster.vq import kmeans2

class dbscan_m():
    def process(self,data,clusterSize):
        dbscan = DBSCAN()
        data=pd.DataFrame(data)
        hpc=data.values
        dbscan.fit(hpc)
            #new column
            #classified_data = k_means.labels_
            #df_processed = sliced.copy()
            #data_processed['Cluster Class'] = pd.Series(classified_data, index=data_processed.index)
        result=dbscan.labels_
        return result
            #TODO I added the clusterer as return value will not work with GUI

    def getConfigurationParams(self):
        return {"clusterSize":"2"}

'''for i in range(data.columns.size):
                #x=pd.DataFrame(data.iloc[:,i])
                #kmeans.fit(x)
                #labels = kmeans.labels_
                #result.iloc[:,i]=labels
                [output,labels3]=kmeans2(np.array(data),int(clusterSize))
                print(labels3)
                result.iloc[:,i]=labels3'''

