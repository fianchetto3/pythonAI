import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



from data_processing import DataProcessor
from model_traning import ModelTrainer

# 1. Data, skapa DataProcessor obejkt
processor = DataProcessor("data/heart.csv")

# läs upp och rensa data
df = processor.load_data()
df = processor.clean_data()

# 2. Modell
#  Skapar ett ModelTrainer objekt
trainer = ModelTrainer(df)

# förbereder träning och testdata
X_train, X_test, y_train, y_test = trainer.prepare_data()

# tränar modellen
trainer.train(X_train, y_train)

# utvärdera modellen
accuracy, report = trainer.evaluate(X_test, y_test)

print("Accuracy:", accuracy)
print(report)
