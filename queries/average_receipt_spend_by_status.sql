-- Displays average spend by receipt status, limited to accepted and rejected
SELECT
    AVG(receipts.total_spent) as "average_spend",
    receipt_status.description as "receipt_status"
FROM
    receipts
    JOIN receipt_status ON receipts.receipt_status_id = receipt_status.receipt_status_id
WHERE
    receipt_status.description = "Accepted"
    OR receipt_status.description = "Rejected"
GROUP BY
    receipt_status.description