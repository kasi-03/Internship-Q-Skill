import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("iris.csv")

# Display first 5 rows
print(df.head())

# Basic Analysis
print("\nDataset Info:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())

# Average of Sepal Length
avg_sepal_length = df['sepal_length'].mean()
print("\nAverage Sepal Length:", avg_sepal_length)

# -----------------------
# Bar Chart
# -----------------------
species_avg = df.groupby('species')['sepal_length'].mean()

plt.figure(figsize=(6,4))
species_avg.plot(kind='bar')
plt.title("Average Sepal Length by Species")
plt.xlabel("Species")
plt.ylabel("Average Length")
plt.show()

# -----------------------
# Scatter Plot
# -----------------------
plt.figure(figsize=(6,4))
plt.scatter(df['sepal_length'], df['petal_length'])
plt.title("Sepal Length vs Petal Length")
plt.xlabel("Sepal Length")
plt.ylabel("Petal Length")
plt.show()

# -----------------------
# Heatmap
# -----------------------
plt.figure(figsize=(6,4))
corr = df.corr(numeric_only=True)

plt.imshow(corr, cmap='coolwarm')
plt.colorbar()

plt.xticks(range(len(corr.columns)), corr.columns, rotation=45)
plt.yticks(range(len(corr.columns)), corr.columns)

plt.title("Correlation Heatmap")
plt.show()