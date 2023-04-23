START TRANSACTION;
INSERT INTO orders (order_id, customer_id, order_total)
VALUES (1234, 5678, 100.00);
UPDATE customers SET balance = balance - 100.00 WHERE customer_id = 5678;
COMMIT;