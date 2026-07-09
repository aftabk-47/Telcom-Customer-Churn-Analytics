"""
================================================================================
CUSTOMER SEGMENTATION ANALYSIS - Telco Customer Churn
================================================================================
This script performs rule-based customer segmentation for business analysis.
No machine learning or clustering algorithms are used.
"""

import pandas as pd
import numpy as np

# ============================================
# LOAD DATA
# ============================================
df = pd.read_csv('telco_churn_cleaned.csv')
df['Churn_Binary'] = (df['Churn'] == 'Yes').astype(int)
df['CLV'] = df['MonthlyCharges'] * df['tenure']

# Count additional services for Segment 3
services = ['PhoneService', 'MultipleLines', 'OnlineSecurity', 'OnlineBackup',
            'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies']

df['num_services'] = 0
for service in services:
    df['num_services'] += (df[service] == 'Yes').astype(int)

print("=" * 70)
print("CUSTOMER SEGMENTATION ANALYSIS")
print("=" * 70)

# ============================================
# SEGMENT 1: HIGH-VALUE LOYAL CUSTOMERS
# ============================================
# Criteria: tenure >= 24 months, monthly charges >= 70, did NOT churn

segment1 = df[(df['tenure'] >= 24) &
             (df['MonthlyCharges'] >= 70) &
             (df['Churn'] == 'No')]

print("\n" + "=" * 70)
print("SEGMENT 1: HIGH-VALUE LOYAL CUSTOMERS")
print("=" * 70)
print(f"\nNumber of customers: {len(segment1)}")
print(f"Average tenure: {segment1['tenure'].mean():.1f} months")
print(f"Average monthly charges: ${segment1['MonthlyCharges'].mean():.2f}")
print(f"Estimated monthly revenue: ${segment1['MonthlyCharges'].sum():,.2f}")
print(f"Estimated annual revenue: ${segment1['MonthlyCharges'].sum() * 12:,.2f}")

print("\nContract Distribution:")
print(segment1['Contract'].value_counts().to_string())

print("\nInternet Service Distribution:")
print(segment1['InternetService'].value_counts().to_string())

# ============================================
# SEGMENT 2: HIGH-VALUE AT-RISK CUSTOMERS
# ============================================
# Criteria: (churned OR month-to-month) AND high monthly charges >= 70

segment2 = df[((df['Churn'] == 'Yes') | (df['Contract'] == 'Month-to-month')) &
              (df['MonthlyCharges'] >= 70)]

print("\n" + "=" * 70)
print("SEGMENT 2: HIGH-VALUE AT-RISK CUSTOMERS")
print("=" * 70)
print(f"\nNumber of customers: {len(segment2)}")
print(f"Average tenure: {segment2['tenure'].mean():.1f} months")
print(f"Average monthly charges: ${segment2['MonthlyCharges'].mean():.2f}")
print(f"Revenue at risk: ${segment2['MonthlyCharges'].sum():,.2f}")

churned_in_segment2 = segment2[segment2['Churn'] == 'Yes']
print(f"\nActual churners in this segment: {len(churned_in_segment2)} ({len(churned_in_segment2)/len(segment2)*100:.1f}%)")

print("\nContract Distribution:")
print(segment2['Contract'].value_counts().to_string())

print("\nPayment Method Distribution:")
print(segment2['PaymentMethod'].value_counts().to_string())

print("\nInternet Service Distribution:")
print(segment2['InternetService'].value_counts().to_string())

# ============================================
# SEGMENT 3: LOW ENGAGEMENT CUSTOMERS
# ============================================
# Criteria: tenure < 12 months, monthly charges < 70, limited services

segment3 = df[(df['tenure'] < 12) &
              (df['MonthlyCharges'] < 70) &
              (df['num_services'] <= 2)]

print("\n" + "=" * 70)
print("SEGMENT 3: LOW ENGAGEMENT CUSTOMERS")
print("=" * 70)
print(f"\nNumber of customers: {len(segment3)}")
print(f"Average tenure: {segment3['tenure'].mean():.1f} months")
print(f"Average monthly charges: ${segment3['MonthlyCharges'].mean():.2f}")
print(f"Churn count: {segment3['Churn_Binary'].sum()}")
print(f"Churn rate: {segment3['Churn_Binary'].mean()*100:.1f}%")

print("\nContract Distribution:")
print(segment3['Contract'].value_counts().to_string())

print("\nPayment Method Distribution:")
print(segment3['PaymentMethod'].value_counts().to_string())

print("\n" + "=" * 70)
print("SEGMENTATION ANALYSIS COMPLETE")
print("=" * 70)