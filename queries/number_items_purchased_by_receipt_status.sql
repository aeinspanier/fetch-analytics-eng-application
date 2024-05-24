-- Display number of items purchased by receipt status, limited to accepted and rejected
SELECT
    COUNT(receipts.receipt_id) as "number_items_purchased",
    receipt_status.description as "receipt_status"
FROM
    receipts
    JOIN rewards_items ON receipts.receipt_id = rewards_items.receipt_id
    JOIN receipt_status ON receipts.receipt_status_id = receipt_status.receipt_status_id
WHERE
    receipt_status.description = "Accepted"
    OR receipt_status.description = "Rejected"
GROUP BY
    receipts.receipt_id