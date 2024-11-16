# Importing libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.preprocessing import MinMaxScaler

# Load dataset
file_path = "ENB2012_data.xlsx"  # Replace with your file path
data = pd.read_excel(file_path)

# Preparing features and target
X = data.iloc[:, :-2]  # Features: X1 to X8
Y = data['Y1']         # Target: Heating Load (Y1)

# Normalizing features
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

# Splitting data
X_train, X_test, Y_train, Y_test = train_test_split(X_scaled, Y, test_size=0.2, random_state=42)
