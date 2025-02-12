import pandas as pd
from ucimlrepo import fetch_ucirepo
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.linear_model import LinearRegression
import numpy as np
communities_and_crime = fetch_ucirepo(id=183)

X = communities_and_crime.data.features
y = communities_and_crime.data.targets
X = X.replace('?', np.nan)
total_missing = X.isnull().sum().sum()

X = X.dropna()
y = y.loc[X.index]

numeric = X.select_dtypes(include=[np.number]).columns
X_train, X_test, y_train, y_test = train_test_split(X[numeric], y, test_size=0.9, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print('Pocet objektu trenovaci mnoziny: {}'.format(len(X_train)))
print('Pocet objektu testovaci mnoziny: {}'.format(len(X_test)))
print('Pocet chybejicich hodnot: {}'.format(total_missing))
print("MAE: {}".format(mean_absolute_error(y_test, y_pred)))
print("RMSE: {}".format(mean_squared_error(y_test, y_pred)))