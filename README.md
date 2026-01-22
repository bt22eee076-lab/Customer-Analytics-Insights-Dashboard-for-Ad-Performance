# Customer Analytics & Insights Dashboard for Ad Performance

## Overview
This project is a self-initiated analytics solution designed to transform raw advertising performance data into actionable insights. It simulates how customer and partner solutions teams analyze campaign performance, identify inefficiencies, and provide data-driven recommendations to improve outcomes.

The focus of the project is not visualization, but structured analysis, metric reasoning, and decision support using SQL and Python.

---

## Problem Statement
Advertisers often have access to large volumes of campaign data but struggle to answer key questions such as:
- Which campaigns are performing well?
- Which campaigns are wasting spend?
- What actions should be taken to improve results?

Manually inspecting raw metrics does not scale. This project demonstrates how structured analytics can support consistent and explainable decision-making.

---

## System Architecture

Campaign Performance Data (CSV)
↓
SQLite Database
↓
SQL KPI Computation
↓
Performance Classification
↓
Actionable Recommendations



---

## KPIs Used
| Metric | Description |
|-----|-------------|
| CTR | Measures ad engagement |
| Conversion Rate | Measures funnel efficiency |
| CPA | Measures cost effectiveness |

These metrics are commonly used to evaluate ad performance and optimization opportunities.

---

## Performance Classification Logic
| Condition | Classification |
|--------|----------------|
| High conversion rate and low CPA | GOOD |
| Conversions present but high CPA | AVERAGE |
| Clicks without conversions | POOR |
| No engagement | POOR |

Each classification is paired with a clear optimization recommendation.

---

## How to Run

``bash,
cd src,
python load_data.py,
python analytics.py

## Sample Output
Campaign: CAMP_001
Status: GOOD
Recommendation: Scale budget and maintain current strategy

Campaign: CAMP_005
Status: POOR
Recommendation: Investigate conversion tracking or landing page issues

## Design Considerations

SQL is used for analytical correctness and transparency.

Business logic is separated from data ingestion.

Recommendations are deterministic and explainable.

The system is designed for extension rather than visualization.
