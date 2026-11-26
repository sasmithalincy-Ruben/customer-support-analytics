import pandas as pd
import sqlite3
from pathlib import Path

project_folder = Path(__file__).resolve().parent.parent

csv_path = project_folder / "data" / "support-tickets-cleaned.csv"
db_path = project_folder / "data" / "support_tickets.db"

df = pd.read_csv(csv_path)

connection = sqlite3.connect(db_path)

df.to_sql("support_tickets", connection, if_exists="replace", index=False)

connection.close()

print("Data loaded into SQLite successfully!")