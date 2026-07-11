# Telecom Customer Churn Analytics

An end-to-end Data Analytics project focused on identifying customer churn patterns, analyzing business KPIs, segmenting customers, and providing actionable retention strategies using Python, MySQL, and Power BI.

---

## Project Objective

Customer churn directly impacts business revenue and profitability. This project analyzes telecom customer behavior to identify the key drivers of churn and provide data-driven recommendations to improve customer retention.

---

## Tech Stack

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- MySQL
- Power BI
- Jupyter Notebook

---

## Project Workflow

```text
Raw Dataset
      ↓
Data Quality Audit
      ↓
Data Cleaning
      ↓
Exploratory Data Analysis (EDA)
      ↓
KPI Analysis
      ↓
Customer Segmentation
      ↓
SQL Business Analysis
      ↓
Interactive Power BI Dashboard
```

---

## Project Structure

```text
Customer_Churn_Analysis/
│
├── data/
├── notebooks/
├── reports/
├── sql/
├── dashboard/
├── charts/
├── README.md
└── requirements.txt
```

---

## Dashboard Highlights

The Power BI dashboard includes:

- Customer Overview
- Churn Rate Analysis
- Revenue at Risk
- Contract-wise Churn Analysis
- Internet Service Analysis
- Payment Method Analysis
- Customer Segmentation
- Interactive Filters

---

## Key Business Insights

- Overall customer churn rate is **26.54%**.
- Month-to-Month contracts exhibit the highest churn rate.
- Fiber Optic customers churn significantly more than DSL customers.
- Electronic Check users have the highest churn rate among payment methods.
- Customers with lower tenure are more likely to churn.
- High-value customers at risk were identified for targeted retention campaigns.

---

## Business Recommendations

- Encourage customers to migrate to long-term contracts.
- Introduce retention offers for new customers.
- Improve Fiber Optic customer experience.
- Promote AutoPay and digital payment methods.
- Prioritize proactive support for high-value customers.

---

## Dashboard Preview

![Telecom Customer Churn Dashboard](Dashboard/Telcom_Customer_Churn_Dashboard.png)

---

## Dataset

**IBM Telco Customer Churn Dataset**

Source: https://www.kaggle.com/datasets/blastchar/telco-customer-churn

---

## How to Run This Project Locally

### 1. Clone the Repository

```bash
git clone https://github.com/aftabk-47/Customer_Churn_Analysis.git
```

### 2. Navigate to the Project Directory

```bash
cd Customer_Churn_Analysis
```

### 3. Create a Virtual Environment (Optional)

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Required Libraries

```bash
pip install -r requirements.txt
```

### 5. Run the Python Scripts

Example:

```bash
python notebooks/data_cleaning.py
python notebooks/exploratory_data_analysis.py
python notebooks/kpi_analysis.py
python notebooks/customer_segmentation.py
```

### 6. Execute SQL Analysis

- Open MySQL Workbench.
- Import `telco_churn_cleaned.csv` into a database.
- Open and execute:

```text
sql/05_sql_business_analysis.sql
```

### 7. Open the Power BI Dashboard

Open:

```text
dashboard/customer_churn_dashboard.pbix
```

Refresh the data source if prompted.

---

## Future Improvements

- Build a predictive churn model using Machine Learning.
- Deploy the dashboard using Power BI Service.
- Integrate automated data refresh.
- Expand the project using larger customer datasets.

---

## Author

**Aftab**

GitHub: https://github.com/aftabk-47

LinkedIn: *(Add your LinkedIn profile)*
