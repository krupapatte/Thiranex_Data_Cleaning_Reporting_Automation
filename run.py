import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent
RAW = ROOT / "data" / "raw_data.csv"
OUT = ROOT / "output"
CHARTS = OUT / "charts"
OUT.mkdir(exist_ok=True)
CHARTS.mkdir(exist_ok=True)

# 1. Read source data
df = pd.read_csv(RAW)
original_rows = len(df)

# 2. Standardize text fields
text_cols = ["Name", "Email", "City"]
for col in text_cols:
    df[col] = df[col].fillna("").astype(str).str.strip()

df["City"] = df["City"].str.title()
df["Email"] = df["Email"].str.lower()

# 3. Convert data types
df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")
df["Sales"] = pd.to_numeric(df["Sales"], errors="coerce")

# 4. Handle missing values
missing_before = int(df.isna().sum().sum())
df["Sales"] = df["Sales"].fillna(df["Sales"].median())
df["Email"] = df["Email"].replace("", "not_provided@example.com")
missing_after = int(df.isna().sum().sum())

# 5. Remove duplicate Customer IDs (keep first occurrence)
duplicates_removed = int(df.duplicated(subset=["Customer ID"], keep="first").sum())
df = df.drop_duplicates(subset=["Customer ID"], keep="first")

# 6. Create a simple sales category
df["Sales Category"] = pd.cut(
    df["Sales"],
    bins=[-1, 5000, 8000, float("inf")],
    labels=["Low", "Medium", "High"]
)

# 7. Save cleaned data
df.to_csv(OUT / "cleaned_data.csv", index=False)

# 8. Create summary tables
city_summary = (
    df.groupby("City", as_index=False)["Sales"]
      .agg(["sum", "mean", "count"])
      .reset_index()
      .rename(columns={"sum":"Total Sales", "mean":"Average Sales", "count":"Orders"})
)
city_summary.to_csv(OUT / "city_summary.csv", index=False)

summary = pd.DataFrame({
    "Metric": [
        "Rows before cleaning", "Rows after cleaning", "Duplicates removed",
        "Missing cells before cleaning", "Missing cells after cleaning",
        "Total sales", "Average sales"
    ],
    "Value": [
        original_rows, len(df), duplicates_removed,
        missing_before, missing_after,
        round(df["Sales"].sum(), 2), round(df["Sales"].mean(), 2)
    ]
})
summary.to_csv(OUT / "report_summary.csv", index=False)

# 9. Create a simple visual summary
plt.figure(figsize=(8, 5))
city_sales = df.groupby("City")["Sales"].sum().sort_values(ascending=False)
city_sales.plot(kind="bar")
plt.title("Total Sales by City")
plt.xlabel("City")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig(CHARTS / "sales_by_city.png", dpi=150)
plt.close()

# 10. Create a readable text report
with open(OUT / "report.txt", "w", encoding="utf-8") as f:
    f.write("DATA CLEANING & REPORTING AUTOMATION REPORT\n")
    f.write("=" * 48 + "\n\n")
    f.write(f"Rows before cleaning : {original_rows}\n")
    f.write(f"Rows after cleaning  : {len(df)}\n")
    f.write(f"Duplicates removed   : {duplicates_removed}\n")
    f.write(f"Missing cells before : {missing_before}\n")
    f.write(f"Missing cells after  : {missing_after}\n")
    f.write(f"Total sales          : {df['Sales'].sum():.2f}\n")
    f.write(f"Average sales        : {df['Sales'].mean():.2f}\n\n")
    f.write("Cleaning steps:\n")
    f.write("1. Trimmed extra spaces from text fields.\n")
    f.write("2. Standardized city names and email case.\n")
    f.write("3. Converted dates and sales to correct data types.\n")
    f.write("4. Filled missing sales using the median.\n")
    f.write("5. Filled missing email with a standard placeholder.\n")
    f.write("6. Removed duplicate customer IDs.\n")
    f.write("7. Added a simple sales category.\n")
    f.write("8. Generated summary tables and a chart.\n")

print("Cleaning and reporting completed.")
print(f"Cleaned rows: {len(df)}")
