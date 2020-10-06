# A/B Test Analyses 
Analyzed results from A/B test launched by a predecessor of whom only the technical specifications and the test results.

Data completed: August, 2020


**Project description:** 
Hello this is my submission for the AB Test sub-project (part of the graduation project) submission from Practicum by Yandex's Data Analyst program. You can find more about the Data Analyst by clicking [here.](https://practicum.yandex.com/data-analyst/)

> You've received an analytical task from an international online store. Your predecessor failed to complete it: they launched an A/B test and then quit (to start a watermelon farm in Brazil). They left only the technical specifications and the test results.

## Goal
Test whether the new recommendation system was able to increase conversion rates by at 10% per each stage in the funnel
## Tech description
**Date**: 2020-12-07 - 2021-01-01 (date stopped taking in new users -> 2020-12-21)

**Purpose of the test**: testing changes related to the introduction of an improved recommendation system

**Expected result**: within 14 days of signing up, users will show better conversion into product page views (the product_page event), product card views (product_card) and purchases (purchase). 

**At each of the stage of the funnel**: product_page → product_card → purchase, there will be at least a 10% increase. -> compared to first day -> per user make two columns (first and 14 days after conversion rates) (may need to drop some users)
**Audience:** 15% of the new users from the EU region
**Expected number of test participants:** 6000

## Metrics:
- Product page view # of product page views / total view
- Product card view # of product_card views/ total view
- Purchases: bought / did not buy (or bought / unique visits)

## Findings
- Unique user conversion **did not statistically differ** for events in the **product page and product cart page**.
- For the **purchase page**, users in the **control group converted 2.36%** better than the experimental group and this difference was found to be **statistically significant** (p < .03).
 - In terms of the result, this may have been that there are more users that were concentrated in the purchase stage (from funnel findings) which warrants further testing.
- It **seems likely** that users in **group A** were **disproportionately shared direct links to the purchase page** more often than users in group B, hence the difference in # of purchase. A further follow up analysis can be done to assess effectiveness of the purchase page redirect link.
 
### Figures

#### Figure 1.
<img src="images/Screenshot_442.png?raw=true" width="50%" height="50%"/>

#### Figure 2.
<img src="images/Screenshot_443.png?raw=true" width="70%" height="70%"/>

#### Figure 3.
<img src="images/Screenshot_444.png?raw=true" width="80%" height="80%"/>

