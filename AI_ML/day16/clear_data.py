import pandas as pd

def clear_data():
    df=pd.DataFrame({'name':[],'enc':[]})
    fname='features.csv'
    df.to_csv(fname)