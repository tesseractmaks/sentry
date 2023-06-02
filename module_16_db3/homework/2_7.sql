SELECT customer.full_name, 'order'.order_no FROM customer
LEFT JOIN 'order' on customer.customer_id = 'order'.customer_id
WHERE customer.manager_id IS NULL
AND 'order'.order_no IS NOT NULL GROUP BY customer.full_name;