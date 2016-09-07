__author__ = 'Shirin,Alireza'
from PyQt4 import QtCore, QtGui
#import preproc.Non
#import preproc.minmax
#import preproc.mean
import csv
#from form_drop_multiple_helpWin1O.py import Ui_Form
import numpy as np
import preproc.Znorm
import preproc.norm
import preproc.Clean
import preproc.Outlier
import preproc.MovingAvg
import preproc.Non
import preproc.SAX_mine
import preproc.ResamplePAA
import preproc.kmeans
#import preproc.corrM
#import preproc.dbscan_m

class AlgorithmManager1(QtGui.QWidget):


    def __init__(self):
        QtGui.QWidget.__init__(self)
        ####self.Output=[]
        #Dictionary of algorithms
        self.algorithms = {"H-Kmeans":"kmeans","G-SAX":"SAX_mine","F-ResamplePAA":"ResamplePAA","E-MovingAvg":"MovingAvg",
                           "Db-norm":"norm","D-Znorm":"Znorm","C-Outlier":"Outlier","B-Clean":"Clean","A-Non":"Non"}
        #{"-":"Non","---------PREPROCESSING---------":"Non","Moving Average":"mean","---------DATA VISUALIZATION---------":"Non"}
        #self.selected = None
        self.module_path = "preproc."


    #print logic.preproc.bandpass.bandpass()
    #print logic.preproc.integration.integration()
    def Main(self):     #Selects the appropriate algorithm based on the users input
        ComboBox_1 = getattr(getattr(preproc,self.algorithms[self.method_1]), self.algorithms[self.method_1])()
        self.Output=ComboBox_1.process(self.Data,self.param_1)
        ComboBox_2 = getattr(getattr(preproc,self.algorithms[self.method_2]), self.algorithms[self.method_2])()
        self.Output=ComboBox_2.process(self.Output,self.param_2)
        ComboBox_3 = getattr(getattr(preproc,self.algorithms[self.method_3]), self.algorithms[self.method_3])()
        self.Output=ComboBox_3.process(self.Output,self.param_3)
        ComboBox_4 = getattr(getattr(preproc,self.algorithms[self.method_4]), self.algorithms[self.method_4])()
        self.Output=ComboBox_4.process(self.Output,self.param_4)
        ComboBox_5 = getattr(getattr(preproc,self.algorithms[self.method_5]), self.algorithms[self.method_5])()
        self.Output=ComboBox_5.process(self.Output,self.param_5)
        ComboBox_6 = getattr(getattr(preproc,self.algorithms[self.method_6]), self.algorithms[self.method_6])()
        self.Output=ComboBox_6.process(self.Output,self.param_6)
        ComboBox_7 = getattr(getattr(preproc,self.algorithms[self.method_7]), self.algorithms[self.method_7])()
        self.Output=ComboBox_7.process(self.Output,self.param_7)
        ComboBox_8 = getattr(getattr(preproc,self.algorithms[self.method_8]), self.algorithms[self.method_8])()
        self.Output=ComboBox_8.process(self.Output,self.param_8)
        #self.SaveOutput(self.Output,self.filename)
        return self.Output

    def CollectData(self,DataDimension,Data):                       #Collect the data set from the main window
        self.Data=Data
        self.DataDimension=DataDimension

    def getAlgorithms(self):
        return self.algorithms

    def CollectMethods(self,Meth_1,Meth_2,Meth_3,Meth_4,Meth_5,Meth_6,Meth_7,Meth_8):                   #Collect methods from drop down menus
        self.method_1=str(Meth_1)
        self.method_2=str(Meth_2)
        self.method_3=str(Meth_3)
        self.method_4=str(Meth_4)
        self.method_5=str(Meth_5)
        self.method_6=str(Meth_6)
        self.method_7=str(Meth_7)
        self.method_8=str(Meth_8)

        #x="21 3"
        #[a,b]=x.split()
        #print(a)
        #print(b)

    def CollectParameters(self,Param_1,Param_2,Param_3,Param_4,Param_5,Param_6,Param_7,Param_8):                #Collect Corresponding Parameters
        self.param_1=str(Param_1)
        self.param_2=str(Param_2)
        self.param_3=str(Param_3)
        self.param_4=str(Param_4)
        self.param_5=str(Param_5)
        self.param_6=str(Param_6)
        self.param_7=str(Param_7)
        self.param_8=str(Param_8)
        #[a,b]=self.param_1.split()
        #print(a)
        #print(b)
        #print(int(a))
        #print(int(b))

    '''def CollectFilename(self,filename):
        self.filename=str(filename)'''

    '''def SaveOutput(self,OutputData,filename):
        ###filename = QtGui.QFileDialog.getSaveFileName(self, 'Save File', '.')    #Open directory corresponding to the location to save.
        ###f=open(filename) open("Output.csv", "wb")
        with open(filename, "wb") as myfile:
            wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
            wr.writerow(OutputData)'''

    def HelpInformation(self,text):
        Algorithm=str(text)
        ComboBoxHelp = getattr(getattr(preproc,self.algorithms[Algorithm]), self.algorithms[Algorithm])()
        Text=ComboBoxHelp.Help()
        return(str(Text))

