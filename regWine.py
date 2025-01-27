import pandas as pd
from ucimlrepo import fetch_ucirepo 
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.linear_model import LinearRegression
wine_quality = fetch_ucirepo(id=186) 

X = wine_quality.data.features 
y = wine_quality.data.targets 
total_missing = X.isnull().sum().sum()

print(pd.DataFrame(wine_quality.data.features, columns=wine_quality.feature_names))
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.9, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print('Pocet objektu trenovaci mnoziny: {}'.format(len(X_train)))
print('Pocet objektu testovaci mnoziny: {}'.format(len(X_test)))
print('Pocet chybejicich hodnot: {}'.format(total_missing))
print ("MAE: {}".format(mean_absolute_error(y_test, y_pred)))
print ("RMSE: {}".format(mean_squared_error(y_test, y_pred)))