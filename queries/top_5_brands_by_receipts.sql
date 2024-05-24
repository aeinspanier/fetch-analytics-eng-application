-- Displays total spent by customers grouped by brand, limited 
SELECT
    SUM(rewards_items.item_price) as "total_spent_by_consumers",
    brands.brand_code as "brand"
FROM
    receipts
    JOIN rewards_items ON receipts.receipt_id = rewards_items.receipt_id
    JOIN brands ON brands.brand_id = rewards_items.brand_id
WHERE
    -- Note: Change the dates below as needed
    receipts.date_scanned BETWEEN "04/01/2024" AND "04/30/2024"
GROUP BY
    brands.brand_code
ORDER BY
    SUM(rewards_items.item_price) DESC
LIMIT
    5