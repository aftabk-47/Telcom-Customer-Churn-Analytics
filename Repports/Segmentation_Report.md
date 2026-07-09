# CUSTOMER SEGMENTATION ANALYSIS REPORT

---

## 1. Segmentation Criteria

| Segment | Criteria |
|---|---|
| **High-Value Loyal** | Tenure ≥ 24 months, Monthly Charges ≥ $70, Did NOT Churn |
| **High-Value At-Risk** | (Churned OR Month-to-Month Contract) AND Monthly Charges ≥ $70 |
| **Low Engagement** | Tenure < 12 months, Monthly Charges < $70, ≤ 2 Services |

---

## 2. Segment Summary Table

| Segment | # Customers | Avg Tenure (mo) | Avg Monthly Charges | Revenue Contribution | Churn Rate |
|---|---|---|---|---|---|
| **High-Value Loyal** | 1,801 | 54.8 | $93.20 | $167,845/month | 0% (by definition) |
| **High-Value At-Risk** | 2,267 | 24.4 | $88.22 | $199,999 at risk | 56.2% (already churned) |
| **Low Engagement** | 1,030 | 3.8 | $34.15 | $35,175/month | 36.1% |

---

## 3. Individual Segment Analysis

### Segment 1: High-Value Loyal Customers

| Metric | Value |
|---|---|
| Number of customers | 1,801 |
| Average tenure | 54.8 months |
| Average monthly charges | $93.20 |
| Estimated annual revenue | $2,014,135 |

**Key Characteristics:**
- 72% are on fiber optic internet (premium service)
- 40% hold long-term contracts (two-year: 721, one-year: 553)
- 29% remain on month-to-month but are retained due to loyalty

**Business Recommendation:**
- **Reward loyalty** — Offer exclusive perks, priority support, and loyalty discounts
- **Referral program** — Leverage their satisfaction to bring in new customers
- **Upsell strategically** — They already pay premium; offer value-add services they don't yet have

---

### Segment 2: High-Value At-Risk Customers

| Metric | Value |
|---|---|
| Number of customers | 2,267 |
| Average tenure | 24.4 months |
| Average monthly charges | $88.22 |
| Revenue at risk | $199,999/month |
| Actual churners | 1,274 (56.2%) |

**Main Churn Characteristics:**
- 93% are on month-to-month contracts (very unstable)
- 59% use electronic check payment (highest churn payment method)
- 95% have fiber optic internet (premium but high-churn service)
- Average tenure of 24 months indicates mid-stage relationship

**Recommended Retention Strategy:**
1. **Immediate:** Offer 12-24 month contract incentives with 15-20% discount
2. **Payment migration:** Incentivize switch to automatic payments (credit card/bank transfer)
3. **Proactive outreach:** Contact at 12-month mark before contract renewal
4. **Service quality check:** Investigate fiber optic service issues driving churn

---

### Segment 3: Low Engagement Customers

| Metric | Value |
|---|---|
| Number of customers | 1,030 |
| Average tenure | 3.8 months |
| Average monthly charges | $34.15 |
| Churn rate | 36.1% |

**Key Characteristics:**
- 88% are on month-to-month contracts
- 51% use mailed check (indicates low tech comfort)
- Average only 3.8 months tenure — very new customers

**Business Recommendation:**
- **Improve onboarding** — 30/60/90 day check-ins for new customers
- **Bundle deals** — Offer discounted service bundles to increase engagement
- **Simplify options** — Provide easy-to-understand plans for low-engagement users

---

## 4. Which Segment to Prioritize First?

### Priority: High-Value At-Risk Customers

**Why this segment should be prioritized first:**

| Reason | Explanation |
|---|---|
| **Largest revenue exposure** | $200K/month at risk — more than any other segment |
| **Already churning** | 56.2% have already left; immediate action needed |
| **Recoverable** | These customers have shown willingness to pay premium; they just need stability |
| **Quick win potential** | Converting month-to-month to annual contracts has proven impact on churn reduction |

The High-Value At-Risk segment represents the **biggest opportunity for quick business impact**. Even a 10% reduction in this segment's churn would save approximately $20,000 monthly or $240,000 annually.

---

## 5. Three Overall Business Recommendations

### 1. Convert Month-to-Month to Annual Contracts

**Target:** High-Value At-Risk and Low Engagement segments

**Action:** Offer 15-20% discount for switching to annual contracts, plus bonus services (Tech Support, Online Security)

**Expected Impact:** Based on EDA, two-year contracts have 2.83% churn vs. 42.71% for month-to-month — this single change could reduce overall churn by 10-15%

---

### 2. Incentivize Automatic Payment Adoption

**Target:** All customers on electronic check

**Action:** Offer $5/month discount for switching to credit card or bank transfer auto-pay

**Expected Impact:** Auto-pay users have 15.24% churn vs. 45.29% for electronic check — this addresses one of the strongest predictors of churn

---

### 3. Strengthen New Customer Onboarding

**Target:** Low Engagement segment (new customers in first 12 months)

**Action:** Implement structured 30/60/90 day check-in program with proactive support and service bundle offers

**Expected Impact:** New customers have 47.68% churn rate; improved onboarding could reduce this by 20-30%, protecting future revenue

---

*Report prepared using rule-based segmentation from cleaned telco customer data.*