SELECT customer.full_name, count('order'.customer_id) FROM 'order'
INNER JOIN customer on customer.customer_id = 'order'.customer_id
GROUP BY customer.full_name
ORDER BY count('order'.customer_id)
LIMIT 20;