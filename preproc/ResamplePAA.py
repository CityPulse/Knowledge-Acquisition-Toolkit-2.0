__author__ = 'shirin'

import pandas as pd
from PyQt4 import QtCore, QtGui
from Paa import *

class ResamplePAA():
    def process(self,data,window):
        p=Paa()
        data=pd.DataFrame(data)
        result=pd.DataFrame(index=data.index,columns=data.columns)
        if not window:
            msgBox = QtGui.QMessageBox()
            msgBox.setText('Please enter the scaling factor for resampling! ')
            msgBox.setWindowTitle ('Warning!!!' )
            msgBox.exec_()
        else:
            result=pd.DataFrame( p.process( data.iloc[:,0],data.__len__()/(int(window)) ) )

            result=pd.DataFrame(index=result.index,columns=data.columns)
            for i in range(data.columns.size):
                result.iloc[:,i]=p.process( data.iloc[:,i],data.__len__()/(int(window)) )
        #result = np.array(result)
        # print "paa output shape", result.shape
        return result

    def getConfigurationParams(self):
        return {"window":"1"}



