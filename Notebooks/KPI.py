"""
================================================================================
KPI CALCULATION SCRIPT - Telco Customer Churn Analysis
================================================================================
This script calculates key performance indicators and answers business questions
using the cleaned telco customer churn dataset.
"""

import pandas as pd
import numpy as np

# ============================================
# LOAD DATA
# ============================================
df = pd.read_csv('telco_churn_cleaned.csv')
df['Churn_Binary'] = (df['Churn'] == 'Yes').astype(int)

# Create tenure groups for analysis
df['tenure_group'] = pd.cut(df['tenure'],
                           bins=[0, 12, 24, 36, 48, 72],
                           labels=['0-12', '13-24', '25-36', '37-48', '49-72'])

# Calculate CLV (approximate)
df['CLV'] = df['MonthlyCharges'] * df['tenure']

print("=" * 70)
print("KPI CALCULATIONS")
print("=" * 70)

# ============================================
# STEP 1: CALCULATE KPIs
# ============================================

# 1. Total Customers
total_customers = len(df)
print(f"\n1. Total Customers: {total_customers}")

# 2. Churn Rate (%)
churn_rate = (df['Churn_Binary'].sum() / total_customers) * 100
print(f"2. Churn Rate: {churn_rate:.2f}%")

# 3. Revenue at Risk (Total Monthly Charges of customers who churned)
churned_df = df[df['Churn'] == 'Yes']
revenue_at_risk = churned_df['MonthlyCharges'].sum()
print(f"3. Revenue at Risk: ${revenue_at_risk:,.2f}")

# 4. Average Customer Lifetime Value (Monthly Charges × Tenure)
avg_clv = df['CLV'].mean()
print(f"4. Average CLV: ${avg_clv:,.2f}")

# 5. Average Customer Tenure (Months)
avg_tenure = df['tenure'].mean()
print(f"5. Average Tenure: {avg_tenure:.2f} months")

# ============================================
# STEP 2: BUSINESS QUESTIONS
# ============================================

print("\n" + "=" * 70)
print("BUSINESS QUESTION 1: Which customer groups generate the highest revenue?")
print("=" * 70)

# Revenue by Contract Type
print("\n--- Revenue by Contract Type ---")
contract_revenue = df.groupby('Contract')['MonthlyCharges'].sum().sort_values(ascending=False)
for contract, revenue in contract_revenue.items():
    print(f"  {contract}: ${revenue:,.2f}")

# Revenue by Internet Service
print("\n--- Revenue by Internet Service ---")
internet_revenue = df.groupby('InternetService')['MonthlyCharges'].sum().sort_values(ascending=False)
for service, revenue in internet_revenue.items():
    print(f"  {service}: ${revenue:,.2f}")

# Revenue by Payment Method
print("\n--- Revenue by Payment Method ---")
payment_revenue = df.groupby('PaymentMethod')['MonthlyCharges'].sum().sort_values(ascending=False)
for method, revenue in payment_revenue.items():
    print(f"  {method}: ${revenue:,.2f}")

# Revenue by Tenure Group
print("\n--- Revenue by Tenure Group ---")
tenure_revenue = df.groupby('tenure_group', observed=True)['MonthlyCharges'].sum()
for group, revenue in tenure_revenue.items():
    print(f"  {group}: ${revenue:,.2f}")

print("\n" + "=" * 70)
print("BUSINESS QUESTION 2: Which customer groups have the highest churn rate?")
print("=" * 70)

# Churn by Contract Type
print("\n--- Churn Rate by Contract Type ---")
contract_churn = df.groupby('Contract')['Churn_Binary'].mean() * 100
for contract, rate in contract_churn.sort_values(ascending=False).items():
    print(f"  {contract}: {rate:.2f}%")

# Churn by Internet Service
print("\n--- Churn Rate by Internet Service ---")
internet_churn = df.groupby('InternetService')['Churn_Binary'].mean() * 100
for service, rate in internet_churn.sort_values(ascending=False).items():
    print(f"  {service}: {rate:.2f}%")

# Churn by Payment Method
print("\n--- Churn Rate by Payment Method ---")
payment_churn = df.groupby('PaymentMethod')['Churn_Binary'].mean() * 100
for method, rate in payment_churn.sort_values(ascending=False).items():
    print(f"  {method}: {rate:.2f}%")

# Churn by Tenure Group
print("\n--- Churn Rate by Tenure Group ---")
tenure_churn = df.groupby('tenure_group', observed=True)['Churn_Binary'].mean() * 100
for group, rate in tenure_churn.items():
    print(f"  {group}: {rate:.2f}%")

# Churn by Additional Services
print("\n--- Churn Rate by Additional Services ---")
services = ['OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies']
for service in services:
    without = df[df[service] == 'No']['Churn_Binary'].mean() * 100
    with_svc = df[df[service] == 'Yes']['Churn_Binary'].mean() * 100
    print(f"  {service}: Without={without:.1f}%, With={with_svc:.1f}%")

print("\n" + "=" * 70)
print("BUSINESS QUESTION 3: Which customer groups should be prioritized for retention?")
print("=" * 70)

# High-Risk High-Value Segments
print("\n--- High-Risk High-Value Segments ---")

# Month-to-month with Fiber Optic
mtm_fiber = df[(df['Contract'] == 'Month-to-month') & (df['InternetService'] == 'Fiber optic')]
churn_rate_mtm_fiber = mtm_fiber['Churn_Binary'].mean() * 100
revenue_mtm_fiber = mtm_fiber['MonthlyCharges'].sum()
print(f"  Month-to-month + Fiber optic: {churn_rate_mtm_fiber:.1f}% churn, ${revenue_mtm_fiber:,.0f} revenue")

# Electronic check with Fiber optic
ec_fiber = df[(df['PaymentMethod'] == 'Electronic check') & (df['InternetService'] == 'Fiber optic')]
churn_rate_ec_fiber = ec_fiber['Churn_Binary'].mean() * 100
revenue_ec_fiber = ec_fiber['MonthlyCharges'].sum()
print(f"  Electronic check + Fiber optic: {churn_rate_ec_fiber:.1f}% churn, ${revenue_ec_fiber:,.0f} revenue")

# New customers (0-12 months tenure)
new_customers = df[df['tenure'] <= 12]
churn_rate_new = new_customers['Churn_Binary'].mean() * 100
revenue_new = new_customers['MonthlyCharges'].sum()
print(f"  New customers (0-12 months): {churn_rate_new:.1f}% churn, ${revenue_new:,.0f} revenue")

print("\n" + "=" * 70)
print("BUSINESS QUESTION 4: Business Impact of Customer Churn")
print("=" * 70)

retained_df = df[df['Churn'] == 'No']

print(f"\n--- Revenue Impact ---")
print(f"  Revenue at Risk (monthly): ${churned_df['MonthlyCharges'].sum():,.2f}")
print(f"  Average monthly revenue lost per churned customer: ${churned_df['MonthlyCharges'].mean():.2f}")

print(f"\n--- Customer Lifetime Value Impact ---")
print(f"  Average CLV of churned customers: ${churned_df['CLV'].mean():,.2f}")
print(f"  Average CLV of retained customers: ${retained_df['CLV'].mean():,.2f}")
print(f"  CLV difference: ${retained_df['CLV'].mean() - churned_df['CLV'].mean():,.2f}")

print(f"\n--- Tenure Impact ---")
print(f"  Average tenure of churned customers: {churned_df['tenure'].mean():.1f} months")
print(f"  Average tenure of retained customers: {retained_df['tenure'].mean():.1f} months")

print("\n" + "=" * 70)
print("KPI CALCULATION COMPLETE")
print("=" * 70)