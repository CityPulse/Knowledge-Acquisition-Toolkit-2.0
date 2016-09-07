__author__ = 'shirin '

import time
import numpy as np
import pylab as pl
import pandas as pd
from sklearn.cluster import MiniBatchKMeans, KMeans
from PyQt4 import QtCore, QtGui
import matplotlib.pyplot as plt
from scipy.spatial.distance import cdist
from sklearn.metrics.pairwise import paired_distances

class corrM():
    def process(self,data,output_length):
        data=pd.DataFrame(data)
        print(data.shape)
        #plt.matshow(data.corr())
        result=(data.iloc[:,0]-data.iloc[:,1])**2
        print(result)
        print(result.shape)
        return result

    def getConfigurationParams(self):
        return {"output_length":"1"}


