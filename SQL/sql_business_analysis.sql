create database customer_churn_db;
USE customer_churn_db;
show tables;
SELECT * FROM telco_churn_cleaned
limit 10 ;
ALTER table telco_churn_cleaned rename customer_churn;
SELECT * FROM customer_churn
limit 10 ;

select gender, count(*) from customer_churn
group by gender;

-- ==========================================================
-- CUSTOMER CHURN ANALYSIS
-- Telecom Customer Churn Dataset
-- Author: Aftab Khan
-- Database: customer_churn_db
-- Table: customer_churn

USE customer_churn_db;

-- ==========================================================
-- SECTION 1 : CUSTOMER OVERVIEW
-- ==========================================================

-- Q1. What is the total number of customers in the company?

SELECT COUNT(*) AS Total_Customers
FROM customer_churn;


-- Q2. How many customers have churned?

SELECT COUNT(*) AS Churned_Customers
FROM customer_churn
WHERE Churn = 'Yes';


-- Q3. What is the overall customer churn rate (%)?

SELECT
    ROUND(
        (SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END) * 100.0)
        / COUNT(*),
        2
    ) AS Churn_Rate
FROM customer_churn;


-- ==========================================================
-- SECTION 2 : REVENUE ANALYSIS
-- ==========================================================

-- Q4. What is the total monthly revenue generated from all customers?

SELECT
    ROUND(SUM(MonthlyCharges),2) AS Total_Monthly_Revenue
FROM customer_churn;


-- Q5. How much monthly revenue is at risk due to customer churn?

SELECT
    ROUND(SUM(MonthlyCharges),2) AS Revenue_At_Risk
FROM customer_churn
WHERE Churn='Yes';


-- Q6. What is the average monthly charge paid by customers?

SELECT
    ROUND(AVG(MonthlyCharges),2) AS Average_Monthly_Charge
FROM customer_churn;


-- Q7. Which contract type generates the highest monthly revenue?

SELECT
    Contract,
    COUNT(*) AS Customers,
    ROUND(SUM(MonthlyCharges),2) AS Revenue
FROM customer_churn
GROUP BY Contract
ORDER BY Revenue DESC;


-- ==========================================================
-- SECTION 3 : CUSTOMER BEHAVIOUR
-- ==========================================================

-- Q8. Which contract type has the highest customer churn rate?
SELECT Contract,
    COUNT(*) AS Total_Customers,
    SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END) AS Churned_Customers,
    ROUND(
        SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*),
        2
    ) AS Churn_Rate
FROM customer_churn
GROUP BY Contract
ORDER BY Churn_Rate DESC;


-- Q9. Which payment method has the highest churn rate?

SELECT
    PaymentMethod,
    COUNT(*) AS Customers,
    SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END) AS Churned_Customers,
    ROUND(
        SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*),
        2
    ) AS Churn_Rate
FROM customer_churn
GROUP BY PaymentMethod
ORDER BY Churn_Rate DESC;


-- Q10. How does churn vary across different internet service types?

SELECT
    InternetService,
    COUNT(*) AS Customers,
    SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END) AS Churned_Customers,
    ROUND(
        SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*),
        2
    ) AS Churn_Rate
FROM customer_churn
GROUP BY InternetService
ORDER BY Churn_Rate DESC;


-- Q11. Is customer churn different for male and female customers?
SELECT Gender, COUNT(*) AS Customers,
    SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END) AS Churned_Customers,
    ROUND(
        SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*),
        2
    ) AS Churn_Rate
FROM customer_churn
GROUP BY Gender;


-- Q12. Do senior citizens churn more than non-senior customers?

SELECT
    SeniorCitizen,
    COUNT(*) AS Customers,
    SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END) AS Churned_Customers,
    ROUND(
        SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*),
        2
    ) AS Churn_Rate
FROM customer_churn
GROUP BY SeniorCitizen;


-- ==========================================================
-- SECTION 4 : CUSTOMER VALUE
-- ==========================================================

-- Q13. What is the average customer tenure?

SELECT
    ROUND(AVG(Tenure),2) AS Average_Tenure
FROM customer_churn;


-- Q14. Who are the top 10 highest paying customers?

SELECT
    CustomerID,
    MonthlyCharges,
    Tenure,
    Contract
FROM customer_churn
ORDER BY MonthlyCharges DESC
LIMIT 10;


-- Q15. Which customers pay above the company's average monthly charge?

SELECT
    CustomerID,
    MonthlyCharges,
    Contract
FROM customer_churn
WHERE MonthlyCharges >
(
    SELECT AVG(MonthlyCharges)
    FROM customer_churn
)
ORDER BY MonthlyCharges DESC;


-- Q16. What is the estimated average Customer Lifetime Value (CLV) by contract type?

SELECT
    Contract,
    ROUND(AVG(MonthlyCharges * Tenure),2) AS Estimated_CLV
FROM customer_churn
GROUP BY Contract
ORDER BY Estimated_CLV DESC;


-- ==========================================================
-- SECTION 5 : RETENTION OPPORTUNITIES
-- ==========================================================

-- Q17. Which high-value customers have already churned?
SELECT CustomerID, MonthlyCharges, Tenure, Contract
FROM customer_churn
WHERE Churn='Yes'
AND MonthlyCharges >
(
    SELECT AVG(MonthlyCharges)
    FROM customer_churn
)
ORDER BY MonthlyCharges DESC;


-- Q18. How many customers do not subscribe to Tech Support?

SELECT
    COUNT(*) AS Customers_Without_TechSupport
FROM customer_churn
WHERE TechSupport='No';


-- Q19. How many customers do not subscribe to Online Security?

SELECT
    COUNT(*) AS Customers_Without_OnlineSecurity
FROM customer_churn
WHERE OnlineSecurity='No';


-- Q20. Which month-to-month customers pay above average monthly charges?

SELECT
    CustomerID,
    MonthlyCharges,
    Tenure
FROM customer_churn
WHERE Contract='Month-to-month'
AND MonthlyCharges >
(
    SELECT AVG(MonthlyCharges)
    FROM customer_churn
)
ORDER BY MonthlyCharges DESC;

