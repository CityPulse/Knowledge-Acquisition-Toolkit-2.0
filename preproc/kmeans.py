__author__ = 'shirin'
import time

import numpy as np
import pylab as pl
import pandas as pd
from sklearn.cluster import MiniBatchKMeans, KMeans
from PyQt4 import QtCore, QtGui
from scipy.cluster.vq import kmeans2
from src.MainGUI import Ui_Form
class kmeans():
    def process(self,data,clusterSize):
        if not clusterSize:
            msgBox = QtGui.QMessageBox()
            msgBox.setText('Please enter the number of clusters! ')
            msgBox.setWindowTitle ('Warning!!!' )
            msgBox.exec_()
        else:
            result=[]
            kmeans = KMeans(int(clusterSize))
            result_in=pd.DataFrame(index=data.index,columns=data.columns)
            data=pd.DataFrame(data)
            for i in range(data.columns.size):
                x=pd.DataFrame(data.iloc[:,i])
                kmeans.fit(x)
                labels = kmeans.labels_
                result_in.iloc[:,i]=labels
            #msgBox = QtGui.QMessageBox()
            #msgBox.setText('Cluster center for the selected channels: '+str(kmeans.cluster_centers_))
            #msgBox.setWindowTitle ('Inofrmation!' )
            #msgBox.exec_()
            return result_in
            #TODO I added the clusterer as return value will not work with GUI

    def getConfigurationParams(self):
        return {"clusterSize":"2"}


''' #####################Do not delete: individual label
for i in range(data.columns.size):
                #x=pd.DataFrame(data.iloc[:,i])
                #kmeans.fit(x)
                #labels = kmeans.labels_
                #result.iloc[:,i]=labels
                [output,labels3]=kmeans2(np.array(data),int(clusterSize))
                print(labels3)
                result.iloc[:,i]=labels3 '''

''' ####################Global label
kmeans = KMeans(int(clusterSize))
            data=pd.DataFrame(data)
            hpc=data.values
            kmeans.fit(hpc)
            result=kmeans.labels_ '''

