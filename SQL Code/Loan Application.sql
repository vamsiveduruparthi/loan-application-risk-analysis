-- ============================================
-- LOAN APPLICATION & RISK ANALYSIS
-- ============================================


-- 1. View the dataset
SELECT *
FROM loan_applications;


-- 2. Total number of applications
SELECT COUNT(*) AS total_applications
FROM loan_applications;


-- 3. Approved applications
SELECT COUNT(*) AS approved_applications
FROM loan_applications
WHERE Loan_Status = 'Approved';


-- 4. Rejected applications
SELECT COUNT(*) AS rejected_applications
FROM loan_applications
WHERE Loan_Status = 'Rejected';


-- 5. Overall approval rate
SELECT
    ROUND(
        100.0 * SUM(
            CASE WHEN Loan_Status = 'Approved' THEN 1 ELSE 0 END
        ) / COUNT(*),
        2
    ) AS approval_rate
FROM loan_applications;


-- 6. Total and average loan amount
SELECT
    SUM(Loan_Amount) AS total_loan_amount,
    AVG(Loan_Amount) AS average_loan_amount
FROM loan_applications;


-- 7. Average credit score, income, interest rate and DTI
SELECT
    AVG(Credit_Score) AS average_credit_score,
    AVG(Annual_Income) AS average_annual_income,
    AVG(Interest_Rate) AS average_interest_rate,
    AVG(DTI_Ratio) AS average_dti_ratio
FROM loan_applications;


-- 8. Applications by region
SELECT
    Region,
    COUNT(*) AS applications
FROM loan_applications
GROUP BY Region
ORDER BY applications DESC;


-- 9. Applications by employment
SELECT
    Employment,
    COUNT(*) AS applications
FROM loan_applications
GROUP BY Employment
ORDER BY applications DESC;


-- 10. Applications by loan purpose
SELECT
    Loan_Purpose,
    COUNT(*) AS applications
FROM loan_applications
GROUP BY Loan_Purpose
ORDER BY applications DESC;


-- 11. Total loan amount by purpose
SELECT
    Loan_Purpose,
    SUM(Loan_Amount) AS total_loan_amount
FROM loan_applications
GROUP BY Loan_Purpose
ORDER BY total_loan_amount DESC;


-- 12. Average loan amount by region
SELECT
    Region,
    AVG(Loan_Amount) AS average_loan_amount
FROM loan_applications
GROUP BY Region
ORDER BY average_loan_amount DESC;


-- 13. Average loan amount by employment
SELECT
    Employment,
    AVG(Loan_Amount) AS average_loan_amount
FROM loan_applications
GROUP BY Employment
ORDER BY average_loan_amount DESC;


-- 14. Applications by credit category
SELECT
    Credit_Category,
    COUNT(*) AS applications
FROM loan_applications
GROUP BY Credit_Category
ORDER BY applications DESC;


-- 15. Approval rate by credit category
SELECT
    Credit_Category,
    COUNT(*) AS applications,
    SUM(
        CASE WHEN Loan_Status = 'Approved' THEN 1 ELSE 0 END
    ) AS approved_applications,
    ROUND(
        100.0 * SUM(
            CASE WHEN Loan_Status = 'Approved' THEN 1 ELSE 0 END
        ) / COUNT(*),
        2
    ) AS approval_rate
FROM loan_applications
GROUP BY Credit_Category
ORDER BY approval_rate DESC;


-- 16. Average loan amount by credit category
SELECT
    Credit_Category,
    AVG(Loan_Amount) AS average_loan_amount
FROM loan_applications
GROUP BY Credit_Category
ORDER BY average_loan_amount DESC;


-- 17. Average interest rate by credit category
SELECT
    Credit_Category,
    AVG(Interest_Rate) AS average_interest_rate
FROM loan_applications
GROUP BY Credit_Category
ORDER BY average_interest_rate DESC;


-- 18. Average DTI ratio by loan status
SELECT
    Loan_Status,
    AVG(DTI_Ratio) AS average_dti_ratio
FROM loan_applications
GROUP BY Loan_Status
ORDER BY average_dti_ratio DESC;


-- 19. Average annual income by loan status
SELECT
    Loan_Status,
    AVG(Annual_Income) AS average_annual_income
FROM loan_applications
GROUP BY Loan_Status
ORDER BY average_annual_income DESC;


-- 20. Average loan amount by loan status
SELECT
    Loan_Status,
    AVG(Loan_Amount) AS average_loan_amount
FROM loan_applications
GROUP BY Loan_Status
ORDER BY average_loan_amount DESC;


-- 21. Applications by loan term
SELECT
    Loan_Term_Months,
    COUNT(*) AS applications
FROM loan_applications
GROUP BY Loan_Term_Months
ORDER BY Loan_Term_Months;


-- 22. Approval rate by employment
SELECT
    Employment,
    COUNT(*) AS applications,
    SUM(
        CASE WHEN Loan_Status = 'Approved' THEN 1 ELSE 0 END
    ) AS approved_applications,
    ROUND(
        100.0 * SUM(
            CASE WHEN Loan_Status = 'Approved' THEN 1 ELSE 0 END
        ) / COUNT(*),
        2
    ) AS approval_rate
FROM loan_applications
GROUP BY Employment
ORDER BY approval_rate DESC;


-- 23. Approval rate by region
SELECT
    Region,
    COUNT(*) AS applications,
    SUM(
        CASE WHEN Loan_Status = 'Approved' THEN 1 ELSE 0 END
    ) AS approved_applications,
    ROUND(
        100.0 * SUM(
            CASE WHEN Loan_Status = 'Approved' THEN 1 ELSE 0 END
        ) / COUNT(*),
        2
    ) AS approval_rate
FROM loan_applications
GROUP BY Region
ORDER BY approval_rate DESC;


-- 24. Loan status distribution
SELECT
    Loan_Status,
    COUNT(*) AS applications
FROM loan_applications
GROUP BY Loan_Status
ORDER BY applications DESC;


-- 25. Credit category and loan status analysis
SELECT
    Credit_Category,
    Loan_Status,
    COUNT(*) AS applications
FROM loan_applications
GROUP BY Credit_Category, Loan_Status
ORDER BY Credit_Category, applications DESC;


-- 26. High-DTI applications
SELECT
    Loan_ID,
    Customer_ID,
    DTI_Ratio,
    Loan_Amount,
    Credit_Score,
    Loan_Status
FROM loan_applications
WHERE DTI_Ratio >= 0.75
ORDER BY DTI_Ratio DESC;


-- 27. High-value loans
SELECT
    Loan_ID,
    Customer_ID,
    Loan_Amount,
    Annual_Income,
    Credit_Score,
    DTI_Ratio,
    Loan_Status
FROM loan_applications
WHERE Loan_Amount >= 1000000
ORDER BY Loan_Amount DESC;


-- 28. Approved applications by credit category
SELECT
    Credit_Category,
    COUNT(*) AS approved_applications
FROM loan_applications
WHERE Loan_Status = 'Approved'
GROUP BY Credit_Category
ORDER BY approved_applications DESC;


-- 29. Approved applications by employment
SELECT
    Employment,
    COUNT(*) AS approved_applications
FROM loan_applications
WHERE Loan_Status = 'Approved'
GROUP BY Employment
ORDER BY approved_applications DESC;


-- 30. Regional loan portfolio
SELECT
    Region,
    COUNT(*) AS applications,
    SUM(Loan_Amount) AS total_loan_amount,
    AVG(Loan_Amount) AS average_loan_amount,
    AVG(Credit_Score) AS average_credit_score
FROM loan_applications
GROUP BY Region
ORDER BY total_loan_amount DESC;
