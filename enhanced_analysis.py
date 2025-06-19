import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset (change path if needed)
df = pd.read_csv("superstore_sales.csv", encoding='latin1')

# -------------------------------
# Basic Exploration
# -------------------------------
print("\nFirst 5 rows:")
print(df.head())

print("\nSummary:")
print(df.describe())

# Drop nulls
df.dropna(inplace=True)

# Convert Order Date to datetime
df["Order Date"] = pd.to_datetime(df["Order Date"])

# -------------------------------
# 1. Sales by Category
# -------------------------------
category_sales = df.groupby("Category")["Sales"].sum().reset_index()

plt.figure(figsize=(7, 4))
sns.barplot(x="Category", y="Sales", data=category_sales, palette="viridis")
plt.title("Total Sales by Category")
plt.tight_layout()
plt.show()

# -------------------------------
# 2. Sales by Region
# -------------------------------
region_sales = df.groupby("Region")["Sales"].sum().reset_index()

plt.figure(figsize=(7, 4))
sns.barplot(x="Region", y="Sales", data=region_sales, palette="mako")
plt.title("Total Sales by Region")
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()

# -------------------------------
# 3. Monthly Sales Trend
# -------------------------------
monthly_sales = df.resample('M', on='Order Date')["Sales"].sum().reset_index()

plt.figure(figsize=(10, 4))
plt.plot(monthly_sales["Order Date"], monthly_sales["Sales"], marker='o', linestyle='-')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True)
plt.tight_layout()
plt.show()

# -------------------------------
# 4. Profit vs Discount
# -------------------------------
plt.figure(figsize=(8, 5))
sns.scatterplot(x="Discount", y="Profit", data=df, hue="Category")
plt.title("Profit vs Discount by Category")
plt.tight_layout()
plt.show()