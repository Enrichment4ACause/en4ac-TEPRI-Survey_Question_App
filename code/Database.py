import pandas as pd
import numpy as np

class Database:
    df_Demographic = pd.DataFrame(columns=["ID", "Question", "Tag", "Year", "Survey", "Response Choices"])
    df_Energy_efficency = pd.DataFrame(columns=["ID", "Question", "Tag", "Year", "Survey", "Response Choices"])
    df_Affordability = pd.DataFrame(columns=["ID", "Question", "Tag", "Year", "Survey", "Response Choices"])
    df_Reliability = pd.DataFrame(columns=["ID", "Question", "Tag", "Year", "Survey", "Response Choices"])
    df_Grid_flexibility = pd.DataFrame(columns=["ID", "Question", "Tag", "Year", "Survey", "Response Choices"])
    df_Other = pd.DataFrame(columns=["ID", "Question", "Tag", "Year", "Survey", "Response Choices"])


    def __init__(self,data):
        #Assuming data is same format as above+Category. Work on saving to local files using OS
        self.df_Demographic = data.drop(data[data["Category"] == "Demographic"].index)
        self.df_Affordability = data.drop(data[data["Category"] == "Affordability"].index)
        self.df_Reliability = data.drop(data[data["Category"] == "Reliability"].index)
        self.df_Grid_flexibility = data.drop(data[data["Category" == "Grid Flexibility"]].index)
        self.df_Energy_efficency = data.drop(data[data["Category" == "Energy Efficency"]].index)
        self.df_Other = data

    def __add__(self, data):
        
        for i in range(len(data)):
            
            temp = data.at(i,"Category")
            
            if(temp == "Demographic"):
                self.df_Demographic.add(temp.iloc[[i]])
            
            elif(temp == "Affordability"):
                self.df_Affordability.add(temp.iloc[[i]])
            
            elif(temp == "Reliability"):
                self.df_Reliability.add(temp.iloc[[i]])
            
            elif(temp == "Grid Flexibility"):
                self.df_Grid_flexibility.add(temp.iloc[[i]])
            
            elif(temp == "Energy Efficency"):
                self.df_Energy_efficency.add(temp.iloc[[i]])
            else:
                self.df_Other.add(temp.iloc[[i]])

    def __remove__(self, id):
        pass

#How search is implemented is not the most important. Just make sure it makes sense :)
    def __search_by_Category__(self):
        pass

    def __search_by_in_category__(self, Category):
        pass

data = pd.read_csv("test_data.csv")
print(data)

test = Database
test.__init__(test,data=data)

