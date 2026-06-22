import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# Load dataset
df = pd.read_csv("Housing.csv")

# Convert categorical variables
df = pd.get_dummies(df, drop_first=True)

# Features and target
X = df.drop("price", axis=1)
y = df["price"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
predictions = model.predict(X_test)

# Evaluation
mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print("Mean Absolute Error:", mae)
print("R2 Score:", r2)

# Example Prediction
sample = X_test.iloc[[0]]
predicted_price = model.predict(sample)

print("Predicted Price:", predicted_price[0])
print("Actual Price:", y_test.iloc[0])

# -----------------------------
# Graph 1: Actual vs Predicted
# -----------------------------
plt.figure(figsize=(8,6))
plt.scatter(y_test, predictions)

plt.xlabel("Actual House Prices")
plt.ylabel("Predicted House Prices")
plt.title("Actual vs Predicted House Prices")

# Perfect prediction line
plt.plot(
    [y_test.min(), y_test.max()],
    [y_test.min(), y_test.max()],
    'r--'
)

plt.show()

# -----------------------------
# Graph 2: Prediction Errors
# -----------------------------
errors = y_test - predictions

plt.figure(figsize=(8,6))
plt.hist(errors, bins=20)

plt.title("Distribution of Prediction Errors")
plt.xlabel("Error")
plt.ylabel("Frequency")

plt.show()

# -----------------------------
# Graph 3: Area vs Price
# -----------------------------
plt.figure(figsize=(8,6))
plt.scatter(df['area'], df['price'])

plt.xlabel("Area")
plt.ylabel("Price")
plt.title("Area vs House Price")

plt.show()