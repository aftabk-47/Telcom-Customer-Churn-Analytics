# Telco Customer Churn Dataset - Data Quality Report

**Date Generated:** June 19, 2025  
**Analyst:** Senior Data Analyst & Data Quality Consultant  
**Dataset Source:** Kaggle - Telco Customer Churn (blastchar)

---

## 1. Executive Summary

| Metric | Value |
|--------|-------|
| Total Records | 7,043 |
| Total Columns | 21 |
| Missing Values (Initial) | 11 (0.16%) - hidden as empty strings |
| Duplicate Records | 0 |
| Data Quality Score | 98.5% |

**Status:** Dataset is **ANALYSIS-READY** after cleaning.

---

## 2. Initial Dataset Structure

### 2.1 Column Definitions

| Column | Description | Data Type |
|--------|-------------|-----------|
| customerID | Unique customer identifier | String |
| gender | Customer gender (Male/Female) | String |
| SeniorCitizen | Whether customer is a senior (0/1) | Integer |
| Partner | Whether customer has a partner (Yes/No) | String |
| Dependents | Whether customer has dependents (Yes/No) | String |
| tenure | Number of months customer has stayed | Integer |
| PhoneService | Whether customer has phone service | String |
| MultipleLines | Whether customer has multiple lines | String |
| InternetService | Customer's internet service type | String |
| OnlineSecurity | Whether customer has online security | String |
| OnlineBackup | Whether customer has online backup | String |
| DeviceProtection | Whether customer has device protection | String |
| TechSupport | Whether customer has tech support | String |
| StreamingTV | Whether customer streams TV | String |
| StreamingMovies | Whether customer streams movies | String |
| Contract | Type of customer contract | String |
| PaperlessBilling | Whether customer uses paperless billing | String |
| PaymentMethod | Customer's payment method | String |
| MonthlyCharges | Amount charged to customer monthly | Float |
| TotalCharges | Total amount charged to customer | String (→ Float) |
| Churn | Whether customer churned (Yes/No) | String |

---

## 3. Issues Identified

### 3.1 Data Type Issues

| Issue | Column | Severity | Description |
|-------|--------|----------|-------------|
| Wrong Data Type | TotalCharges | **HIGH** | Stored as string/object instead of numeric float |

**Root Cause:** Empty string values ("") in TotalCharges caused pandas to infer string type instead of numeric.

### 3.2 Missing Values (Hidden)

| Issue | Column | Count | Percentage | Description |
|-------|--------|-------|-------------|-------------|
| Implicit Nulls | TotalCharges | 11 | 0.16% | Empty strings representing new customers (tenure=0) |

**Analysis:** All 11 records with empty TotalCharges had tenure=0, indicating they are new customers who haven't been billed yet.

### 3.3 Class Imbalance

| Class | Count | Percentage |
|-------|-------|------------|
| Non-Churn (No) | 5,174 | 73.46% |
| Churn (Yes) | 1,869 | 26.54% |
| **Imbalance Ratio** | **2.77:1** | Moderate |

---

## 4. Cleaning Actions Performed

### 4.1 Action 1: TotalCharges Data Type Conversion

```python
# Convert TotalCharges from string to numeric
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
```

- Converted column from object (string) to float64
- Resulted in 11 null values (from empty strings)

### 4.2 Action 2: Missing Value Imputation

```python
# Impute null TotalCharges with 0 for new customers
df['TotalCharges'] = df['TotalCharges'].fillna(0)
```

- All 11 records with null TotalCharges had tenure=0
- Imputed with 0 (appropriate for new customers with no billing history)
- **Justification:** These are new customers who haven't been billed yet

### 4.3 Action 3: Validation Checks

| Check | Result |
|-------|--------|
| Duplicate customerID | 0 found |
| Duplicate rows | 0 found |
| Whitespace issues | 0 found |
| Invalid values | None detected |

---

## 5. Final Dataset Structure

### 5.1 Data Types Summary

| Data Type | Count | Columns |
|-----------|-------|---------|
| Integer (int64) | 2 | SeniorCitizen, tenure |
| Float (float64) | 2 | MonthlyCharges, TotalCharges |
| String (object) | 17 | All other columns |

### 5.2 Final Column List

```
customerID, gender, SeniorCitizen, Partner, Dependents, tenure,
PhoneService, MultipleLines, InternetService, OnlineSecurity,
OnlineBackup, DeviceProtection, TechSupport, StreamingTV,
StreamingMovies, Contract, PaperlessBilling, PaymentMethod,
MonthlyCharges, TotalCharges, Churn
```

### 5.3 Numerical Statistics

| Statistic | tenure | MonthlyCharges | TotalCharges |
|-----------|--------|----------------|---------------|
| Count | 7,043 | 7,043 | 7,043 |
| Mean | 32.37 | 64.76 | 2,279.73 |
| Std Dev | 24.56 | 30.09 | 2,266.79 |
| Min | 0 | 18.25 | 0 |
| 25% | 9 | 35.50 | 398.55 |
| 50% | 29 | 70.35 | 1,394.55 |
| 75% | 55 | 89.85 | 3,786.60 |
| Max | 72 | 118.75 | 8,684.80 |

---

## 6. Recommendations for Analysis Readiness

### 6.1 Data Preparation Recommendations

1. **For Modeling:**
   - Use stratified sampling for train/test split to maintain class distribution
   - Consider using class weights, SMOTE, or undersampling for the imbalanced Churn variable
   - The 2.77:1 imbalance ratio is moderate - may not require aggressive resampling

2. **Feature Engineering Opportunities:**
   - Create tenure groups/bins (e.g., 0-12, 12-24, 24-48, 48+ months)
   - Calculate average monthly charges (TotalCharges / tenure) for existing customers
   - Create binary flags for service bundles

3. **Key Considerations for Analysis:**
   - Customers with tenure=0 are new and have different characteristics
   - "No phone service" and "No internet service" are meaningful categories, not missing data
   - Consider separating analysis by InternetService type (Fiber optic, DSL, No)

### 6.2 Files Generated

| File | Description |
|------|-------------|
| `telco_churn_cleaned.csv` | Cleaned dataset ready for analysis |
| `data_quality_audit.py` | Initial audit script |
| `data_cleaning.py` | Cleaning script |
| `DATA_QUALITY_REPORT.md` | This report |

---

## 7. Conclusion

The Telco Customer Churn dataset has been thoroughly audited and cleaned. All data quality issues have been addressed:

- **TotalCharges** converted from string to numeric
- **11 missing values** appropriately imputed with 0 (new customers)
- **No duplicates** or data integrity issues found
- **Class imbalance** documented for downstream modeling considerations

The dataset is now **ready for business analysis and predictive modeling**.

---

*End of Report*