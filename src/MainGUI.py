# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\aa0049.UWS30383\Desktop\PythonGUI_Test\form_drop_multiple_helpWin1.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
__author__ = 'Shirin,Alireza'

from PyQt4 import QtCore, QtGui
import preproc
import AlgorithmManager1 as amc
import sys
import os
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import pandas
import numpy as np
import csv
import datetime

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(QtGui.QWidget):

    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        self.Data=[]
        self.DataDimension=[]

#add self.Form=Form it is required for future steps
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(706, 756)
        self.Form=Form
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout.addWidget(self.pushButton_2, 3, 0, 1, 1)
        self.groupBox = QtGui.QGroupBox(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 200))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_11 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_11.setObjectName(_fromUtf8("gridLayout_11"))
        self.gridLayout_10 = QtGui.QGridLayout()
        self.gridLayout_10.setObjectName(_fromUtf8("gridLayout_10"))
        self.pushButton_4 = QtGui.QPushButton(self.groupBox)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.gridLayout_10.addWidget(self.pushButton_4, 1, 2, 1, 1)
        self.lineEdit_8 = QtGui.QLineEdit(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_8.sizePolicy().hasHeightForWidth())
        self.lineEdit_8.setSizePolicy(sizePolicy)
        self.lineEdit_8.setObjectName(_fromUtf8("lineEdit_8"))
        self.gridLayout_10.addWidget(self.lineEdit_8, 1, 1, 1, 1)
        self.lineEdit_7 = QtGui.QLineEdit(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_7.sizePolicy().hasHeightForWidth())
        self.lineEdit_7.setSizePolicy(sizePolicy)
        self.lineEdit_7.setObjectName(_fromUtf8("lineEdit_7"))
        self.gridLayout_10.addWidget(self.lineEdit_7, 0, 1, 1, 1)
        self.pushButton_3 = QtGui.QPushButton(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.gridLayout_10.addWidget(self.pushButton_3, 0, 2, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_10.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_10.addWidget(self.label_3, 1, 0, 1, 1)
        self.gridLayout_11.addLayout(self.gridLayout_10, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(Form)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_9 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_9.setObjectName(_fromUtf8("gridLayout_9"))
        self.gridLayout_8 = QtGui.QGridLayout()
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.lineEdit_2 = QtGui.QLineEdit(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.gridLayout_8.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.lineEdit = QtGui.QLineEdit(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout_8.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.comboBox = QtGui.QComboBox(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.gridLayout_8.addWidget(self.comboBox, 0, 0, 1, 1)
        self.comboBox_2 = QtGui.QComboBox(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_2.sizePolicy().hasHeightForWidth())
        self.comboBox_2.setSizePolicy(sizePolicy)
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.gridLayout_8.addWidget(self.comboBox_2, 1, 0, 1, 1)
        self.lineEdit_6 = QtGui.QLineEdit(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_6.sizePolicy().hasHeightForWidth())
        self.lineEdit_6.setSizePolicy(sizePolicy)
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.gridLayout_8.addWidget(self.lineEdit_6, 5, 1, 1, 1)
        self.comboBox_6 = QtGui.QComboBox(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_6.sizePolicy().hasHeightForWidth())
        self.comboBox_6.setSizePolicy(sizePolicy)
        self.comboBox_6.setObjectName(_fromUtf8("comboBox_6"))
        self.gridLayout_8.addWidget(self.comboBox_6, 5, 0, 1, 1)
        self.lineEdit_5 = QtGui.QLineEdit(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_5.sizePolicy().hasHeightForWidth())
        self.lineEdit_5.setSizePolicy(sizePolicy)
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.gridLayout_8.addWidget(self.lineEdit_5, 4, 1, 1, 1)
        self.comboBox_8 = QtGui.QComboBox(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_8.sizePolicy().hasHeightForWidth())
        self.comboBox_8.setSizePolicy(sizePolicy)
        self.comboBox_8.setObjectName(_fromUtf8("comboBox_8"))
        self.gridLayout_8.addWidget(self.comboBox_8, 6, 0, 1, 1)
        self.lineEdit_9 = QtGui.QLineEdit(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_9.sizePolicy().hasHeightForWidth())
        self.lineEdit_9.setSizePolicy(sizePolicy)
        self.lineEdit_9.setObjectName(_fromUtf8("lineEdit_9"))
        self.gridLayout_8.addWidget(self.lineEdit_9, 6, 1, 1, 1)
        self.lineEdit_4 = QtGui.QLineEdit(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_4.sizePolicy().hasHeightForWidth())
        self.lineEdit_4.setSizePolicy(sizePolicy)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.gridLayout_8.addWidget(self.lineEdit_4, 3, 1, 1, 1)
        self.comboBox_5 = QtGui.QComboBox(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_5.sizePolicy().hasHeightForWidth())
        self.comboBox_5.setSizePolicy(sizePolicy)
        self.comboBox_5.setObjectName(_fromUtf8("comboBox_5"))
        self.gridLayout_8.addWidget(self.comboBox_5, 4, 0, 1, 1)
        self.comboBox_3 = QtGui.QComboBox(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_3.sizePolicy().hasHeightForWidth())
        self.comboBox_3.setSizePolicy(sizePolicy)
        self.comboBox_3.setObjectName(_fromUtf8("comboBox_3"))
        self.gridLayout_8.addWidget(self.comboBox_3, 2, 0, 1, 1)
        self.lineEdit_3 = QtGui.QLineEdit(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.gridLayout_8.addWidget(self.lineEdit_3, 2, 1, 1, 1)
        self.comboBox_4 = QtGui.QComboBox(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_4.sizePolicy().hasHeightForWidth())
        self.comboBox_4.setSizePolicy(sizePolicy)
        self.comboBox_4.setObjectName(_fromUtf8("comboBox_4"))
        self.gridLayout_8.addWidget(self.comboBox_4, 3, 0, 1, 1)
        self.comboBox_9 = QtGui.QComboBox(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_9.sizePolicy().hasHeightForWidth())
        self.comboBox_9.setSizePolicy(sizePolicy)
        self.comboBox_9.setObjectName(_fromUtf8("comboBox_9"))
        self.gridLayout_8.addWidget(self.comboBox_9, 7, 0, 1, 1)
        self.lineEdit_10 = QtGui.QLineEdit(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_10.sizePolicy().hasHeightForWidth())
        self.lineEdit_10.setSizePolicy(sizePolicy)
        self.lineEdit_10.setObjectName(_fromUtf8("lineEdit_10"))
        self.gridLayout_8.addWidget(self.lineEdit_10, 7, 1, 1, 1)
        self.gridLayout_9.addLayout(self.gridLayout_8, 0, 0, 1, 1)
        self.groupBox.raise_()
        self.gridLayout.addWidget(self.groupBox_2, 2, 0, 1, 1)
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 4, 0, 1, 1)
        self.groupBox_3 = QtGui.QGroupBox(Form)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.gridLayout_12 = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout_12.setObjectName(_fromUtf8("gridLayout_12"))
        self.textEdit = QtGui.QTextEdit(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.gridLayout_12.addWidget(self.textEdit, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_3, 5, 0, 1, 1)
        self.groupBox_4 = QtGui.QGroupBox(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.gridLayout_14 = QtGui.QGridLayout()
        self.gridLayout_14.setObjectName(_fromUtf8("gridLayout_14"))
        self.verticalLayout_3.addLayout(self.gridLayout_14)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.pushButton_6 = QtGui.QPushButton(self.groupBox_4)
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.horizontalLayout_3.addWidget(self.pushButton_6)
        self.comboBox_7 = QtGui.QComboBox(self.groupBox_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_7.sizePolicy().hasHeightForWidth())
        self.comboBox_7.setSizePolicy(sizePolicy)
        self.comboBox_7.setObjectName(_fromUtf8("comboBox_7"))
        self.horizontalLayout_3.addWidget(self.comboBox_7)
        self.pushButton_5 = QtGui.QPushButton(self.groupBox_4)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.horizontalLayout_3.addWidget(self.pushButton_5)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.gridLayout.addWidget(self.groupBox_4, 2, 1, 4, 1)
        self.widget = QtGui.QWidget(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout.addWidget(self.widget, 0, 1, 1, 1)
        self.widget = QtGui.QWidget(Form)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout.addWidget(self.widget, 0, 1, 1, 1)
        pic = QtGui.QLabel(self.widget)
        pic.setGeometry(10, 10, 800, 100)
        pic.setPixmap(QtGui.QPixmap(os.getcwd() + "/KAT_logo.png"))
        self.figure = plt.figure()
        self.figure.patch.set_facecolor('white')
        self.figure.patch.set_alpha(0.7)
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.gridLayout_14.addWidget(self.canvas)
        self.gridLayout_14.addWidget(self.toolbar)


        self.pushButton_3.clicked.connect(self.InputDirectory)
        self.pushButton_4.clicked.connect(self.Save)
        self.pushButton_2.clicked.connect(self.loadDialog)
        self.pushButton.clicked.connect(self.Run)

        '''am = amc.AlgorithmManager1()
        self.ListAlgorithms=am.CollectMethods()
        #self.ListAlgorithms=['-','---------PREPROCESSING---------','Moving Average','Outlier Removal','---------DATA VISUALIZATION---------']
        for k in self.ListAlgorithms:
            self.comboBox.addItem(k)
            self.comboBox_2.addItem(k)              #List of Combo Boxes
            self.comboBox_3.addItem(k)
            self.comboBox_4.addItem(k)
            self.comboBox_5.addItem(k)
            self.comboBox_6.addItem(k)
            self.comboBox_8.addItem(k)
            self.comboBox_9.addItem(k)'''


        am=amc.AlgorithmManager1()
        ss=am.getAlgorithms().keys()
        ss.sort()
        print(ss)
        for k in ss:
            self.comboBox.addItem(k)
            self.comboBox_2.addItem(k)
            self.comboBox_3.addItem(k)
            self.comboBox_4.addItem(k)
            self.comboBox_5.addItem(k)
            self.comboBox_6.addItem(k)
            self.comboBox_8.addItem(k)
            self.comboBox_9.addItem(k)

        #Help COnsole Area
        self.comboBox.currentIndexChanged['QString'].connect(self.HelpBoxText)
        self.comboBox_2.currentIndexChanged['QString'].connect(self.HelpBoxText)
        self.comboBox_3.currentIndexChanged['QString'].connect(self.HelpBoxText)
        self.comboBox_4.currentIndexChanged['QString'].connect(self.HelpBoxText)
        self.comboBox_5.currentIndexChanged['QString'].connect(self.HelpBoxText)
        self.comboBox_6.currentIndexChanged['QString'].connect(self.HelpBoxText)
        self.comboBox_8.currentIndexChanged['QString'].connect(self.HelpBoxText)
        self.comboBox_9.currentIndexChanged['QString'].connect(self.HelpBoxText)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.pushButton_2.setText(_translate("Form", "Load Data", None))
        self.groupBox.setTitle(_translate("Form", "Input/Output Files", None))
        self.pushButton_4.setText(_translate("Form", "...", None))
        self.pushButton_3.setText(_translate("Form", "...", None))
        self.label_2.setText(_translate("Form", "Input:", None))
        self.label_3.setText(_translate("Form", "Save Output:", None))
        self.groupBox_2.setTitle(_translate("Form", "Methods and Parameters", None))
        self.pushButton.setText(_translate("Form", "Run", None))
        self.groupBox_3.setTitle(_translate("Form", "Console Output", None))
        self.groupBox_4.setTitle(_translate("Form", "Figure Console", None))
        self.pushButton_6.setText(_translate("Form", "<<", None))
        self.pushButton_5.setText(_translate("Form", ">>", None))

    def InputDirectory(self):
        filename = QtGui.QFileDialog.getOpenFileName(self, 'Open File', '.')
        self.lineEdit_7.setText(filename)

    def Save(self):
        #filename = QtGui.QFileDialog.getSaveFileName(self, 'Save File', '.')
        path = QtGui.QFileDialog.getSaveFileName(self.Form, 'Save File', '', 'CSV(*.csv)')
        self.lineEdit_8.setText(path)
        if not path.isEmpty():
            with open(unicode(path), 'wb') as stream:
                writer = csv.writer(stream)
                [a,b]=self.Data.shape
                for row in range(a):
                    rowdata = []
                    for column in range(b):
                        item = self.Data.item(row, column)
                        if item is not None:
                            rowdata.append(item)
                        else:
                            rowdata.append('')
                    writer.writerow(rowdata)
        self.textEdit.setText('Output Saved')
        print "The output is saved in", path

    def loadDialog(self):           #Load Data
        filename=self.lineEdit_7.text()
        reader = pandas.read_csv(str(filename), delimiter=",")

        reader['time_stamp'] = reader['time_stamp'].astype('datetime64[ns]')
        a=[]
        for row in reader:
             a.append(''.join(row))
   #print '' .join(row)
        print(a)
        name='time_stamp'
        for p in a:
            if ('time_stamp' in a):
                reader['time_stamp'] = reader['time_stamp'].astype('datetime64[ns]')
                self.sph=sum((reader['time_stamp'] >= reader.time_stamp[0]) & (reader['time_stamp'] < reader.time_stamp[0]+datetime.timedelta(hours=1) ))
                self.spd=sum((reader['time_stamp'] >= reader.time_stamp[0]) & (reader['time_stamp'] < reader.time_stamp[0]+datetime.timedelta(days=1) ))
                self.nd=round(len(reader.time_stamp)/self.spd)
            else:
                msgBox = QtGui.QMessageBox()
                msgBox.setText('Change the lable of time channel to "time_stamp" !  ')
                msgBox.setWindowTitle ('Warning!!!' )
                msgBox.exec_()

        #reader.ffill(inplace=True)
        #reader=reader.fillna(reader.mean())
        ''' We can enter two textbox to define a specific range for data (in terms of days or samples)
        if (self.startD.text().isEmpty()) & (self.endD.text().isEmpty()):
            Data=reader
        else:
            reader['time_stamp'] = reader['time_stamp'].astype('datetime64[ns]')
            st = int(self.startD.text())
            en = int(self.endD.text())
            select = (reader['time_stamp'] >= reader.time_stamp[0]+datetime.timedelta(days=st-1)) & (reader['time_stamp'] < reader.time_stamp[0]+datetime.timedelta(days=en))
            Data = reader[select]
        '''
        Data_o=reader
        space = 0
        self.checkboxes = []
        for i in Data_o.columns:
            c = QtGui.QCheckBox(self.Form)
            #print space
            c.setGeometry(QtCore.QRect(10 + space, 130, 70, 17))
            c.setText(_fromUtf8(i))
            c.show()
            c.clicked.connect(self.selected)
            self.checkboxes.append(c)
            space += 85
                    #Data=reader.values
        DimTemp=np.shape(Data_o)
        Dim=DimTemp[1]
        '''for s in range(0,Dim):      #Plot data
            plt.figure(s+1)
            plt.plot(Data[:,s])
            plt.show()'''
        self.Data_o=Data_o
        self.Data_oDimension=Dim
        self.textEdit.clear()
        #self.textEdit.setText('LOADED DATA')
        self.textEdit.setText('LOADED DATA'+'\n'+'Sample per hour:'+str(self.sph)+'\n'+'Sample per day:'+str(self.spd)+'\n'+'Number of days included:'+str(self.nd) )

        #'Samples per hour:',sph,'Samples per day:',spd,'Number of days included:',round(len(reader.time_stamp)/spd))

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    def selected(self, state):
        from itertools import cycle
        selItems = []
        for c in self.checkboxes:
            c.isChecked()
            c.text()
            if c.isChecked():
                selItems.append(str(c.text()))
        self.selected_data = np.array(self.Data_o[selItems])
        print "Size of the selected data", self.selected_data.shape
        Data = self.selected_data
        DimTemp=np.shape(Data)
        Dim=DimTemp[1]
        '''for s in range(0,Dim):      #Plot data
            plt.figure(s+1)
            plt.plot(Data[:,s])
            plt.show()'''
        self.Data=Data
        self.DataDimension=Dim
        self.textEdit.clear()
        self.textEdit.setText('LOADED DATA'+'\n'+'Sample per hour:'+str(self.sph)+'\n'+'Sample per day:'+str(self.spd)+'\n'+'Number of days included:'+str(self.nd) )
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    def HelpBoxText(self, text):        #HelpTextBox function
        am = amc.AlgorithmManager1()
        self.textEdit.clear()
        #self.textEdit.setText(am.HelpInformation(text))

    def Run(self):
        if self.DataDimension:
            self.textEdit.clear()
            am = amc.AlgorithmManager1()
            am.CollectData(self.DataDimension,self.Data)
            am.CollectMethods(self.comboBox.currentText(),self.comboBox_2.currentText(),self.comboBox_3.currentText(),self.comboBox_4.currentText(),self.comboBox_5.currentText(),self.comboBox_6.currentText(),self.comboBox_8.currentText(),self.comboBox_9.currentText())
            am.CollectParameters(self.lineEdit.text(),self.lineEdit_2.text(),self.lineEdit_3.text(),self.lineEdit_4.text(),self.lineEdit_5.text(),self.lineEdit_6.text(),self.lineEdit_9.text(),self.lineEdit_10.text())
            win=1
            if (self.comboBox.currentText()=='F-ResamplePAA'):win=self.lineEdit.text()
            if (self.comboBox_2.currentText()=='F-ResamplePAA'):win=self.lineEdit_2.text()
            if (self.comboBox_3.currentText()=='F-ResamplePAA'):win=self.lineEdit_3.text()
            if (self.comboBox_4.currentText()=='F-ResamplePAA'):win=self.lineEdit_4.text()
            if (self.comboBox_5.currentText()=='F-ResamplePAA'):win=self.lineEdit_5.text()
            if (self.comboBox_6.currentText()=='F-ResamplePAA'):win=self.lineEdit_6.text()
            if (self.comboBox_7.currentText()=='F-ResamplePAA'):win=self.lineEdit_7.text()
            if (self.comboBox_8.currentText()=='F-ResamplePAA'):win=self.lineEdit_8.text()
            Output=am.Main()
            print Output
            ax = self.figure.add_subplot(111)
            ax.hold(False)
            ax.plot(Output, '.-')
            self.canvas.draw()
            #self.textEdit.setText('RUN FINISHED')
            self.textEdit.setText('RUN FINISHED'+'\n'+'New sample per hour~:'+str(self.sph/float(win))+'\n'+'New sample per day~:'+str(self.spd/float(win))+'\n'+'Number of days included:'+str(self.nd) )

        else:           #If no data is loaded prompt message box
            msgBox = QtGui.QMessageBox()
            msgBox.setText('Please Load Data!      ')
            msgBox.setWindowTitle ('Warning!!!' )
            msgBox.exec_()

'''if __name__=='__main__':
    app=QtGui.QApplication(sys.argv)
    ex=Ui_Form()
    ex.show()
    sys.exit(app.exec_())'''

def main():
    import sys
    app=QtGui.QApplication(sys.argv)
    #MainWindow = QtGui.QMainWindow()
    ui = Ui_Form()
    ui.show()
    #ui.setupUi(MainWindow)
    #MainWindow.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
        main()
