# Customer Segmentation Report

## Project Name

RetailIQ: E-commerce Customer Churn Prediction Platform

---

## Objective

The objective of customer segmentation is to group customers based on similar behavior patterns such as spending behavior, purchase frequency, rating behavior, discount usage, and churn tendency.

This helps business owners understand different customer groups and take targeted business actions.

---

## Segmentation Method

The customer segmentation model uses:

```text
K-Means Clustering
```

Number of clusters:

```text
4
```

The model groups customers into four business-friendly segments.

---

## Features Used for Segmentation

The following features were used to create customer segments:

* age
* total_spend
* items_purchased
* average_rating
* avg_spend_per_item
* discount_used_flag
* low_rating_flag
* is_high_value_customer
* is_frequent_buyer

---

## Model Quality

Silhouette Score:

```text
0.2898
```

A silhouette score of 0.2898 is acceptable for customer behavior segmentation because customer groups often overlap in real business data.

The goal of this segmentation model is not only mathematical separation, but also business interpretability.

---

## Segment Distribution

| Segment Name                | Number of Customers |
| --------------------------- | ------------------: |
| Satisfied Regular Customers |              47,380 |
| High Value Customers        |              21,323 |
| At Risk Customers           |              20,277 |
| Low Engagement Customers    |              11,020 |

---

## Segment Summary

| Segment Name                | Customers | Avg Total Spend | Avg Items Purchased | Avg Rating | Churn Rate |
| --------------------------- | --------: | --------------: | ------------------: | ---------: | ---------: |
| At Risk Customers           |    20,277 |          241.43 |                3.93 |       2.33 |       0.88 |
| High Value Customers        |    21,323 |          616.73 |               12.77 |       3.96 |       0.19 |
| Low Engagement Customers    |    11,020 |          299.17 |               10.36 |       3.43 |       0.72 |
| Satisfied Regular Customers |    47,380 |          229.66 |                3.82 |       3.94 |       0.64 |

---

## Business Interpretation

### 1. High Value Customers

High Value Customers have the highest average spend and purchase more items compared to other groups.

Key observations:

* Average spend: 616.73
* Average items purchased: 12.77
* Average rating: 3.96
* Churn rate: 0.19

Business action:

* Provide loyalty rewards
* Offer early access to premium products
* Keep them engaged with personalized communication
* Avoid unnecessary over-discounting because they already spend well

---

### 2. At Risk Customers

At Risk Customers have low average ratings and very high churn rate.

Key observations:

* Average spend: 241.43
* Average items purchased: 3.93
* Average rating: 2.33
* Churn rate: 0.88

Business action:

* Send retention offers
* Collect customer feedback
* Run customer satisfaction recovery campaigns
* Provide personal follow-up or support
* Offer discount coupons carefully to regain trust

---

### 3. Low Engagement Customers

Low Engagement Customers purchase a reasonable number of items but have a high churn rate.

Key observations:

* Average spend: 299.17
* Average items purchased: 10.36
* Average rating: 3.43
* Churn rate: 0.72

Business action:

* Send re-engagement campaigns
* Recommend relevant products
* Offer limited-time deals
* Improve product discovery and communication
* Encourage repeat purchases through personalized offers

---

### 4. Satisfied Regular Customers

Satisfied Regular Customers are the largest customer group and have good average ratings.

Key observations:

* Customers: 47,380
* Average spend: 229.66
* Average items purchased: 3.82
* Average rating: 3.94
* Churn rate: 0.64

Business action:

* Convert them into loyal or high-value customers
* Offer membership upgrades
* Recommend bundled products
* Encourage repeat purchases
* Use personalized offers to increase average order value

---

## Owner-Level Dashboard Insights

This segmentation can be used in the dashboard to show:

* Total customers by segment
* Revenue contribution by segment
* Churn rate by segment
* Average spend by segment
* Average rating by segment
* Recommended actions for each segment
* Priority customers for retention campaigns

---

## Business Priority

Recommended priority order:

1. At Risk Customers
2. Low Engagement Customers
3. Satisfied Regular Customers
4. High Value Customers

Reason:

At Risk and Low Engagement customers have high churn rates, so retention campaigns should focus there first.

High Value Customers should be protected through loyalty and premium engagement programs.

Satisfied Regular Customers should be nurtured and converted into higher-value customers.

---

## Output Files

The segmentation pipeline generates:

```text
models/segmentation_model.pkl
models/segmentation_scaler.pkl
data/processed/customer_segments.csv
```

These files are generated locally and are not pushed to GitHub because they are ignored using `.gitignore`.

---

## How This Helps the Business

The segmentation model helps the business answer important questions:

* Which customer group is most valuable?
* Which customers are most likely to churn?
* Which customers need retention offers?
* Which customer group should receive loyalty rewards?
* Which group needs re-engagement campaigns?
* Which group can be targeted for membership upgrades?

---

## Future Improvements

* Test different cluster counts using elbow method
* Compare K-Means with DBSCAN or Gaussian Mixture Models
* Add transaction history features
* Add recency-frequency-monetary analysis
* Add segment-level customer lifetime value
* Add segment-level revenue contribution
* Visualize customer clusters in Streamlit dashboard
* Add segment filters in owner dashboard
