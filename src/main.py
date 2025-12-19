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


X = df.drop("target", axis=1)
y = df["target"]

print("Shape X:", X.shape)
print("Shape y:", y.shape)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,y,
    test_size=0.2,
    random_state=42
)
print("Träningsdata:", X_train.shape)
print("Testdata:", X_test.shape)

from sklearn.linear_model import LogisticRegression

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)


from sklearn.metrics import accuracy_score, classification_report

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

print("\nClassification report:")
print(classification_report(y_test, y_pred))
