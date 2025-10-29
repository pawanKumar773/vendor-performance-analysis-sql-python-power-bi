🧾 Vendor Performance & Profitability Analysis – SQL | Python | Power BI

A complete data analytics project analyzing vendor sales, purchases, and freight performance to identify profitability trends and improve inventory efficiency.

📊 Dashboard Preview
<p align="center"> <img src="dashboard/Dashboard_1.png" alt="Vendor Performance Dashboard" width="800"> </p>

🗂️ Dashboard File:
dashboard/vendor_performance_analysis.pbix

📌 Table of Contents

Overview

Business Objective

Dataset

Tools & Technologies

Project Architecture

Data Preparation

Exploratory Data Analysis (EDA)

Statistical Insights

Dashboard

How to Run This Project

Recommendations

Author

🔍 Overview

This project focuses on analyzing vendor performance using retail sales and inventory data.
The goal is to identify high-performing vendors, detect inefficiencies, and suggest data-driven procurement strategies.

A complete analytics pipeline was built using:

Python for data processing

SQL for data management

Power BI for visualization

🎯 Business Objective

Evaluate vendor contribution to overall profit

Identify under- or over-performing suppliers

Detect high freight costs affecting profit margin

Statistically validate whether vendor type (Top vs Low) significantly affects profitability
🧩 Dataset

The dataset consists of three main CSV files located in the /sale_data/ folder:
/sale_data/
│
├── sales.csv
├── purchase.csv
└── inventory.csv
🧾 1. sales.csv
Column Name	Description	Insight
vendor_id	Unique ID for each vendor	Used to join with vendor and purchase data
invoice_no	Unique sales transaction number	Helps track transaction-level performance
sales_qty	Number of units sold	High values indicate top-performing vendors
sales_price	Selling price per unit	Used to compute total sales and revenue
freight_cost	Cost of shipping goods	High freight cost reduces overall margin
gross_profit	Profit before taxes	Main indicator of profitability
margin_percent	Profit margin percentage	Key performance metric used for comparison

📊 Conclusion:

Vendors with high sales_qty have consistent but lower margin_percent.

freight_cost heavily impacts profit — high freight cost reduces margin significantly.

🧾 2. purchase.csv
Column Name	Description	Insight
vendor_id	Supplier identifier	Common key for merging datasets
purchase_qty	Quantity of goods purchased	Helps analyze demand vs. supply
purchase_price	Cost price per unit	Used for calculating profit margins
purchase_date	Date of procurement	Used to calculate lead time and inventory flow

📊 Conclusion:

Strong correlation (≈0.99) between purchase_qty and sales_qty shows efficient inventory planning.

Vendors with frequent small purchases tend to maintain better inventory turnover.

🧾 3. inventory.csv
Column Name	Description	Insight
vendor_id	Vendor identifier	Links to sales & purchase data
opening_stock	Units available at start	Used for turnover and stock analysis
closing_stock	Units available at end	Indicates unsold inventory
unsold_inventory	Calculated as difference between stock & sales	High unsold inventory shows inefficiency

📊 Conclusion:

Vendors with low unsold inventory indicate better stock management.

Some low-margin vendors compensate with faster stock turnover.

🧩 Combined Data Model

After merging these three files, new features were engineered:

Gross Profit = Sales – Purchase – Freight

Margin% = (Gross Profit / Sales) × 100

Freight-to-Sales Ratio = Freight / Sales

Turnover Rate = Sales Quantity / Average Inventory

Final processed data is stored as:
vendor_summary_data.csv
🛠️ Tools & Technologies
Category	Tools
Database	SQLite, SQLAlchemy
Programming	Python (Pandas, NumPy, SciPy, Matplotlib, Seaborn)
Visualization	Power BI
Version Control	Git, GitHub
Logging	Python Logging module
⚙️ Project Architecture
vendor-performance-analysis/
│
├── README.md
│
├── ingestion_db.py                  # Data ingestion into SQLite
├── sale_summary_script.py           # Vendor summary table creation
│
├── sale_data/                       # Raw CSV datasets
│   ├── sales.csv
│   ├── purchase.csv
│   └── inventory.csv
│
├── notebooks/
│   ├── eda_Vendor_sale_summary_analysis.ipynb
│   └── vendor_performance_Analysis.ipynb
│
├── dashboard/
│   ├── Dashboard_1.png
│   └── vendor_performance_analysis.pbix
│
├── reports/
│   └── Vendor_Performance_Analysis_Report.pdf
│
└── logs/
    └── ingestion_db.log
🧹 Data Preparation

Removed invalid records:

Missing or zero sales_qty

Profit margin ≤ 0

Negative gross_profit

Created new columns:

Gross_Profit

Margin_%

Freight_to_Sales_Ratio

Turnover_Rate

🔬 Exploratory Data Analysis (EDA)

Key Insights:

High-volume vendors show lower but stable margins.

Low vendors show high margin (~42%) but inconsistent profits.

freight_cost is inversely correlated with profit.

Detected multiple outliers in freight and purchase costs.

📈 Statistical Insights
Test	Result	Interpretation
Shapiro–Wilk	p = 0.000	Non-normal data
Levene’s Test	p = 0.000	Unequal variances
T-Test	p = 0.000	Mean difference significant
Cohen’s d	−0.538	Medium effect size

✅ Conclusion:
There is a statistically significant difference between top and low vendor profit margins.

📊 Dashboard

Interactive Insights Include:

Vendor-wise margin and sales comparison

Inventory turnover visualization

Freight vs Profit heatmaps

High vs Low vendor profitability

File: dashboard/vendor_performance_analysis.pbix
💻 How to Run This Project
🪜 Step 1 — Clone the Repository
git clone https://github.com/yourusername/vendor-performance-analysis.git
cd vendor-performance-analysis
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
The dataset consists of three main CSV files located in the /dataset/ folder:
/sale_data/
│
├── sales.csv
├── purchase.csv
└── inventory.csv
## 🧾 1. sales.csv
Column Name	Description	Insight
vendor_id	Unique ID for each vendor	Used to join with vendor and purchase data
invoice_no	Unique sales transaction number	Helps track transaction-level performance
sales_qty	Number of units sold	High values indicate top-performing vendors
sales_price	Selling price per unit	Used to compute total sales and revenue
freight_cost	Cost of shipping goods	High freight cost reduces overall margin
gross_profit	Profit before taxes	Main indicator of profitability
margin_percent	Profit margin percentage	Key performance metric used for comparison

## 📊 Conclusion:

Vendors with high sales_qty have consistent but lower margin_percent.

freight_cost heavily impacts profit — high freight cost reduces margin significantly.

## 🧾 2. purchase.csv
Column Name	Description	Insight
vendor_id	Supplier identifier	Common key for merging datasets
purchase_qty	Quantity of goods purchased	Helps analyze demand vs. supply
purchase_price	Cost price per unit	Used for calculating profit margins
purchase_date	Date of procurement	Used to calculate lead time and inventory flow

## 📊 Conclusion:

Strong correlation (≈0.99) between purchase_qty and sales_qty shows efficient inventory planning.

Vendors with frequent small purchases tend to maintain better inventory turnover.

## 🧾 3. inventory.csv
Column Name	Description	Insight
vendor_id	Vendor identifier	Links to sales & purchase data
opening_stock	Units available at start	Used for turnover and stock analysis
closing_stock	Units available at end	Indicates unsold inventory
unsold_inventory	Calculated as difference between stock & sales	High unsold inventory shows inefficiency

## 📊 Conclusion:

Vendors with low unsold inventory indicate better stock management.

Some low-margin vendors compensate with faster stock turnover.
## 🧩 Combined Data Model

After merging these three files, new features were engineered:

Gross Profit = Sales – Purchase – Freight

Margin% = (Gross Profit / Sales) × 100

Freight-to-Sales Ratio = Freight / Sales

Turnover Rate = Sales Quantity / Average Inventory

Final processed data is stored as:

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
│
├── README.md
│
├── ingestion_db.py                  # Data ingestion into SQLite
├── sale_summary_script.py           # Vendor summary table creation
│
├── sale_data/                       # Raw CSV datasets
│   ├── sales.csv
│   ├── purchase.csv
│   └── inventory.csv
│
├── notebooks/
│   ├── eda_Vendor_sale_summary_analysis.ipynb
│   └── vendor_performance_Analysis.ipynb
│
├── dashboard/
│   └── vendor_performance_analysis.pbix
│
├── reports/
│   └── Vendor_Performance_Analysis_Report.pdf
│
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
🪜 Step 1 — Clone the Repository
git clone https://github.com/yourusername/vendor-performance-analysis.git
cd vendor-performance-analysis

🪜 Step 2 — Run Data Ingestion Script
python ingestion_db.py

🪜 Step 3 — Generate Vendor Summary Table
python sale_summary_script.py

🪜 Step 4 — Perform EDA and Analysis
jupyter notebook notebooks/eda_Vendor_sale_summary_analysis.ipynb
jupyter notebook notebooks/vendor_performance_Analysis.ipynb

🪜 Step 5 — View Dashboard

Open Power BI → Load file
dashboard/vendor_performance_analysis.pbix

## 🧭 Recommendations

Balance high-volume (top) and high-margin (low) vendors.

Reduce freight costs via better contract negotiation.

Automate vendor monitoring using Python alerts.

Use Power BI to track vendor KPIs monthly.

## 👨‍💻 Author

Pawan Kumar Prajapati
Data Analyst | SQL • Python • Power BI

📧 Email: pawankumar231314@gmail.com

🔗 LinkedIn: Pawan Kumar Prajapati