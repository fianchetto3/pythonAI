import pandas as pd

class DataProcessor:
    def __init__(self, filepath):
        self.filepath = filepath
        self.df = None

    def load_data(self):
         self.df = pd.read_csv(self.filepath)
         return self.df
        
    def clean_data(self):
        self.df = self.df.dropna()
        return self.df
            