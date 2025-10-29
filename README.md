# 🧾 Vendor Performance & Profitability Analysis – SQL | Python | Power BI

A complete **data analytics project** analyzing vendor sales, purchases, and freight performance to identify profitability trends and improve inventory efficiency.

---

## 📊 Project Dashboard Preview

**Vendor Performance Dashboard**

*Figure:* Power BI Dashboard showing total sales, purchase, profit margin, unsold inventory, and vendor performance insights.

---

## 📌 Table of Contents
1. [Overview](#-overview)
2. [Business Objective](#-business-objective)
3. [Dataset](#-dataset)
4. [Tools & Technologies](#-tools--technologies)
5. [Project Architecture](#-project-architecture)
6. [Data Preparation](#-data-preparation)
7. [Exploratory Data Analysis (EDA)](#-exploratory-data-analysis-eda)
8. [Statistical Insights](#-statistical-insights)
9. [Dashboard](#-dashboard)
10. [How to Run the Project](#-how-to-run-this-project)
11. [Recommendations](#-recommendations)
12. [Author](#-author)

---

## 📊 Overview
This project focuses on analyzing **vendor performance** using retail sales and inventory data.  
The goal is to identify **high-performing vendors**, detect inefficiencies, and suggest **data-driven procurement strategies**.

A complete data pipeline was built using:
- **Python** for data processing  
- **SQL** for database management  
- **Power BI** for interactive dashboarding

---

## 🎯 Business Objective
- Evaluate vendor contribution to overall profit  
- Identify under- or over-performing suppliers  
- Detect high freight costs affecting profit margins  
- Statistically validate if vendor type (Top vs Low) significantly affects margin

---

## 🧩 Dataset
- Multiple CSV files located in the **`/sale_data/`** folder (`sales.csv`, `purchase.csv`, `inventory.csv`)
- Summary table created from ingested data and used for analysis

**Processing Pipeline:**
1. `ingestion_db.py` → Data ingestion into SQLite  
2. `sale_summary_script.py` → Vendor summary table creation  
3. `vendor_summary_data.csv` → Final clean dataset for analysis

---

## 🛠️ Tools & Technologies

| Category | Tools |
|-----------|--------|
| **Database** | SQLite, SQLAlchemy |
| **Programming** | Python (Pandas, NumPy, SciPy, Matplotlib, Seaborn) |
| **Visualization** | Power BI |
| **Version Control** | Git, GitHub |
| **Logging** | Python Logging module |

---

## ⚙️ Project Architecture

vendor-performance-analysis/
├── README.md
├── ingestion_db.py # Data ingestion into SQLite
├── sale_summary_script.py # Vendor summary table creation
├── sale_data/ # Raw CSV datasets
│ ├── sales.csv
│ ├── purchase.csv
│ └── inventory.csv
├── notebooks/
│ ├── eda_Vendor_sale_summary_analysis.ipynb
│ └── vendor_performance_Analysis.ipynb
├── dashboard/
│ └── vendor_performance_analysis.pbix
├── reports/
│ └── Vendor_Performance_Analysis_Report.pdf
└── logs/
└── ingestion_db.log

---

## 🧹 Data Preparation
**Cleaning Steps:**
- Removed records with:
  - Missing or zero sales quantities  
  - Profit margin ≤ 0  
  - Negative gross profit  
- Merged vendor and sales tables  
- Created key features:
  - `Gross Profit`
  - `Margin %`
  - `Freight-to-Sales Ratio`
  - `Turnover Rate`

---

## 🔍 Exploratory Data Analysis (EDA)
### Key Findings:
- Vendors with high sales volume showed **lower margin** but stable profit.  
- Low vendors had **higher margins (~42%)** but high variability.  
- Top vendors were consistent (~31%) with tighter confidence intervals.  
- Correlation between purchase qty and sales qty ≈ **0.99**  
- Outliers in **freight** and **purchase price** identified.  

---

## 📊 Statistical Insights

| Test | Result | Interpretation |
|------|---------|----------------|
| **Shapiro–Wilk** | p = 0.000 | Non-normal data |
| **Levene’s Test** | p = 0.000 | Unequal variances |
| **T-Test** | p = 0.000 | Mean difference significant |
| **Cohen’s d** | -0.538 | Medium effect size |

✅ **Conclusion:**  
There is a statistically significant difference between top and low vendor profit margins.

---

## 📈 Dashboard (Power BI)
Interactive insights include:
- Vendor-wise margin and sales analysis  
- Inventory turnover visualization  
- Freight vs Profit heatmaps  
- High vs Low vendor comparison  

**File:** `dashboard/vendor_performance_analysis.pbix`

---

## 💻 How to Run This Project

```bash
# Step 1: Clone repo
git clone https://github.com/yourusername/vendor-performance-analysis.git
cd vendor-performance-analysis

# Step 2: Run ingestion script
python ingestion_db.py

# Step 3: Generate vendor summary table
python sale_summary_script.py

# Step 4: Open Jupyter notebooks for analysis
jupyter notebook notebooks/eda_Vendor_sale_summary_analysis.ipynb
jupyter notebook notebooks/vendor_performance_Analysis.ipynb

# Step 5: View dashboard
# Open Power BI → Load dashboard/vendor_performance_analysis.pbix
🧭 Recommendations

Balance high-volume (top) and high-margin (low) vendors.

Reduce freight costs via better contract negotiation.

Automate vendor monitoring using Python alerts.

Use Power BI to track vendor KPIs monthly.

👨‍💻 Author

Pawan Kumar Prajapati
Data Analyst | SQL • Python • Power BI

📧 Email: pawankumar231314@gmail.com

🔗 LinkedIn: Pawan Kumar Prajapati