
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import pickle
print(" Loading dataset...")
data = pd.read_csv(r"C:\Users\medac\OneDrive\Desktop\coverletter\house_prices.csv")  # change path to your CSV file
print(" Dataset loaded successfully!\n")

print("Here are the first 5 rows of the dataset:")
print(data.head(), "\n")
print(" Preprocessing data...")
data = data.dropna()
data = pd.get_dummies(data, columns=['Location'], drop_first=True)

print("Preprocessing complete!\n")
X = data.drop('Price', axis=1)
y = data['Price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print("Data split complete! (80% training, 20% testing)\n")

print(" Training Linear Regression model...")
model = LinearRegression()
model.fit(X_train, y_train)
print(" Model training complete!\n")

print("Evaluating model performance...")
y_pred = model.predict(X_test)
print("Mean Absolute Error (MAE):", mean_absolute_error(y_test, y_pred))
print("Mean Squared Error (MSE):", mean_squared_error(y_test, y_pred))
print("R² Score:", r2_score(y_test, y_pred), "\n")
print(" Testing with sample input...")
sample = [[2000, 3, 2, 1, 0, 0]]  
prediction = model.predict(sample)
print("Predicted House Price:", prediction[0], "\n")
pickle.dump(model, open('house_price_model.pkl', 'wb'))
print(" Model saved successfully as 'house_price_model.pkl'")
