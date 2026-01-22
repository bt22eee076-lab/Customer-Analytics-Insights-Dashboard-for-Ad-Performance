import sqlite3

conn = sqlite3.connect("analytics.db")
cursor = conn.cursor()

print("\n--- Campaign Performance Classification & Insights ---")

query = """
SELECT
    campaign_id,
    impressions,
    clicks,
    conversions,
    cost,
    ROUND((clicks * 1.0 / impressions), 3) AS ctr,
    CASE 
        WHEN clicks > 0 THEN ROUND((conversions * 1.0 / clicks), 3)
        ELSE 0
    END AS conversion_rate,
    CASE
        WHEN conversions > 0 THEN ROUND((cost * 1.0 / conversions), 2)
        ELSE NULL
    END AS cpa
FROM campaign_performance;
"""

rows = cursor.execute(query).fetchall()

for row in rows:
    campaign_id, impressions, clicks, conversions, cost, ctr, conv_rate, cpa = row

    if clicks == 0:
        status = "POOR"
        recommendation = "Improve targeting or creatives to drive engagement"
    elif conversions == 0:
        status = "POOR"
        recommendation = "Investigate conversion tracking or landing page issues"
    elif conv_rate >= 0.05 and cpa <= 50:
        status = "GOOD"
        recommendation = "Scale budget and maintain current strategy"
    else:
        status = "AVERAGE"
        recommendation = "Optimize bidding strategy and reduce acquisition cost"

    print(f"""
Campaign: {campaign_id}
CTR: {ctr}
Conversion Rate: {conv_rate}
CPA: {cpa}
Status: {status}
Recommendation: {recommendation}
""")

conn.close()
