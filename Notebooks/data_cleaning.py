"""
================================================================================
DATA CLEANING SCRIPT - Telco Customer Churn Dataset
================================================================================
"""
import pandas as pd
import numpy as np
import os

# ============================================
# LOAD DATA
# ============================================
# Use relative path - works for anyone who clones the project
input_path = 'WA_Fn-UseC_-Telco-Customer-Churn.csv'
output_path = 'telco_churn_cleaned.csv'

df = pd.read_csv(input_path)
print("DATA CLEANING REPORT - Telco Customer Churn Dataset")

print(f"\n[INITIAL] Dataset: {df.shape[0]} rows x {df.shape[1]} columns")

# ============================================
# ISSUE 1: TotalCharges - Incorrect Data Type
# ============================================

print("ISSUE 1: TotalCharges Incorrect Data Type")
print("-" * 80)
print("  Problem: TotalCharges stored as string instead of numeric")
print("  Impact: Cannot perform numerical analysis on this column")

# Convert TotalCharges to numeric (coerce errors to NaN)
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

# Check how many failed conversion
null_totalcharges = df['TotalCharges'].isnull().sum()
print(f"  Action: Converted TotalCharges to float64")
print(f"  Result: {null_totalcharges} null values created from empty strings")

# ============================================
# ISSUE 2: TotalCharges - Missing Values for New Customers
# ============================================

print("ISSUE 2: TotalCharges Missing Values (New Customers)")
print("-" * 80)
print(f"  Problem: {null_totalcharges} records have empty TotalCharges")
print(f"  Analysis: All records with null TotalCharges have tenure = 0")

# Verify this is true
new_customers = df[df['tenure'] == 0]
print(f"  Verification: Records with tenure=0: {len(new_customers)}")
print(f"  Records with both tenure=0 and null TotalCharges: {new_customers['TotalCharges'].isnull().sum()}")

# Impute with 0 for new customers (they haven't been billed yet)
df['TotalCharges'] = df['TotalCharges'].fillna(0)
print(f"  Action: Imputed null TotalCharges with 0")
print(f"  Result: TotalCharges now has {df['TotalCharges'].isnull().sum()} null values")

# ============================================
# ISSUE 3: Data Type Standardization
# ============================================

print("ISSUE 3: Data Type Standardization")
print("-" * 80)

# SeniorCitizen should be converted to categorical (binary 0/1)
print(f"  Action: SeniorCitizen already correctly typed as int64 (binary)")

# Verify data types are now correct
print(f"  Result: Final data types:")
print(f"    - Numerical: SeniorCitizen (int64), tenure (int64), MonthlyCharges (float64), TotalCharges (float64)")
print(f"    - Categorical: All other columns (object/string)")

# ============================================
# ISSUE 4: Categorical Value Standardization
# ============================================

print("ISSUE 4: Categorical Value Standardization")
print("-" * 80)

# Standardize 'No phone service' / 'No internet service' values
# We'll standardize "No phone service" and "No internet service" to "No" for consistency

services_with_no_service = ['MultipleLines', 'OnlineSecurity', 'OnlineBackup',
                            'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies']

for col in services_with_no_service:
    unique_vals = df[col].unique()
    if 'No phone service' in unique_vals or 'No internet service' in unique_vals:
        print(f"  Column '{col}': Contains service absence indicators")
        print(f"    Original values: {list(unique_vals)}")

# We'll keep these as-is since they carry meaningful information
# But we note this for analysis
print(f"  Action: Retained original values (they carry semantic meaning)")
print(f"  Note: 'No phone service' and 'No internet service' indicate customer doesn't have that service")

# ============================================
# ISSUE 5: Class Imbalance in Target Variable
# ============================================

print("ISSUE 5: Class Imbalance in Target Variable (Churn)")
print("-" * 80)

churn_counts = df['Churn'].value_counts()
print(f"  Problem: Imbalanced classes")
print(f"    - Non-Churn: {churn_counts.get('No', 0)} ({churn_counts.get('No', 0)/len(df)*100:.2f}%)")
print(f"    - Churn: {churn_counts.get('Yes', 0)} ({churn_counts.get('Yes', 0)/len(df)*100:.2f}%)")
print(f"    - Imbalance ratio: {churn_counts.get('No', 0)/churn_counts.get('Yes', 0):.2f}:1")

print(f"  Recommendation: Use stratified sampling for train/test split")
print(f"  Note: For modeling, consider SMOTE, class weights, or undersampling")

# ============================================
# ISSUE 6: CustomerID Format Check
# ============================================

print("ISSUE 6: CustomerID Validation")
print("-" * 80)

print(f"  Total unique customerIDs: {df['customerID'].nunique()}")
print(f"  Total records: {len(df)}")
if df['customerID'].nunique() == len(df):
    print(f"  Result: [OK] All customerIDs are unique")
else:
    print(f"  Result: [WARNING] Duplicate customerIDs found!")

# ============================================
# ISSUE 7: Inconsistent Formatting
# ============================================

print("ISSUE 7: Formatting Consistency Check")
print("-" * 80)

# Check for leading/trailing whitespace in string columns
whitespace_issues = []
for col in df.select_dtypes(include=['object']).columns:
    if df[col].dtype == 'object':
        has_ws = df[col].astype(str).str.strip() != df[col].astype(str)
        if has_ws.any():
            whitespace_issues.append(col)

if whitespace_issues:
    print(f"  Problem: Found whitespace issues in: {whitespace_issues}")
    # Strip whitespace
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].astype(str).str.strip()
    print(f"  Action: Stripped leading/trailing whitespace from all string columns")
else:
    print(f"  Result: [OK] No whitespace issues found")

# ============================================
# FINAL DATASET SUMMARY
# ============================================
print("\n")
print("FINAL CLEANED DATASET SUMMARY")


print(f"\nDataset Shape: {df.shape[0]} rows x {df.shape[1]} columns")

print("\n--- Column Data Types ---")
for col in df.columns:
    print(f"  {col}: {df[col].dtype}")

print("\n--- Missing Values Summary ---")
missing = df.isnull().sum()
missing = missing[missing > 0]
if len(missing) > 0:
    for col, count in missing.items():
        print(f"  {col}: {count} ({count/len(df)*100:.2f}%)")
else:
    print("  [OK] No missing values")

print("\n--- Numerical Statistics ---")
numerical_cols = ['tenure', 'MonthlyCharges', 'TotalCharges']
print(df[numerical_cols].describe().to_string())

print("\n--- Churn Distribution (Final) ---")
churn_final = df['Churn'].value_counts()
for val, count in churn_final.items():
    print(f"  {val}: {count} ({count/len(df)*100:.2f}%)")

# ============================================
# SAVE CLEANED DATASET
# ============================================
df.to_csv(output_path, index=False)
print(f"\n[OUTPUT] Cleaned dataset saved to: {output_path}")

print("\n")
print("DATA CLEANING COMPLETE")
