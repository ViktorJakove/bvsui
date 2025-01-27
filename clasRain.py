import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.ensemble import RandomForestClassifier
path = './weatherAUS.csv'
data = pd.read_csv(path)

data['Day'] = pd.to_datetime(data['Date'], errors='coerce').dt.day
data['Month'] = pd.to_datetime(data['Date'], errors='coerce').dt.month
data['Year'] = pd.to_datetime(data['Date'], errors='coerce').dt.year
data.drop(columns=['Date'], inplace=True)

data.fillna(value={'RainToday': 'No', 'RainTomorrow': 'No'}, inplace=True)

input = ['Year', 'Month', 'Day', 'Location', 'MinTemp', 'MaxTemp', 'Rainfall', 'Evaporation', 
         'Sunshine', 'WindGustDir', 'WindGustSpeed', 'WindDir9am', 
         'WindDir3pm', 'WindSpeed9am', 'WindSpeed3pm', 'Humidity9am', 
         'Humidity3pm', 'Pressure9am', 'Pressure3pm', 'Cloud9am', 'Cloud3pm', 
         'Temp9am', 'Temp3pm', 'RainToday']
output = ['RainTomorrow']
X = data[input]
y = data[output].values.ravel()
categorical_cols = X.select_dtypes(include=['object']).columns.tolist()
X = pd.get_dummies(X, columns=categorical_cols, drop_first=True)
total_missing = X.isnull().sum().sum()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=50)
print('Pocet objektu trenovaci casti: {}'.format(len(X_train)))
print('Pocet objektu testovaci casti: {}'.format(len(X_test)))
print('Pocet chybejicich hodnot: {}'.format(total_missing))

rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)
rf_preds = rf_model.predict(X_test)
print("Uspesnost nahodnych lesu:")
print(classification_report(y_test, rf_preds))