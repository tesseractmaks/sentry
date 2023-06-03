SELECT customer.full_name, manager.full_name, 'order'.order_no FROM 'order'
INNER JOIN customer on customer.customer_id = 'order'.customer_id
INNER JOIN manager on manager.manager_id = 'order'.manager_id
WHERE manager.city != customer.city
GROUP BY customer.full_name
LIMIT 20;