SELECT customer.full_name, 'order'.order_no FROM customer
LEFT JOIN 'order' on customer.customer_id = 'order'.customer_id
WHERE 'order'.customer_id IS NULL
GROUP BY customer.full_name
LIMIT 20;