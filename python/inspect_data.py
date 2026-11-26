
import pandas as pd

from pathlib import Path

project_folder = Path(__file__).resolve().parent.parent
file_path = project_folder / "data" / "support-tickets.csv"

df = pd.read_csv(file_path)
df.columns = df.columns.str.strip()
df["channel"] = df["channel"].str.strip()
df["queue"] = df["queue"].str.strip()
df["priority"] = df["priority"].str.strip()
df["reopened"] = df["reopened"].str.strip()
df["first_response_min"] = df["first_response_min"].str.strip().replace("", pd.NA)

df["resolved_at"] = df["resolved_at"].str.strip().replace("", pd.NA)

df["csat"] = df["csat"].str.strip().replace("", pd.NA)
df["opened_at"] = pd.to_datetime(df["opened_at"])

df["resolved_at"] = pd.to_datetime(df["resolved_at"])

df["first_response_min"] = pd.to_numeric(df["first_response_min"])

df["csat"] = pd.to_numeric(df["csat"])

print("Dataset loaded successfully!")
print("\nColumn names:")
print(df.columns.tolist())

print("\nFirst 5 rows:")
print(df.head())
print("\nDataset shape:")
print(df.shape)

print("\nData types:")
print(df.dtypes)

print("\nMissing values:")
print(df.isnull().sum())
print("\nSample values for date and numeric columns:")

print("\nopened_at:")
print(df["opened_at"].head())

print("\nfirst_response_min:")
print(df["first_response_min"].head())

print("\nresolved_at:")
print(df["resolved_at"].head())

print("\ncsat:")
print(df["csat"].head())
cleaned_file_path = project_folder / "data" / "support-tickets-cleaned.csv"

df.to_csv(cleaned_file_path, index=False, na_rep="NA")

print("\nCleaned dataset saved successfully!")
check_df = pd.read_csv(cleaned_file_path)

print("\nCSAT values in saved file:")
print(check_df["csat"].head(10))