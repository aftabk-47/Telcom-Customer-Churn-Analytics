# TELECOM CUSTOMER CHURN - BUSINESS PERFORMANCE REPORT

---

## 1. KPI Summary Table

| KPI | Value |
|---|---|
| **Total Customers** | 7,043 |
| **Churn Rate** | 26.54% |
| **Revenue at Risk** (Monthly Charges of Churned Customers) | $139,130.85 |
| **Average Customer Lifetime Value (CLV)** | $2,279.58 |
| **Average Customer Tenure** | 32.37 months |

---

## 2. Business Question Analysis

### Question 1: Which customer groups generate the highest revenue?

| Customer Group | Monthly Revenue |
|---|---|
| **Fiber optic internet** | $283,284.40 |
| Month-to-month contracts | $257,294.15 |
| Electronic check payments | $180,345.00 |
| Long-tenure customers (49-72 months) | $165,563.70 |

**Finding:** Fiber optic customers generate the highest revenue ($283K/month), followed by month-to-month contract holders. Interestingly, customers with 49-72 months tenure also contribute significantly despite being fewer in number.

---

### Question 2: Which customer groups have the highest churn rate?

| Customer Group | Churn Rate |
|---|---|
| **Month-to-month contracts** | 42.71% |
| **Electronic check payment** | 45.29% |
| **Fiber optic internet** | 41.89% |
| New customers (0-12 months tenure) | 47.68% |

**Finding:** Month-to-month contract holders churn at 42.71% — nearly 16× higher than two-year contract customers (2.83%). Electronic check users churn at 45.29%, and fiber optic customers at 41.89%. New customers in their first year have the highest churn rate at 47.68%.

---

### Question 3: Which customer groups should be prioritized for retention?

| Priority Segment | Churn Rate | Monthly Revenue |
|---|---|---|
| Month-to-month + Fiber optic | 54.6% | $185,181 |
| Electronic check + Fiber optic | 53.2% | $143,046 |
| New customers (0-12 months) | 47.4% | $122,630 |

**Finding:** The most critical retention priority is the **Month-to-month + Fiber optic** segment — these customers have a 54.6% churn rate and generate $185K monthly. These are high-value customers behaving like high-risk ones.

---

### Question 4: What is the estimated business impact of customer churn?

| Impact Metric | Value |
|---|---|
| Monthly revenue at risk | $139,130.85 |
| Average revenue lost per churned customer | $74.44/month |
| Average CLV lost per churned customer | $1,531.61 |
| Average tenure lost | 18.0 months vs 37.6 months (retained) |

**Finding:** Churned customers have nearly half the CLV of retained customers ($1,532 vs $2,550). The company loses approximately $139K in monthly recurring revenue, with each churned customer representing $1,018 less lifetime value than a retained customer.

---

## 3. Top Five Business Insights

### Insight 1: Contract Type is the Strongest Churn Predictor

**Finding:** Month-to-month customers churn at 42.71% compared to just 2.83% for two-year contracts.

**Business Impact:** Short-term contracts create unstable revenue and high acquisition costs with little return.

**Recommendation:** Offer strong incentives (discounts, bonus services) for customers to switch from month-to-month to annual contracts. Consider loyalty rewards after 12 months of tenure.

---

### Insight 2: Fiber Optic Customers Are High-Value but High-Risk

**Finding:** Fiber optic generates the most revenue ($283K/month) but also has the highest churn rate (41.89%).

**Business Impact:** This premium service segment is driving revenue but bleeding customers at an alarming rate. The combination of high monthly charges + month-to-month flexibility creates a volatile mix.

**Recommendation:** Target fiber optic customers with proactive retention offers before contract renewal. Investigate service quality issues specific to fiber optic that may be driving churn.

---

### Insight 3: Electronic Check Users Need Attention

**Finding:** Customers paying by electronic check have a 45.29% churn rate — nearly 3× higher than credit card auto-pay users (15.24%).

**Business Impact:** This payment method indicates customers who may not have established automated payment habits and are more likely to switch providers.

**Recommendation:** Offer discounts or rewards for customers who switch to automatic payment methods (credit card or bank transfer). Auto-pay reduces churn and improves cash flow.

---

### Insight 4: New Customers Are the Most Vulnerable

**Finding:** Customers with 0-12 months tenure have a 47.68% churn rate — the highest of any tenure group.

**Business Impact:** Early-stage customers are most likely to leave, wasting acquisition costs before ROI materializes.

**Recommendation:** Implement a structured onboarding program with check-ins at 30, 60, and 90 days. Offer new customer promotions and proactive support during the first year.

---

### Insight 5: Add-on Services Significantly Reduce Churn

**Finding:** Customers without Online Security (41.8% churn) vs. with Online Security (14.6% churn). Similar patterns exist for Tech Support (41.6% vs 15.2%) and Device Protection (39.1% vs 22.5%).

**Business Impact:** Each additional service a customer has creates "switching cost" and deeper engagement, reducing churn likelihood.

**Recommendation:** Bundle add-on services at discounted rates for new customers. Focus on selling Online Security and Tech Support first — they show the largest drop in churn rates.

---

## 4. Short Conclusion

The telecommunications company faces a 26.54% churn rate that translates to **$139,131 in monthly revenue at risk**. The data clearly shows that **contract type, payment method, and tenure** are the strongest indicators of churn risk. Month-to-month customers on fiber optic plans using electronic check are the highest-risk segment. By focusing retention efforts on new customers (0-12 months), converting month-to-month contracts to annual plans, and encouraging automatic payment adoption, the company can significantly reduce churn and protect over $1.6M in annual recurring revenue.

---

*Report prepared using cleaned telco customer data and exploratory data analysis findings.*