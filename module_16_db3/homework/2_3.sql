SELECT customer.full_name, manager.full_name, 'order'.purchase_amount, 'order'.date FROM 'order'
INNER JOIN customer on customer.customer_id = 'order'.customer_id
INNER JOIN manager on manager.manager_id = 'order'.manager_id;