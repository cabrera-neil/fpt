CREATE TABLE Customers (
    customer_id SERIAL PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL
);

CREATE TABLE Products (
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR(255) NOT NULL,
    unit_price DECIMAL(10, 2) NOT NULL,
    category VARCHAR(255) NOT NULL
);

CREATE TABLE Orders (
    order_id SERIAL PRIMARY KEY,
    order_date DATE NOT NULL,
    customer_id INTEGER REFERENCES Customers(customer_id),
    total_amount DECIMAL(10, 2) NOT NULL
);

SELECT first_name, last_name, email
FROM Customers;

SELECT product_name, unit_price
FROM Products
WHERE unit_price > 50
ORDER BY unit_price DESC;

SELECT o.order_date, c.first_name, o.total_amount
FROM Orders o
JOIN Customers c ON o.customer_id = c.customer_id;

UPDATE Products
SET unit_price = unit_price * 1.10
WHERE category = 'Electronics';
