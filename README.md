# E-Commerce Strategic Growth Analysis
**Technical Stack:** Python (Pandas), SQL (SQLite), Tableau

## 📌 Business Overview
This project analyzes a dataset of 10,000+ orders to identify the root causes of a significant revenue decline in Q3 2025. By building a reproducible data pipeline, I isolated a major "Concentration Risk" that threatened the company's stability.

## ⚙️ The Technical Pipeline
1. **Data Engineering (Python):** Resolved data type mismatches by converting string-based order dates into `datetime64[ns]` objects, ensuring chronological integrity for time-series analysis.
2. **SQL Analytics:** Leveraged SQL window functions to calculate:
   - **88.10% Repeat Purchase Rate** (Customer Loyalty)
   - **$159.58 Average Order Value** (Transaction Health)
3. **Visualization (Tableau):** Created an executive dashboard to pinpoint a **$20,000 revenue crash in August 2025**.

## 💡 Strategic Insights
- **The Problem:** The business is "top-heavy," with 50% of revenue coming from a single category (Electronics). 
- **The Crash:** The August decline was directly linked to a seasonal slump in tech sales, which the company had no "buffer" to absorb.
- **The Fix:** Recommended a **20% reallocation of marketing budget** toward the Sports and Home categories to diversify the revenue stream and build a stable financial floor.
