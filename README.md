# fetch-analytics-eng-application

# Structured Relational Data Model

The three data models that would be present in the data warehouse are as follows:

`brands`


![alt text](image.png)

`users`


![alt text](image-1.png)

`receipts`


![alt text](image-2.png)


# Queries for Business Stakeholders
        
        
- The file `queries\average_receipt_spend_by_status.sql` contains a query that will display information about the average amount spent by users for `Accepted` and `Rejected` receipt statuses.

- The file `queries\number_items_purchased_by_receipt_status.sql` contains a query that will display information about the total number of items users purchased for `Accepted` and `Rejected` receipt statuses.

- The file `queries\top_5_brands_by_receipts.sql` contains a query that will display the top 5 brands, according to amount spent by consumers, within the month of April. The dates within the query may be changed to inspect different time periods as well.

# Data Quality Issues

Analysis performed by running `scripts/analyze_datasets.py`

- `brands.jsonl`
- Analysis shows that of all brands in the file, 76% are unique, and 30% are invalid "Test" brands. Additionally, very few of the records (fewer than 3%) are marked as top brands, and 52% of entries are missing the topBrand field. Additionally, 23% of the records are missing a brand code.
    - Percentage of unique brands in file: 76.8 %
    - Percentage of invalid brands in file: 30.8 %
    - Percentage of top brands in file: 2.7 %
    - Percentage of entries missing brand codes: 23.1 %
    - Percentage of entries missing top brand flag: 52.4 %
- `receipts.jsonl`
- Analysis shows that a majority of receipts are in the `Submitted` or `Finished` status, with minorities in `Flagged`, `Rejected`, and `Pending`. There were no receipts in the data with a status of `Accepted`. Based on the provided data, consumers purchased an average of 6 items with each receipt. Additionally, over 30% of receipts had just one item. Almost 40% of the receipts had zero items, bringing into question the overall quality of the dataset.
    - Counts of receipt statuses: {'FLAGGED': 46, 'SUBMITTED': 434, 'REJECTED': 71, 'PENDING': 50, 'FINISHED': 518}
    - Average number of items purchased by consumers: 6.2
    - Percentage of receipts with just one item: 33.7 %
    - Percentage of receipts with zero items: 39.3 %

- `users.jsonl`
- Analysis shows that a majority of users reside in Wisconsin, with a handful of users throughout other states including KY, AL, CO, IL, OH, SC, and NH. A majority of users signed up via email with a very small minority signing up via google. Roughly 80% of users in the dataset are true consumers while roughly 20% are fetch staff. Data quality issues are present in this dataset with ~10% of users without a signup source and 11% of users without a state.
    - Counts of users per state: {'WI': 396, 'KY': 1, 'AL': 12, 'CO': 1, 'IL': 3, 'OH': 5, 'SC': 1, 'NH': 20}
    - Counts of users per signup source: {'Email': 443, 'Google': 4}
    - Counts of users per role: {'consumer': 413, 'fetch-staff': 82}
    - Percentage of users without signup source: 9.7 %
    - Percentage of users without state: 11.3 %

# Clairfying Questions

Dear Product Manager,

Thank you for providing our team with valuable data upon which to base our new data warehouse models for brands, receipts, and users. We have constructed some preliminary data models, complete with some sample queries above. Additionally, we have analyzed the data to check its integrity and quality.

Although this is an excellent starting point, we have some key issues to address before moving forward with the project. These details may seem small, but it is imperative to handle them to ensure that the data warehouse gets populated with high-quality, informative data that can deliver value to the business.

1. The `brands` data:


This dataset contained a lot of interesting and relevant records about different brands, but these were diluted by a lot of "test" entries that did not represent real brands and entries simply not labeled with a brand code at all. Is this truly representative of the data that we would be loading into the warehouse? Additionally, the "top brand" flag attached to each record seems to be inconsistently applied, with a majority of the records not having it at all, and fewer than 3% of the entries being marked as top brands. How are brands marked as 'top brands' and can we investigate whether our criteria for doing so are reasonable?


2. The `receipts` data:


The receipts dataset was very informative regarding purchasing behavior of consumers. However, there were no receipt statuses marked as `Accepted` - is this expected? Additionally, over two-thirds of the dataset had receipts with 1 or 0 items - is this representative of typical receipts that are submitted to Fetch?


3. The `users` data:


The users data contained information about our users, but is heavily skewed towards users that reside in Wisconsin. Is it possible to provide a larger dataset containing more users from other states? Or is this representative of the type of data that we can expect? Also, many of the users appear to be fetch employees - is there any concern that this may skew the data in some way? There are some data quality issues here as well. 10% of users do not have a signup source, and 11% don't have a state. Is it possible to investigate how this can be the case, and ensure these fields get populated during data extraction?


4. The process for loading new data into the warehouse:


We are curious what the stakeholders envisioned for loading the data into the data warehouse. Would data ideally be loaded on a periodic basis (i.e. a once-per-day job), or would they want data to be available immediately based on consumer-driven events? Additionally, is there an estimate for how many data sources (apps, web backends, cloud environments, etc.) would need to be connected to the data warehouse in order to load the data effectively?


Thank you for your time!

Andrew Einspanier