import pandas as pd

df = pd.read_csv("sales_data.xlsx.csv")

print(df.head())
print(df.info())
print(df.describe())
# Remove duplicate rows
df = df.drop_duplicates()

# Check missing values
print(df.isnull().sum())

# Remove missing values (simple way)
df = df.dropna()
df['Order Date'] = pd.to_datetime(df['Order Date'])
df.columns = df.columns.str.strip()
# Total Sales
print("Total Sales:", df['Sales'].sum())

# Total Profit
print("Total Profit:", df['Profit'].sum())

# Sales by Region
print(df.groupby('Region')['Sales'].sum())

# Profit by Category
print(df.groupby('Category')['Profit'].sum())
import matplotlib.pyplot as plt

df.groupby('Region')['Sales'].sum().plot(kind='bar')
plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.show()
df['Month'] = df['Order Date'].dt.month

monthly_sales = df.groupby('Month')['Sales'].sum()

monthly_sales.plot(kind='line', marker='o')
plt.title("Monthly Sales Trend")
plt.show()
top_products = df.groupby('Sub-Category')['Sales'].sum().sort_values(ascending=False).head(10)

top_products.plot(kind='bar')
plt.title("Top 10 Products by Sales")
plt.xticks(rotation=45)

plt.savefig("top_products.png")
plt.close()
df.groupby('Category')['Profit'].sum().plot(kind='bar')

plt.title("Profit by Category")

plt.savefig("profit_category.png")
plt.close()
import seaborn as sns

sns.scatterplot(x=df['Discount'], y=df['Profit'])

plt.title("Discount vs Profit")

plt.savefig("discount_vs_profit.png")
plt.close()
df['Year'] = df['Order Date'].dt.year

yearly_sales = df.groupby('Year')['Sales'].sum()

yearly_sales.plot(kind='line', marker='o')

plt.title("Yearly Sales Trend")

plt.savefig("yearly_sales.png")
plt.close()
df.groupby('Region')['Profit'].sum().plot(kind='bar')

plt.title("Profit by Region")

plt.savefig("profit_region.png")
plt.close()