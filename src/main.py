import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Läs in data från csv filen
df = pd.read_csv("data/heart.csv")

# inspektion av datan 
print(df.info())
print("\nSaknade värden per kolumn:")
print(df.isna().sum())

# Tar bort tomma rader ifall det finns
df = df.dropna() 

print("Shape efter rensning:", df.shape)

# EDA grafer

# hur många som har hjärtsjukdom eller inte
sns.countplot(x="target", data=df)
plt.title("Fördelning av hjärtsjukdom")
plt.show()

# åldersfördelning på datan
plt.figure(figsize=(6,4))
sns.histplot(df["age"], bins=20)
plt.title("Åldersfördelning")
plt.xlabel("Ålder")
plt.ylabel("Antal")

plt.show()