from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

class ModelTrainer:
    def __init__(self, df):
        # tar emot färdig data
        self.df = df
        # Skapar modellen 
        self.model = LogisticRegression(max_iter=1000)

    def prepare_data(self):
         # X = alla kolumner utom target
         X = self.df.drop("target", axis=1)
         # y = target, det vi vill förutsäga
         y = self.df["target"]
         # delar upp i träning och test, 0.2 = 20% testdata, randomstate = samma split varje gång
         return train_test_split(X,y,test_size=0.2,random_state=42)
        
    def train(self,X_train, y_train):
            # lär modellen sambanden i träningsdatan
            self.model.fit(X_train, y_train)

    def evaluate(self, X_test, y_test):
        # modellen predictar på testdatan
        y_pred = self.model.predict(X_test)
        
        # hur många gissningar blev rätt
        accuracy = accuracy_score(y_test, y_pred)

        # utvärdering
        report = classification_report(y_test, y_pred)

        return accuracy, report