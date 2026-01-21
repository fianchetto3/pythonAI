# Heart disease med hjälp av AI 
Detta projekt är baserat på datasetet Heart.csv och använder sig av Machine learning för att kunna förutspå ifall en patient kan ha hjärtsjukdom. Träffsäkerheten ligger på nästan 80%. 

## Verktyg
Python är såklart språket som använts i projektet tillsammans med olika bibliotek.

- Pandas används för att läsa in datasetet, rensa data och hantera tabeller. 

- MatPlotlib användes för att visualisera med diagram.

- Seaborn bygger tillsammans med MatPlotLib och gör mer informativa och snyggare grafer

- Scikit-learn är det vikitgaste bibliotektet i projektet och hanterar träning och modellen, exempelvis
- train_test_split - delar upp data i träning och testmängd
- LogisticRegression - ML modellen
- accuracy_score - utvärdering och visualisering av modellens träffsäkerhet

Projektet är byggt med ett OOP tänk och har olika klasser som hanterar olika delar
- DataProccessor - Hanterar läsning och resning av data
- ModelTrainer - Tränar och utvärderar modellen
- AppInterface - Hanterar användarinmatning i terminalen


## Filstruktur

Projektet är uppdelat i mappar

data/heart.csv - datan
src/ 
- app.py - app byggd för terminalen
- data_proccessing.py - hanterar att öppna .csv, rensa (dropna) och läsa filen 
- main.py - huvudfilen i projektet, genom att köra mainfilen körs projektets alla delar. 
- model_traning.py - Klassen ModelTrainer som sköter hur modellen tränas på datan.


## Hur Projektet körs 

Kör projektet genom att köra filen main.py. Då kommer appen starta i terminalen där användaren skriver in värderna som efterfrågas. 
Efter User Inputs kommer svaret visas där modellen har gjort en prediciton baserat på värderna och datan den är tränad på. 

Bibliotek i projektet: 
- Pandas
- MatPlotlib
- Seaborn
- Scikit-learn


## Lärdomar 
Detta är första gången jag använder spårket Python i ett projekt vilket har varit den största lärdomen för mig, samt att anävnda det i syfte för ML. 
ML och AI är två väldigt stora områden och detta har varit en bra introduktion till det. 
OOP programering är något jag är van med då jag har förkunskaper ifrån C#. 

