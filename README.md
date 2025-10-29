
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
### 📊 Dataset Overview: Vendor Summary Data

The dataset vendor_summary_data.csv provides detailed insights into vendor-level sales and purchasing performance.
It includes financial metrics, profit margins, turnover rates, and sales-to-purchase ratios — all crucial for analyzing vendor efficiency and profitability.

### 🧾 Basic Information

| **Metric**         | **Value**                    |
| ------------------ | ---------------------------- |
| **File Name**      | `vendor_summary_data.csv`    |
| **Total Rows**     | 10,648                       |
| **Total Columns**  | 18                           |
| **Missing Values** | None                         |
| **File Type**      | CSV (Comma-Separated Values) |

### 🧱 Column Details and Descriptions

| **Column Name**             | **Data Type** | **Description**                                                              |
| --------------------------- | ------------- | ---------------------------------------------------------------------------- |
| **VendorNumber**            | int64         | Unique identifier assigned to each vendor.                                   |
| **VendorName**              | object        | The registered business name of the vendor.                                  |
| **Brand**                   | int64         | Numeric code representing the brand or product line.                         |
| **Description**             | object        | Product name or description supplied by the vendor.                          |
| **Volume**                  | float64       | Quantity or size of product units (e.g., ml, liters, etc.).                  |
| **actual_price**            | float64       | Actual retail selling price per unit.                                        |
| **PurchasePrice**           | float64       | Cost price per unit at which the vendor sells the product.                   |
| **total_quantity_purchase** | int64         | Total quantity purchased from the vendor.                                    |
| **total_dollar_purchase**   | float64       | Total purchase cost in dollars.                                              |
| **total_Quantity_sale**     | float64       | Total quantity of items sold.                                                |
| **total_sale_price**        | float64       | Combined selling price for all sold units.                                   |
| **total_sale_dollar**       | float64       | Total revenue generated from sales.                                          |
| **total_excise_tax**        | float64       | Total tax levied on the sale of the vendor’s products.                       |
| **total_freight_cost**      | float64       | Transportation or logistics cost associated with vendor deliveries.          |
| **gross_profit**            | float64       | Total profit (Revenue - Cost). Indicates vendor profitability.               |
| **margin**                  | float64       | Profit margin ratio (Gross Profit / Sales Revenue).                          |
| **turnOver**                | float64       | Frequency of inventory turnover; higher values indicate faster sales cycles. |
| **sale_to_purchase_ratio**  | float64       | Ratio of sales to purchases, showing vendor performance efficiency.          |

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
│   ├── Dashboard_1.png
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

### Step 1: Clone the repository
git clone https://github.com/yourusername/vendor-performance-analysis.git
cd vendor-performance-analysis

### Step 2: Run ingestion script
python ingestion_db.py

### Step 3: Generate vendor summary table
python sale_summary_script.py

### Step 4: Open Jupyter notebooks for analysis
jupyter notebook notebooks/eda_Vendor_sale_summary_analysis.ipynb
jupyter notebook notebooks/vendor_performance_Analysis.ipynb

### Step 5: View dashboard
 Open Power BI → Load dashboard/vendor_performance_analysis.pbix

## 🧭 Recommendations

Balance high-volume (top) and high-margin (low) vendors.

Reduce freight costs via better contract negotiation.

Clear unsold inventory strategically

Optimize bulk order strategies

Reprice slow-moving, high-margin brands
## 👨‍💻 Author

**Pawan Kumar Prajapati**

Data Analyst | SQL • Python • Power BI

📧 Email: pawankumar231314@gmail.com

🔗 LinkedIn: https://www.linkedin.com/in/pawan-kumar-prajapati-3579b1217/