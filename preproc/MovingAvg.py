__author__ = 'shirin'

import pandas as pd
from PyQt4 import QtCore, QtGui

class MovingAvg():
    def process(self, data,window):
        data=pd.DataFrame(data)
        result=pd.DataFrame(index=data.index,columns=data.columns)
        if not window:
            msgBox = QtGui.QMessageBox()
            msgBox.setText('Please enter the filter length for moving averag! ')
            msgBox.setWindowTitle ('Warning!!!' )
            msgBox.exec_()
        else:
            #if window.split()
            for i in range(data.columns.size):
                result = ( pd.rolling_mean(data, int(window), center=True) )
                result.ffill(inplace=True)
                result.bfill(inplace=True)
        #result = np.array(result)
        #print "paa output shape", result.shape
        return result

    def getConfigurationParams(self):
        return {"window":"1"}

