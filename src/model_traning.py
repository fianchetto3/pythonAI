from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

class ModelTrainer:
    def __init__(self, df):
        self.df = df
        self.model = LogisticRegression(max_iter=1000)

    def prepare_data(self):
         X = self.df.drop("target", axis=1)
         y = self.df["target"]
         return train_test_split(X,y,test_size=0.2,random_state=42)
        
    def train(self,X_train, y_train):
            self.model.fit(X_train, y_train)

    def evaluate(self, X_test, y_test):
        y_pred = self.model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        report = classification_report(y_test, y_pred)
        return accuracy, report