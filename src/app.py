import pandas as pd

class AppInterface:
    def __init__(self, model):
        self.model = model

    def get_user_input(self):
        print("Mata in patientdata:")

        age = int(input("Ålder: "))
        sex = int(input("Kön (0 = kvinna, 1 = man): "))
        cp = int(input("Bröstsmärta (0–3): "))
        trestbps = int(input("Vilo-blodtryck: "))
        chol = int(input("Kolesterol: "))
        fbs = int(input("Fastande blodsocker > 120 (0 = nej, 1 = ja): "))
        restecg = int(input("EKG-resultat (0–2): "))
        thalach = int(input("Maxpuls: "))
        exang = int(input("Ansträngningsutlöst angina (0 = nej, 1 = ja): "))
        oldpeak = float(input("ST-depression (oldpeak): "))
        slope = int(input("Lutning ST (0–2): "))
        ca = int(input("Antal färgade kärl (0–3): "))
        thal = int(input("Thal (1–3): "))
        return pd.DataFrame([{
            "age": age,
            "sex": sex,
            "cp": cp,
            "trestbps": trestbps,
            "chol": chol,
            "fbs": fbs,
            "restecg": restecg,
            "thalach": thalach,
            "exang": exang,
            "oldpeak": oldpeak,
            "slope": slope,
            "ca": ca,
            "thal": thal
        }])
    def run(self):
        user_data = self.get_user_input()

        prediction = self.model.predict(user_data)[0]
        
        proba = self.model.predict_proba(user_data)[0][1]
        print(f"Sannolikhet för hjärtsjukdom: {proba:.2f}")

        print("\nResultat:")


        if proba >= 0.7:
            print("Hög risk för hjärtsjukdom")
        elif proba >= 0.4:
            print("Måttlig risk för hjärtsjukdom")
        else:
          print("Låg risk för hjärtsjukdom")
    
     

       