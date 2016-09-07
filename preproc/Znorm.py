__author__ = 'shirin'
import pandas as pd

class Znorm():
    def process(self, data,output_length):
        data=pd.DataFrame(data)
        result=pd.DataFrame(index=data.index,columns=data.columns)
        for i in range(data.columns.size):
            result.iloc[:, i] = ( (data.iloc[:, i] - data.iloc[:, i].mean()) / data.iloc[:, i].std() )
        #result = np.array(result)
        #print "paa output shape", result.shape
        return result

    def getConfigurationParams(self):
        return {"output_length":"1"}