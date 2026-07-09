import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

# Load the dataset (using relative path - works for anyone who clones the project)
df = pd.read_csv('WA_Fn-UseC_-Telco-Customer-Churn.csv')
print("INITIAL DATASET OVERVIEW")
print(f"\nDataset Shape: {df.shape[0]} rows × {df.shape[1]} columns")
print(f"\nColumn Names:\n{df.columns.tolist()}")

# ============================================
# SECTION 1: DATA TYPES AUDIT
# ============================================
print("\n")
print("SECTION 1: DATA TYPES AUDIT")
print("\n--- Current Data Types ---")
dtype_df = pd.DataFrame({
    'Column': df.columns,
    'Data_Type': df.dtypes.values,
    'Non_Null_Count': df.count().values,
    'Null_Count': df.isnull().sum().values
})
print(dtype_df.to_string(index=False))

# ============================================
# SECTION 2: MISSING VALUES AUDIT
# ============================================
print("\n")
print("SECTION 2: MISSING VALUES AUDIT")

# Check for explicit nulls
explicit_nulls = df.isnull().sum()
explicit_nulls = explicit_nulls[explicit_nulls > 0]
if len(explicit_nulls) > 0:
    print("\n--- Explicit Null Values (True NaN) ---")
    for col, count in explicit_nulls.items():
        pct = (count / len(df)) * 100
        print(f"  {col}: {count} ({pct:.2f}%)")
else:
    print("\n[OK] No explicit null values found")

# Check for implicit nulls (empty strings, ' ', 'N/A', etc.)
print("\n--- Implicit Null Values (Empty/Invalid Strings) ---")
implicit_issues = {}
for col in df.columns:
    if df[col].dtype == 'object':
        # Check for empty strings, whitespace-only, common placeholders
        empty_count = df[col].astype(str).str.strip().isin(['', ' ', 'N/A', 'NA', 'null', 'NULL', 'None', 'nan', 'NaN']).sum()
        if empty_count > 0:
            implicit_issues[col] = empty_count

if implicit_issues:
    for col, count in implicit_issues.items():
        pct = (count / len(df)) * 100
        print(f"  {col}: {count} ({pct:.2f}%)")
else:
    print("  [OK] No implicit null values found")

# ============================================
# SECTION 3: DUPLICATES AUDIT
# ============================================
print("\n")
print("SECTION 3: DUPLICATES AUDIT")


# Check for duplicate rows
duplicates_all = df.duplicated().sum()
print(f"\n--- Duplicate Rows ---")
print(f"  Exact duplicate rows: {duplicates_all}")

# Check for duplicate customerID (if exists)
if 'customerID' in df.columns:
    duplicates_id = df['customerID'].duplicated().sum()
    print(f"  Duplicate customerID: {duplicates_id}")

# ============================================
# SECTION 4: CATEGORICAL VALUES AUDIT
# ============================================
print("\n")
print("SECTION 4: CATEGORICAL VALUES AUDIT")


categorical_cols = df.select_dtypes(include=['object']).columns.tolist()
print(f"\nCategorical columns ({len(categorical_cols)}): {categorical_cols}")

for col in categorical_cols:
    unique_vals = df[col].nunique()
    if unique_vals <= 15:
        print(f"\n--- {col} ({unique_vals} unique values) ---")
        value_counts = df[col].value_counts()
        for val, count in value_counts.items():
            pct = (count / len(df)) * 100
            print(f"    {val}: {count} ({pct:.2f}%)")

# ============================================
# SECTION 5: NUMERICAL COLUMNS AUDIT
# ============================================
print("\n")
print("SECTION 5: NUMERICAL COLUMNS AUDIT")


numerical_cols = df.select_dtypes(include=[np.number]).columns.tolist()
print(f"\nNumerical columns ({len(numerical_cols)}): {numerical_cols}")

for col in numerical_cols:
    print(f"\n--- {col} ---")
    print(f"    Min: {df[col].min()}")
    print(f"    Max: {df[col].max()}")
    print(f"    Mean: {df[col].mean():.2f}")
    print(f"    Median: {df[col].median()}")
    print(f"    Std: {df[col].std():.2f}")
    print(f"    Nulls: {df[col].isnull().sum()}")

# ============================================
# SECTION 6: TARGET VARIABLE (CHURN) AUDIT
# ============================================
print("\n")
print("SECTION 6: TARGET VARIABLE (CHURN) AUDIT")


if 'Churn' in df.columns:
    churn_counts = df['Churn'].value_counts()
    print("\n--- Churn Distribution ---")
    for val, count in churn_counts.items():
        pct = (count / len(df)) * 100
        print(f"  {val}: {count} ({pct:.2f}%)")

    # Class imbalance check
    majority_pct = max(churn_counts) / len(df) * 100
    minority_pct = min(churn_counts) / len(df) * 100
    imbalance_ratio = max(churn_counts) / min(churn_counts)
    print(f"\n--- Class Imbalance Analysis ---")
    print(f"  Majority class: {majority_pct:.2f}%")
    print(f"  Minority class: {minority_pct:.2f}%")
    print(f"  Imbalance ratio: {imbalance_ratio:.2f}:1")
    if imbalance_ratio > 3:
        print(f"  [WARNING] Significant class imbalance detected!")
else:
    print("  [ERROR] Churn column not found!")

# ============================================
# SECTION 7: OUTLIER DETECTION
# ============================================
print("\n")
print("SECTION 7: OUTLIER DETECTION (IQR Method)")


for col in numerical_cols:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)][col]
    if len(outliers) > 0:
        print(f"\n--- {col} ---")
        print(f"  Outliers detected: {len(outliers)} ({len(outliers)/len(df)*100:.2f}%)")
        print(f"  Range: [{lower_bound:.2f}, {upper_bound:.2f}]")
        print(f"  Actual range: [{df[col].min()}, {df[col].max()}]")

print("\n")
print("AUDIT COMPLETE - SUMMARY")
