"""
Telco Customer Churn - Comprehensive Exploratory Data Analysis (v2)
=====================================================================
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import warnings
import os
warnings.filterwarnings('ignore')

# Set style for visualizations
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 11

# Create charts directory
charts_dir = 'charts'
os.makedirs(charts_dir, exist_ok=True)

# Load the cleaned dataset
df = pd.read_csv('telco_churn_cleaned.csv')

# Convert Churn to binary for calculations
df['Churn_Binary'] = (df['Churn'] == 'Yes').astype(int)


print("TELCO CUSTOMER CHURN - EXPLORATORY DATA ANALYSIS")

print(f"\nDataset Shape: {df.shape[0]} customers, {df.shape[1]} features")

# ============================================================================
# SECTION 1: CHURN DISTRIBUTION
# ============================================================================
print("\n" + "="*70)
print("1. CHURN DISTRIBUTION ANALYSIS")


churn_counts = df['Churn'].value_counts()
churn_pct = df['Churn'].value_counts(normalize=True) * 100

print(f"\n{'Churn Status':<15} {'Count':<12} {'Percentage':<12}")
print("-"*40)
for status in churn_counts.index:
    print(f"{status:<15} {churn_counts[status]:<12} {churn_pct[status]:.2f}%")

churn_rate = churn_pct['Yes']
print(f"\n>> Overall Churn Rate: {churn_rate:.2f}%")

# Create churn distribution visualization
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Pie chart
colors = ['#2ecc71', '#e74c3c']
axes[0].pie(churn_counts, labels=churn_counts.index, autopct='%1.1f%%',
            colors=colors, explode=[0, 0.05], startangle=90)
axes[0].set_title('Churn Distribution', fontsize=14, fontweight='bold')

# Bar chart
bars = axes[1].bar(churn_counts.index, churn_counts.values, color=colors, edgecolor='black')
axes[1].set_xlabel('Churn Status', fontsize=12)
axes[1].set_ylabel('Number of Customers', fontsize=12)
axes[1].set_title('Churn Count Distribution', fontsize=14, fontweight='bold')

for bar, count in zip(bars, churn_counts.values):
    axes[1].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 50,
                 f'{count}', ha='center', va='bottom', fontweight='bold')

plt.tight_layout()
plt.savefig(f'{charts_dir}/01_churn_distribution.png', dpi=150, bbox_inches='tight')
plt.close()

# ============================================================================
# SECTION 2: DEMOGRAPHICS VS CHURN
# ============================================================================
print("\n" + "="*70)
print("2. DEMOGRAPHICS VS CHURN ANALYSIS")


# 2a. Gender vs Churn
print("\n--- 2a. Gender vs Churn ---")
gender_churn_pct = pd.crosstab(df['gender'], df['Churn'], normalize='index') * 100
print(f"Female: {gender_churn_pct.loc['Female', 'Yes']:.2f}%")
print(f"Male: {gender_churn_pct.loc['Male', 'Yes']:.2f}%")

# 2b. Senior Citizen vs Churn
print("\n--- 2b. Senior Citizen vs Churn ---")
df['SeniorCitizen_Label'] = df['SeniorCitizen'].map({0: 'No', 1: 'Yes'})
senior_churn_pct = pd.crosstab(df['SeniorCitizen_Label'], df['Churn'], normalize='index') * 100
print(f"No: {senior_churn_pct.loc['No', 'Yes']:.2f}%")
print(f"Yes: {senior_churn_pct.loc['Yes', 'Yes']:.2f}%")

# 2c. Partner vs Churn
print("\n--- 2c. Partner vs Churn ---")
partner_churn_pct = pd.crosstab(df['Partner'], df['Churn'], normalize='index') * 100
print(f"No: {partner_churn_pct.loc['No', 'Yes']:.2f}%")
print(f"Yes: {partner_churn_pct.loc['Yes', 'Yes']:.2f}%")

# 2d. Dependents vs Churn
print("\n--- 2d. Dependents vs Churn ---")
dependents_churn_pct = pd.crosstab(df['Dependents'], df['Churn'], normalize='index') * 100
print(f"No: {dependents_churn_pct.loc['No', 'Yes']:.2f}%")
print(f"Yes: {dependents_churn_pct.loc['Yes', 'Yes']:.2f}%")

# Create demographics visualization
fig, axes = plt.subplots(2, 2, figsize=(16, 12))

gender_data = df.groupby('gender')['Churn_Binary'].mean() * 100
axes[0, 0].bar(gender_data.index, gender_data.values, color=['#3498db', '#e91e63'], edgecolor='black')
axes[0, 0].axhline(y=churn_rate, color='red', linestyle='--', label=f'Overall ({churn_rate:.1f}%)')
axes[0, 0].set_title('Churn Rate by Gender', fontsize=14, fontweight='bold')
axes[0, 0].set_ylabel('Churn Rate (%)')

senior_data = df.groupby('SeniorCitizen_Label')['Churn_Binary'].mean() * 100
axes[0, 1].bar(senior_data.index, senior_data.values, color=['#9b59b6', '#f39c12'], edgecolor='black')
axes[0, 1].axhline(y=churn_rate, color='red', linestyle='--', label=f'Overall ({churn_rate:.1f}%)')
axes[0, 1].set_title('Churn Rate by Senior Status', fontsize=14, fontweight='bold')
axes[0, 1].set_ylabel('Churn Rate (%)')

partner_data = df.groupby('Partner')['Churn_Binary'].mean() * 100
axes[1, 0].bar(partner_data.index, partner_data.values, color=['#1abc9c', '#e74c3c'], edgecolor='black')
axes[1, 0].axhline(y=churn_rate, color='red', linestyle='--', label=f'Overall ({churn_rate:.1f}%)')
axes[1, 0].set_title('Churn Rate by Partner Status', fontsize=14, fontweight='bold')
axes[1, 0].set_ylabel('Churn Rate (%)')

dependents_data = df.groupby('Dependents')['Churn_Binary'].mean() * 100
axes[1, 1].bar(dependents_data.index, dependents_data.values, color=['#2ecc71', '#3498db'], edgecolor='black')
axes[1, 1].axhline(y=churn_rate, color='red', linestyle='--', label=f'Overall ({churn_rate:.1f}%)')
axes[1, 1].set_title('Churn Rate by Dependents Status', fontsize=14, fontweight='bold')
axes[1, 1].set_ylabel('Churn Rate (%)')

plt.tight_layout()
plt.savefig(f'{charts_dir}/02_demographics_vs_churn.png', dpi=150, bbox_inches='tight')
plt.close()

# ============================================================================
# SECTION 3: TENURE VS CHURN
# ============================================================================
print("\n" + "="*70)
print("3. TENURE VS CHURN ANALYSIS")


tenure_by_churn = df.groupby('Churn')['tenure'].describe()
print("\nTenure Statistics by Churn:")
print(tenure_by_churn[['mean', 'std', 'min', 'max']])

df['tenure_group'] = pd.cut(df['tenure'], bins=[0, 12, 24, 36, 48, 72],
                           labels=['0-12', '13-24', '25-36', '37-48', '49-72'])
tenure_group_churn = df.groupby('tenure_group', observed=True)['Churn_Binary'].mean() * 100

print("\nChurn Rate by Tenure Group:")
for group, rate in tenure_group_churn.items():
    print(f"  {group}: {rate:.2f}%")

fig, axes = plt.subplots(1, 2, figsize=(16, 6))

df.boxplot(column='tenure', by='Churn', ax=axes[0])
axes[0].set_title('Tenure by Churn Status', fontsize=14, fontweight='bold')
axes[0].set_ylabel('Tenure (months)')
plt.suptitle('')

colors = plt.cm.RdYlGn_r(np.linspace(0.2, 0.8, len(tenure_group_churn)))
axes[1].bar(tenure_group_churn.index, tenure_group_churn.values, color=colors, edgecolor='black')
axes[1].axhline(y=churn_rate, color='red', linestyle='--', label=f'Overall ({churn_rate:.1f}%)')
axes[1].set_title('Churn Rate by Tenure Group', fontsize=14, fontweight='bold')
axes[1].set_xlabel('Tenure Group (months)')
axes[1].set_ylabel('Churn Rate (%)')

plt.tight_layout()
plt.savefig(f'{charts_dir}/03_tenure_vs_churn.png', dpi=150, bbox_inches='tight')
plt.close()

# ============================================================================
# SECTION 4: MONTHLY CHARGES VS CHURN
# ============================================================================
print("\n" + "="*70)
print("4. MONTHLY CHARGES VS CHURN ANALYSIS")


monthly_by_churn = df.groupby('Churn')['MonthlyCharges'].describe()
print("\nMonthly Charges by Churn:")
print(monthly_by_churn[['mean', 'std', 'min', 'max']])

churned_monthly = df[df['Churn'] == 'Yes']['MonthlyCharges']
retained_monthly = df[df['Churn'] == 'No']['MonthlyCharges']
print(f"\nAvg Monthly Charges - Churned: ${churned_monthly.mean():.2f}")
print(f"Avg Monthly Charges - Retained: ${retained_monthly.mean():.2f}")

fig, axes = plt.subplots(1, 2, figsize=(16, 6))

df.boxplot(column='MonthlyCharges', by='Churn', ax=axes[0])
axes[0].set_title('Monthly Charges by Churn', fontsize=14, fontweight='bold')
axes[0].set_ylabel('Monthly Charges ($)')
plt.suptitle('')

axes[1].hist(retained_monthly, bins=30, alpha=0.7, label='Retained', color='#2ecc71')
axes[1].hist(churned_monthly, bins=30, alpha=0.7, label='Churned', color='#e74c3c')
axes[1].set_title('Monthly Charges Distribution', fontsize=14, fontweight='bold')
axes[1].set_xlabel('Monthly Charges ($)')
axes[1].set_ylabel('Frequency')
axes[1].legend()

plt.tight_layout()
plt.savefig(f'{charts_dir}/04_monthly_charges_vs_churn.png', dpi=150, bbox_inches='tight')
plt.close()

# ============================================================================
# SECTION 5: TOTAL CHARGES VS CHURN
# ============================================================================
print("\n" + "="*70)
print("5. TOTAL CHARGES VS CHURN ANALYSIS")


total_by_churn = df.groupby('Churn')['TotalCharges'].describe()
print("\nTotal Charges by Churn:")
print(total_by_churn[['mean', 'std', 'min', 'max']])

churned_total = df[df['Churn'] == 'Yes']['TotalCharges']
retained_total = df[df['Churn'] == 'No']['TotalCharges']
print(f"\nAvg Total Charges - Churned: ${churned_total.mean():.2f}")
print(f"Avg Total Charges - Retained: ${retained_total.mean():.2f}")

fig, axes = plt.subplots(1, 2, figsize=(16, 6))

df.boxplot(column='TotalCharges', by='Churn', ax=axes[0])
axes[0].set_title('Total Charges by Churn', fontsize=14, fontweight='bold')
axes[0].set_ylabel('Total Charges ($)')
plt.suptitle('')

axes[1].hist(retained_total, bins=30, alpha=0.7, label='Retained', color='#2ecc71')
axes[1].hist(churned_total, bins=30, alpha=0.7, label='Churned', color='#e74c3c')
axes[1].set_title('Total Charges Distribution', fontsize=14, fontweight='bold')
axes[1].set_xlabel('Total Charges ($)')
axes[1].set_ylabel('Frequency')
axes[1].legend()

plt.tight_layout()
plt.savefig(f'{charts_dir}/05_total_charges_vs_churn.png', dpi=150, bbox_inches='tight')
plt.close()

# ============================================================================
# SECTION 6: CONTRACT TYPE VS CHURN
# ============================================================================
print("\n" + "="*70)
print("6. CONTRACT TYPE VS CHURN ANALYSIS")


contract_churn_pct = pd.crosstab(df['Contract'], df['Churn'], normalize='index') * 100
print("\nChurn Rate by Contract Type:")
for contract in contract_churn_pct.index:
    print(f"  {contract}: {contract_churn_pct.loc[contract, 'Yes']:.2f}%")

fig, ax = plt.subplots(figsize=(12, 6))
contract_data = df.groupby('Contract')['Churn_Binary'].mean() * 100
contract_data = contract_data.sort_values()
colors = ['#2ecc71', '#f1c40f', '#e74c3c']
ax.bar(contract_data.index, contract_data.values, color=colors, edgecolor='black')
ax.axhline(y=churn_rate, color='red', linestyle='--', label=f'Overall ({churn_rate:.1f}%)')
ax.set_title('Churn Rate by Contract Type', fontsize=14, fontweight='bold')
ax.set_xlabel('Contract Type')
ax.set_ylabel('Churn Rate (%)')
for i, (idx, val) in enumerate(contract_data.items()):
    ax.text(i, val + 1, f'{val:.1f}%', ha='center', fontweight='bold')

plt.tight_layout()
plt.savefig(f'{charts_dir}/06_contract_vs_churn.png', dpi=150, bbox_inches='tight')
plt.close()

# ============================================================================
# SECTION 7: PAYMENT METHOD VS CHURN
# ============================================================================
print("\n" + "="*70)
print("7. PAYMENT METHOD VS CHURN ANALYSIS")


payment_churn_pct = pd.crosstab(df['PaymentMethod'], df['Churn'], normalize='index') * 100
print("\nChurn Rate by Payment Method:")
for payment in payment_churn_pct.index:
    print(f"  {payment}: {payment_churn_pct.loc[payment, 'Yes']:.2f}%")

fig, ax = plt.subplots(figsize=(14, 6))
payment_data = df.groupby('PaymentMethod')['Churn_Binary'].mean() * 100
payment_data = payment_data.sort_values()
colors = plt.cm.RdYlGn_r(np.linspace(0.2, 0.8, len(payment_data)))
ax.bar(payment_data.index, payment_data.values, color=colors, edgecolor='black')
ax.axhline(y=churn_rate, color='red', linestyle='--', label=f'Overall ({churn_rate:.1f}%)')
ax.set_title('Churn Rate by Payment Method', fontsize=14, fontweight='bold')
ax.set_ylabel('Churn Rate (%)')
ax.set_xticklabels(ax.get_xticklabels(), rotation=15, ha='right')
plt.tight_layout()
plt.savefig(f'{charts_dir}/07_payment_method_vs_churn.png', dpi=150, bbox_inches='tight')
plt.close()

# ============================================================================
# SECTION 8: INTERNET SERVICE VS CHURN
# ============================================================================
print("\n" + "="*70)
print("8. INTERNET SERVICE VS CHURN ANALYSIS")


internet_churn_pct = pd.crosstab(df['InternetService'], df['Churn'], normalize='index') * 100
print("\nChurn Rate by Internet Service:")
for service in internet_churn_pct.index:
    print(f"  {service}: {internet_churn_pct.loc[service, 'Yes']:.2f}%")

fig, ax = plt.subplots(figsize=(12, 6))
internet_data = df.groupby('InternetService')['Churn_Binary'].mean() * 100
internet_data = internet_data.sort_values()
colors = ['#3498db', '#e74c3c', '#2ecc71']
ax.bar(internet_data.index, internet_data.values, color=colors, edgecolor='black')
ax.axhline(y=churn_rate, color='red', linestyle='--', label=f'Overall ({churn_rate:.1f}%)')
ax.set_title('Churn Rate by Internet Service', fontsize=14, fontweight='bold')
ax.set_ylabel('Churn Rate (%)')

plt.tight_layout()
plt.savefig(f'{charts_dir}/08_internet_service_vs_churn.png', dpi=150, bbox_inches='tight')
plt.close()

# ============================================================================
# SECTION 9: ADDITIONAL SERVICES VS CHURN
# ============================================================================
print("\n" + "="*70)
print("9. ADDITIONAL SERVICES VS CHURN ANALYSIS")


services = ['PhoneService', 'MultipleLines', 'OnlineSecurity', 'OnlineBackup',
            'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies']

print("\nChurn Rate by Additional Services:")
print(f"{'Service':<20} {'Without':<12} {'With':<12}")
print("-"*45)

service_churn_data = {}
for service in services:
    service_data = df[~df[service].isin(['No phone service', 'No internet service'])]
    without = service_data[service_data[service] == 'No']['Churn_Binary'].mean() * 100
    with_svc = service_data[service_data[service] == 'Yes']['Churn_Binary'].mean() * 100
    service_churn_data[service] = {'without': without, 'with': with_svc}
    print(f"{service:<20} {without:.1f}%      {with_svc:.1f}%")

fig, ax = plt.subplots(figsize=(14, 8))
services_short = ['Phone', 'Multiple Lines', 'Online Sec.', 'Online Backup',
                  'Device Prot.', 'Tech Support', 'Streaming TV', 'Streaming Movies']
x = np.arange(len(services_short))
width = 0.35

without_vals = [service_churn_data[s]['without'] for s in services]
with_vals = [service_churn_data[s]['with'] for s in services]

ax.bar(x - width/2, without_vals, width, label='Without Service', color='#e74c3c', edgecolor='black')
ax.bar(x + width/2, with_vals, width, label='With Service', color='#2ecc71', edgecolor='black')
ax.axhline(y=churn_rate, color='blue', linestyle='--', linewidth=2, label=f'Overall ({churn_rate:.1f}%)')
ax.set_title('Churn Rate by Additional Services', fontsize=14, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(services_short, rotation=45, ha='right')
ax.set_ylabel('Churn Rate (%)')
ax.legend()

plt.tight_layout()
plt.savefig(f'{charts_dir}/09_additional_services_vs_churn.png', dpi=150, bbox_inches='tight')
plt.close()

# ============================================================================
# CORRELATION HEATMAP
# ============================================================================
# Create a simple correlation visualization
numeric_cols = ['tenure', 'MonthlyCharges', 'TotalCharges', 'Churn_Binary']
corr_matrix = df[numeric_cols].corr()

fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, fmt='.3f', cmap='coolwarm', center=0, ax=ax)
ax.set_title('Correlation with Churn', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig(f'{charts_dir}/10_correlation_matrix.png', dpi=150, bbox_inches='tight')
plt.close()

print("\n" + "="*70)
print("ALL CHARTS GENERATED SUCCESSFULLY!")

print(f"\nCharts saved to: {charts_dir}/")