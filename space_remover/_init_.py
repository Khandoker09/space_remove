'''


'''
import pandas as pd 
import re


def spaceremover():
    fileinput = str(input("excel file path:"))
    df=pd.read_excel(fileinput,index_col=False)
    print(df.head(5))
    col_name=str(input('type col name:'))
    df[col_name]=df[col_name].astype('string')
    df[col_name]= df[col_name].astype('string') 
    df[col_name]=df[col_name].str.strip().replace(r'\s+',' ', regex=True)
    print(df.head(5))
if __name__ == "__main__":
           spaceremover()