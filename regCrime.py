import pandas as pd
from ucimlrepo import fetch_ucirepo
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

# Fetch dataset
communities_and_crime = fetch_ucirepo(id=183)

# Data (as pandas dataframes)
X = communities_and_crime.data.features
y = communities_and_crime.data.targets

# Replace '?' with NaN in the entire DataFrame
X.replace('?', np.nan, inplace=True)

# Drop rows with any missing values
X = X.dropna()
y = y.loc[X.index]  # Ensure the target variable matches the filtered features

# Metadata
#print(communities_and_crime.metadata)

# Variable information
print(communities_and_crime.variables)

# Identify numeric columns
numeric_columns = X.select_dtypes(include=[np.number]).columns

# Splitting the dataset into the Training set and Test set
X_train, X_test, y_train, y_test = train_test_split(X[numeric_columns], y, test_size=0.2, random_state=42)

# Initialize and train the model
model = RandomForestRegressor(n_estimators=100)
model.fit(X_train, y_train)

# Predict the test set results
y_pred = model.predict(X_test)

# Print evaluation metrics
print("MAE: {}".format(mean_absolute_error(y_test, y_pred)))
print("RMSE: {}".format(mean_squared_error(y_test, y_pred, squared=False)))

# Example of predicting criminality in new areas
# Assuming new_areas is a DataFrame with the same structure as X
new_areas = pd.DataFrame({
    # Add the appropriate feature columns here
    # Example:
    'population': [5000, 10000],
    'household_size': [2.5, 3.0],
    # Add all other necessary features
})

# Predict criminality in new areas
new_predictions = model.predict(new_areas[numeric_columns])
print("Predicted criminality in new areas:", new_predictions)