import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data (with proper encoding)
df = pd.read_csv("/Users/rahulkumarbhagat/sales _data_analysis/superstore_sales.csv", encoding='latin1')

# Preview data
print("First 5 rows:")
print(df.head())

# Drop nulls
df.dropna(inplace=True)

# Total sales by category
category_sales = df.groupby("Category")["Sales"].sum().reset_index()

# Plot
sns.barplot(x="Category", y="Sales", data=category_sales)
plt.title("Total Sales by Category")
plt.show()