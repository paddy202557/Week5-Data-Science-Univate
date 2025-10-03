##Splitting the dataset  columns to Quantitative (Numerical) and Qualitative (String based on the data type 
import pandas as pd
import numpy as np

class QQUnivariate():
    
    
    def quanQual(dataset):
        quan=[]
        qual=[]
        for columnName in dataset.columns:
            #print(columnName)
            if(dataset[columnName].dtype=='O'):
                #print("qual")
                qual.append(columnName)
            else:
                #print("quan")
                quan.append(columnName)
        return quan,qual
    
    def freqTable(columnName,dataset):
        freqTable=pd.DataFrame(columns=["Unique_Values", "Frequency","Relative_Frequency", "Cumulative_Sum"])
        freqTable["Unique_Values"]=dataset[columnName].value_counts().index
        freqTable["Frequency"]=dataset[columnName].value_counts().values
        freqTable["Relative_Frequency"]=(freqTable["Frequency"]/103)
        freqTable["Cumulative_Sum"]=freqTable["Relative_Frequency"].cumsum()
        return freqTable
    
    
    def LesserGreater(Quan1,descriptive):
        Lesser=[]
        Greater=[]
        for columnName in  Quan1:
            if (descriptive[columnName]["Min"] < descriptive[columnName]["Lesser"]):
                 Lesser.append(columnName)   
            if  (descriptive[columnName]["Max"] > descriptive[columnName]["Greater"]):
                 Greater.append(columnName) 
        return Lesser,Greater            
                    
    def Univariate(Quan1,dataset):
        descriptive=pd.DataFrame(index=["Mean", "Median", "Mode","Q1:25%", "Q2:50%", "Q3:75%", "Q4:100%","99%",
                                "IQR","1.5rule","Lesser","Greater","Min","Max","kurtosis","skew"],columns=Quan1)
        for columnName in Quan1:
            descriptive[columnName]["Mean"]=round(dataset[columnName].mean())
            descriptive[columnName]["Median"]=dataset[columnName].median()
            descriptive[columnName]["Mode"]=dataset[columnName].mode()[0]
            descriptive[columnName]["Q1:25%"]=dataset.describe()[columnName]["25%"]
            descriptive[columnName]["Q2:50%"]=dataset.describe()[columnName]["50%"]
            descriptive[columnName]["Q3:75%"]=dataset.describe()[columnName]["75%"]
            descriptive[columnName]["Q4:100%"]=dataset.describe()[columnName]["max"]
            #99% 
            descriptive[columnName]["99%"]= np.percentile(dataset[columnName],99)
            #IQR Calculation IQR = Q3 - Q1.
            descriptive[columnName]["IQR"]= descriptive[columnName]["Q3:75%"] - descriptive[columnName]["Q1:25%"] 
            #1.5 Rule to calculate the  Low and High outlier range
            descriptive[columnName]["1.5rule"]=1.5* descriptive[columnName]["IQR"]
            #Low Outlier Range Q1 - 1.5 × IQR
            descriptive[columnName]["Lesser"]= descriptive[columnName]["Q1:25%"] - descriptive[columnName]["1.5rule"]
            #High Outlier Range Q3 + 1.5 × IQR
            descriptive[columnName]["Greater"]=  descriptive[columnName]["Q3:75%"] + descriptive[columnName]["1.5rule"]
            #Derive the min and  max  column value  from the data set
            descriptive[columnName]["Min"]= dataset[columnName].min()
            descriptive[columnName]["Max"] =dataset[columnName].max()
            descriptive[columnName]["kurtosis"]=dataset[columnName].kurtosis()
            descriptive[columnName]["skew"]=dataset[columnName].skew()
        return descriptive   