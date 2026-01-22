import csv
import sqlite3

conn = sqlite3.connect("analytics.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS campaign_performance (
    campaign_id TEXT,
    impressions INTEGER,
    clicks INTEGER,
    conversions INTEGER,
    cost REAL
)
""")

with open("../data/campaign_performance.csv", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        cursor.execute("""
            INSERT INTO campaign_performance
            VALUES (?, ?, ?, ?, ?)
        """, (
            row["campaign_id"],
            int(row["impressions"]),
            int(row["clicks"]),
            int(row["conversions"]),
            float(row["cost"])
        ))

conn.commit()
conn.close()

print("Campaign performance data loaded successfully.")
