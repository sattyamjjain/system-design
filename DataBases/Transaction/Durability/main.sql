BEGIN TRANSACTION;
UPDATE customers SET balance = balance - 100 WHERE customer_id = 123;
COMMIT TRANSACTION;