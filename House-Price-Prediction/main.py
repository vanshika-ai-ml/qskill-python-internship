import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score 
# Load the dataset
data = pd.read_csv("House-Price-Prediction/train.csv")

print("Dataset loaded successfully!")
print(data.head())
print("\nDataset shape:", data.shape)
# Select features and target
features = ["OverallQual", "GrLivArea", "GarageCars", "TotalBsmtSF", "FullBath", "YearBuilt"]

X = data[features]
y = data["SalePrice"]

print("\nSelected features:")
print(features)
print("Missing values:", X.isnull().sum().sum())
# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create and train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

print("\nModel trained successfully!")
print("Training samples:", X_train.shape[0])
print("Testing samples:", X_test.shape[0])
# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print("\nModel Evaluation:")
print("Mean Absolute Error (MAE):", round(mae, 2))
print("Mean Squared Error (MSE):", round(mse, 2))
print("Root Mean Squared Error (RMSE):", round(rmse, 2))
print("R2 Score:", round(r2, 4))
# Visualize Actual vs Predicted Prices
plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred, alpha=0.6, color="royalblue")

plt.xlabel("Actual House Price")
plt.ylabel("Predicted House Price")
plt.title("Actual vs Predicted House Prices")

# Perfect prediction reference line
plt.plot(
    [y_test.min(), y_test.max()],
    [y_test.min(), y_test.max()],
    linestyle="--"
)

plt.tight_layout()
plt.show()
# Predict price for a new house
print("\n--- House Price Prediction ---")

overall_qual = int(input("Enter overall quality (1-10): "))
gr_liv_area = float(input("Enter above-ground living area (sq ft): "))
garage_cars = int(input("Enter garage capacity (number of cars): "))
total_bsmt_sf = float(input("Enter total basement area (sq ft): "))
full_bath = int(input("Enter number of full bathrooms: "))
year_built = int(input("Enter year built: "))

new_house = pd.DataFrame(
    [[overall_qual, gr_liv_area, garage_cars, total_bsmt_sf, full_bath, year_built]],
    columns=features
)

predicted_price = model.predict(new_house)[0]

print("\nEstimated House Price: ${:,.2f}".format(predicted_price))
print("Prediction Completed Successfully!")