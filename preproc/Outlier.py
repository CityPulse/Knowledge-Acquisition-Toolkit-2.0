__author__ = 'shirin'
import pandas as pd
import numpy as np

class Outlier():
    def process(self, data,output_length):
        #********Clean Nan values
        data=pd.DataFrame(data)
        Rdata2=pd.DataFrame(index=data.index,columns=data.columns)
        for i in range(Rdata2.columns.size):
            Rdata2.iloc[:,i]=data.iloc[:,i]
            x=Rdata2.iloc[:,i]
            lower,upper=x.mean()-3*x.std(),x.mean()+3*x.std(),
            print(lower,upper)
            Rdata2.loc[Rdata2.iloc[:,i]>upper,Rdata2.columns[i]] = upper
            Rdata2.loc[Rdata2.iloc[:,i]<lower,Rdata2.columns[i]] = lower
        result=Rdata2
        return result

    def getConfigurationParams(self):
        return {"output_length":"1"}
