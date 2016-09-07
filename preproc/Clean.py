__author__ = 'shirin'
import pandas as pd
import numpy as np

class Clean():
    def process(self, data,output_length):
        #********Clean Nan values
        data=pd.DataFrame(data)
        data.ffill(inplace=True)
        data=data.fillna(data.mean())
        result=data
        return result

    def getConfigurationParams(self):
        return {"output_length":"1"}
