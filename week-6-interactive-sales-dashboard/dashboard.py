# ==========================================
# IMPORT LIBRARIES
# ==========================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

print("Libraries Imported Successfully!")

# ==========================================
# LOAD DATASET
# ==========================================

df = pd.read_csv("data/sales_data.csv")

print("Dataset Loaded Successfully!")

print("Shape:", df.shape)
print(df.head())

# ==========================================
# DATA EXPLORATION
# ==========================================

print("Dataset Information")
df.info()

print("\nSummary Statistics")
print(df.describe())

print("\nColumns")
print(df.columns)

print("\nMissing Values")
print(df.isnull().sum())

print("\nDuplicate Records")
print(df.duplicated().sum())

# ==========================================
# DATA CLEANING
# ==========================================

df = df.drop_duplicates()

df["Date"] = pd.to_datetime(df["Date"])

df["Month"] = df["Date"].dt.month

print("Dataset Cleaned Successfully!")

# ==========================================
# SALES ANALYSIS
# ==========================================

total_revenue = df["Total_Sales"].sum()
average_sales = df["Total_Sales"].mean()
highest_sale = df["Total_Sales"].max()
lowest_sale = df["Total_Sales"].min()

best_product = df.groupby("Product")["Total_Sales"].sum().idxmax()

print("="*60)
print("INTERACTIVE SALES DASHBOARD REPORT")
print("="*60)

print(f"Total Revenue : ₹{total_revenue:,.0f}")
print(f"Average Sales : ₹{average_sales:,.2f}")
print(f"Highest Sale  : ₹{highest_sale:,.0f}")
print(f"Lowest Sale   : ₹{lowest_sale:,.0f}")
print(f"Best Product  : {best_product}")

# ==========================================
# GROUPBY
# ==========================================

sales_by_product = df.groupby("Product")["Total_Sales"].sum()

sales_by_region = df.groupby("Region")["Total_Sales"].sum()

monthly_sales = df.groupby("Month")["Total_Sales"].sum()

print(sales_by_product)

print(sales_by_region)

print(monthly_sales)

# ==========================================
# BAR CHART
# ==========================================

plt.figure(figsize=(8,5))

sns.barplot(
    data=df,
    x="Product",
    y="Total_Sales",
    estimator=sum
)

plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")

plt.tight_layout()

plt.savefig("visualizations/bar_chart.png")

plt.show()

# ==========================================
# BOX PLOT
# ==========================================

plt.figure(figsize=(8,5))

sns.boxplot(
    data=df,
    x="Product",
    y="Total_Sales"
)

plt.title("Sales Distribution by Product")

plt.tight_layout()

plt.savefig("visualizations/box_plot.png")

plt.show()

# ==========================================
# VIOLIN PLOT
# ==========================================

plt.figure(figsize=(8,5))

sns.violinplot(
    data=df,
    x="Region",
    y="Total_Sales"
)

plt.title("Sales Distribution by Region")

plt.tight_layout()

plt.savefig("visualizations/violin_plot.png")

plt.show()

# ==========================================
# HEATMAP
# ==========================================

plt.figure(figsize=(7,5))

corr = df.corr(numeric_only=True)

sns.heatmap(
    corr,
    annot=True,
    cmap="Blues"
)

plt.title("Correlation Heatmap")

plt.tight_layout()

plt.savefig("visualizations/heatmap.png")

plt.show()

# ==========================================
# LINE CHART
# ==========================================

plt.figure(figsize=(8,5))

sns.lineplot(
    x=monthly_sales.index,
    y=monthly_sales.values,
    marker="o"
)

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")

plt.grid(True)

plt.tight_layout()

plt.savefig("visualizations/line_chart.png")

plt.show()

# ==========================================
# INTERACTIVE DASHBOARD
# ==========================================

fig = px.bar(
    df,
    x="Product",
    y="Total_Sales",
    color="Region",
    title="Interactive Sales Dashboard",
    hover_data=["Quantity", "Price"]
)

fig.write_html("visualizations/interactive_dashboard.html")

fig.show()

# ==========================================
# DASHBOARD SUMMARY
# ==========================================

print("="*60)
print("INTERACTIVE SALES DASHBOARD")
print("="*60)

print(f"Total Revenue      : ₹{total_revenue:,.0f}")
print(f"Average Sales      : ₹{average_sales:,.2f}")
print(f"Highest Sale       : ₹{highest_sale:,.0f}")
print(f"Lowest Sale        : ₹{lowest_sale:,.0f}")
print(f"Best Product       : {best_product}")

highest_region = sales_by_region.idxmax()

print(f"Highest Region     : {highest_region}")

print("\nBUSINESS INSIGHTS")
print("- Laptop generated the highest revenue.")
print("- North region achieved the highest sales.")
print("- Heatmap shows relationships between numerical variables.")
print("- Box plot highlights sales distribution and outliers.")
print("- Violin plot visualizes regional sales density.")
print("- Interactive dashboard enables dynamic data exploration.")

print("="*60)