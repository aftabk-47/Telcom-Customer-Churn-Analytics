# Telco Customer Churn - Comprehensive Exploratory Data Analysis

## Executive Summary

This analysis examines **7,043 telecom customers** to identify patterns and factors associated with customer churn. The overall churn rate is **26.54%** (1,869 customers), which is significantly higher than the industry average of 15-20%.

---

## 1. Churn Distribution

| Status | Count | Percentage |
|--------|-------|------------|
| Retained | 5,174 | 73.46% |
| Churned | 1,869 | 26.54% |

**Finding:** The company is losing more than 1 in 4 customers, indicating a critical retention problem.

---

## 2. Demographics vs Churn

### 2a. Gender
- Female: 26.92% churn rate
- Male: 26.16% churn rate
- **Statistical Significance:** NOT significant (p = 0.487)
- **Business Implication:** Gender has no meaningful impact on churn.

### 2b. Senior Citizens
- Non-senior: 23.61% churn rate
- Senior: 41.68% churn rate
- **Statistical Significance:** HIGHLY significant (p < 0.001)
- **Business Implication:** Seniors churn at 1.76x the rate of non-seniors. This group needs specialized retention strategies.

### 2c. Partner Status
- Without partner: 32.96% churn rate
- With partner: 19.66% churn rate
- **Statistical Significance:** HIGHLY significant (p < 0.001)
- **Business Implication:** Single customers churn 1.68x more than those with partners.

### 2d. Dependents
- No dependents: 31.28% churn rate
- Has dependents: 15.45% churn rate
- **Statistical Significance:** HIGHLY significant (p < 0.001)
- **Business Implication:** Customers with family commitments show stronger loyalty.

---

## 3. Tenure vs Churn

| Tenure (months) | Churn Rate | Customers |
|-----------------|------------|-----------|
| 0-12 | 47.68% | 2,175 |
| 13-24 | 28.71% | 1,024 |
| 25-36 | 21.63% | 832 |
| 37-48 | 19.03% | 762 |
| 49-72 | 9.51% | 2,239 |

**Key Statistics:**
- Avg tenure (Churned): 18 months
- Avg tenure (Retained): 37.6 months
- **Correlation with Churn:** -0.35 (strong negative)

**Business Implication:** New customers (first 12 months) are 5x more likely to churn than long-term customers. The first year is the critical retention window.

---

## 4. Monthly Charges vs Churn

| Monthly Charges | Churn Rate | Customers |
|-----------------|------------|-----------|
| $0-35 | 10.89% | 1,735 |
| $36-55 | 27.98% | 897 |
| $56-75 | 26.96% | 1,291 |
| $76-95 | 36.33% | 1,825 |
| $96+ | 32.28% | 1,295 |

**Key Statistics:**
- Avg Monthly Charges (Churned): $74.44
- Avg Monthly Charges (Retained): $61.27
- **Correlation with Churn:** +0.19 (positive)

**Business Implication:** Higher monthly bills correlate with higher churn. Price sensitivity is evident at higher price points.

---

## 5. Total Charges vs Churn

| Total Charges | Churn Rate | Customers |
|---------------|------------|-----------|
| $0-500 | 41.45% | 2,000 |
| $501-1500 | 24.80% | 1,661 |
| $1501-3000 | 23.82% | 1,167 |
| $3001-5000 | 18.05% | 1,069 |
| $5000+ | 13.83% | 1,135 |

**Key Statistics:**
- Avg Total Charges (Churned): $1,531.80
- Avg Total Charges (Retained): $2,549.91
- **Correlation with Churn:** -0.20 (negative)

**Business Implication:** Low-value customers (low total charges) churn more. These are often newer customers who haven't built up investment in the service.

---

## 6. Contract Type vs Churn

| Contract Type | Churn Rate | Customers |
|---------------|------------|-----------|
| Month-to-month | 42.71% | 3,875 |
| One year | 11.27% | 1,473 |
| Two year | 2.83% | 1,695 |

**Statistical Significance:** Extremely significant (χ² = 1184.60, p < 0.001)

**Business Implication:** This is the **#1 predictor of churn**. Month-to-month customers are:
- 15x more likely to churn than two-year customers
- 3.8x more likely to churn than one-year customers

---

## 7. Payment Method vs Churn

| Payment Method | Churn Rate | Customers |
|----------------|------------|-----------|
| Electronic check | 45.29% | 2,365 |
| Mailed check | 19.11% | 1,612 |
| Bank transfer (auto) | 16.71% | 1,544 |
| Credit card (auto) | 15.24% | 1,522 |

**Statistical Significance:** Extremely significant (χ² = 648.14, p < 0.001)

**Business Implication:** Electronic check users churn at 3x the rate of automatic payment methods. Manual payment = higher churn.

---

## 8. Internet Service vs Churn

| Internet Service | Churn Rate | Customers |
|------------------|------------|-----------|
| Fiber optic | 41.89% | 3,096 |
| DSL | 18.96% | 2,421 |
| No internet | 7.40% | 1,526 |

**Statistical Significance:** Extremely significant (χ² = 732.31, p < 0.001)

**Business Implication:** **Fiber optic customers churn at 2.2x the rate of DSL!** This counter-intuitive finding suggests:
- Pricing issues with fiber optic service
- Quality of service problems
- Competitor pressure in fiber markets

---

## 9. Additional Services vs Churn

| Service | Without | With | Difference |
|---------|---------|------|------------|
| Online Security | 41.8% | 14.6% | -65% |
| Tech Support | 41.6% | 15.2% | -63% |
| Online Backup | 39.9% | 21.5% | -46% |
| Device Protection | 39.1% | 22.5% | -42% |
| Streaming TV | 33.5% | 30.1% | -10% |
| Streaming Movies | 33.7% | 29.9% | -11% |
| Multiple Lines | 25.0% | 28.6% | +14% |
| Phone Service | 24.9% | 26.7% | +7% |

**Statistical Significance:** Online Security, Tech Support, Online Backup, and Device Protection are all highly significant (p < 0.001).

**Business Implication:** Add-on services (especially security and support) dramatically reduce churn. Customers who subscribe to 3+ additional services rarely churn.

---

## 10. Correlation Analysis

| Variable | Correlation with Churn |
|----------|----------------------|
| Tenure | -0.35 |
| Total Charges | -0.20 |
| Monthly Charges | +0.19 |

**Interpretation:**
- Longer tenure = lower churn (strongest predictor)
- Higher total charges = lower churn (customers with investment)
- Higher monthly charges = higher churn (price sensitivity)

---

# TOP 10 BUSINESS FINDINGS

## 1. CONTRACT TYPE IS THE STRONGEST PREDICTOR OF CHURN
- **Finding:** Month-to-month customers churn at 42.7% vs 2.8% for two-year
- **Impact:** 15x difference in churn risk
- **Action:** Aggressively promote annual/two-year contracts with incentives

## 2. FIBER OPTIC INTERNET HAS UNEXPECTEDLY HIGH CHURN
- **Finding:** Fiber optic customers churn at 41.9% vs DSL at 19.0%
- **Impact:** 2.2x higher risk
- **Action:** Review fiber pricing, service quality, and competitive positioning

## 3. FIRST 12 MONTHS ARE CRITICAL FOR RETENTION
- **Finding:** New customers (0-12 months) churn at 47.7%
- **Impact:** First-year churn is 5x higher than after year 4
- **Action:** Implement strong onboarding and early engagement programs

## 4. TECH SUPPORT AND SECURITY SERVICES DRIVE RETENTION
- **Finding:** Tech support reduces churn by 63%, online security by 65%
- **Impact:** Customers with these services have <15% churn
- **Action:** Offer free trials or bundled security/support packages

## 5. ELECTRONIC CHECK USERS ARE HIGH-RISK
- **Finding:** Electronic check users churn at 45.3% vs 15.2% for auto credit card
- **Impact:** 3x higher risk
- **Action:** Incentivize enrollment in automatic payment methods

## 6. SENIOR CITIZENS NEED SPECIALIZED RETENTION
- **Finding:** Seniors churn at 41.7% vs 23.6% for non-seniors
- **Impact:** 1.8x higher risk
- **Action:** Develop senior-specific retention programs and support

## 7. SINGLES WITHOUT DEPENDENTS CHURN MORE
- **Finding:** Single customers (no partner) churn at 33.0% vs 19.7%
- **Impact:** 1.7x higher risk
- **Action:** Targeted offers for individual/single customers

## 8. LOW-VALUE CUSTOMERS CHURN MORE
- **Finding:** Customers with <$500 total charges churn at 41.5%
- **Impact:** These are typically new or low-engagement customers
- **Action:** Early engagement and value demonstration in first months

## 9. HIGH MONTHLY CHARGES CORRELATE WITH CHURN
- **Finding:** Customers paying $76-95/month have 36.3% churn rate
- **Impact:** Price sensitivity at higher tiers
- **Action:** Review pricing strategy, consider loyalty discounts

## 10. ADD-ON SERVICES CREATE LOYALTY
- **Finding:** Customers with 3+ additional services rarely churn
- **Impact:** Service bundling creates stickiness
- **Action:** Promote service bundles at signup and during tenure

---

# REVENUE IMPACT ANALYSIS

| Metric | Value |
|--------|-------|
| Total Customers | 7,043 |
| Churned Customers | 1,869 |
| Overall Churn Rate | 26.54% |
| Avg Monthly Revenue | $64.05 |
| Estimated Annual Revenue Loss | ~$1.44M |

## Projected Savings from Churn Reduction:

| Scenario | Reduction | Annual Savings |
|----------|-----------|-----------------|
| Reduce to 20% | 6.5% pts | ~$360K |
| Reduce to 15% (industry avg) | 11.5% pts | ~$640K |
| Target: 10% | 16.5% pts | ~$920K |

---

# RECOMMENDED ACTION PLAN

### Immediate (0-3 months):
1. Launch automatic payment migration campaign
2. Offer month-to-month customers 6 months free for annual contract
3. Provide free tech support trial to all new customers

### Short-term (3-6 months):
4. Investigate fiber optic service quality/pricing issues
5. Develop senior citizen retention program
6. Create onboarding program for first 12 months

### Medium-term (6-12 months):
7. Implement security service bundle at signup
8. Review pricing for $70+ monthly tier
9. Develop targeted offers for single customers

---

*Analysis generated from telco_churn_cleaned.csv (7,043 records)*  
*Charts available in charts/ directory*