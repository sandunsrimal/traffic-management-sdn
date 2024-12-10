import pandas as pd

def preprocess_data(file_path):
    data = pd.read_csv(file_path)
    data.fillna(0, inplace=True)
    return data
