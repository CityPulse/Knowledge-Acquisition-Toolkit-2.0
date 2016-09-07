__author__ = 'shirin'


import pandas as pd
from PyQt4 import QtCore, QtGui
import datetime

class MovingAvg():
    def process(self, data , window):
        data=pd.DataFrame(data)
        if not window:
            msgBox = QtGui.QMessageBox()
            msgBox.setText('Please enter the label of time channel! ')
            msgBox.setWindowTitle ('Warning!!!' )
            msgBox.exec_()
        else:
            data['time_stamp'] = data['time_stamp'].astype('datetime64[ns]')
            spd=sum((data['time_stamp'] >= data.time_stamp[0]) & (data['time_stamp'] < data.time_stamp[0]+datetime.timedelta(days=1) ))
            print "Samples per day:",sum((data['time_stamp'] >= data.time_stamp[0]) & (data['time_stamp'] < data.time_stamp[0]+datetime.timedelta(days=1) ))
        return spd

    def getConfigurationParams(self):
        return {"window":"1"}

