import pandas as pd

class DataProcessor:
    def __init__(self, filepath):
        # sparar sökvägen till csv filen
        self.filepath = filepath
        # lagra datan
        self.df = None

    def load_data(self):
         # läser csv filen till pandas 
         self.df = pd.read_csv(self.filepath)
         return self.df
        
    def clean_data(self):
        # Tar bort tomma värden i raderna 
        self.df = self.df.dropna()
        return self.df
            