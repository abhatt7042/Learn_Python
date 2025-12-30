PRAGMA foreign_keys=ON;


PRAGMA foreign_keys;

-- create TABLE Customer(Id INTEGER PRIMARY KEY AUTOINCREMENT,
-- FirstName varchar(50),
-- LastName varchar(50),
-- Age INT,
-- City varchar(20));

-- INSERT into Customer (FirstName,LastName,Age,City) VALUES('Prachi','Rao',32,'Newyork');


UPDATE customer set City='NewJersey' where LastName='Bhatt';
-- ALTER TABLE customers add City varchar(50);

-- drop table Orders;

-- create TABLE Product(Id INTEGER PRIMARY KEY AUTOINCREMENT,
-- ProductName varchar(50));
-- alter table Product add Price float;
-- INSERT into Product (ProductName,Price) VALUES('Bat','50.25');
-- Update Product set ProductName='Ball' where Price=50.25;


-- create TABLE OrderBook (
-- OrderID INTEGER PRIMARY KEY AUTOINCREMENT, 
-- OrderDate Datetime, 
-- CustomerID int,
-- ProductId int,
-- FOREIGN KEY(CustomerID) REFERENCES Customer(Id),
-- FOREIGN KEY(ProductID) REFERENCES Product(Id)

-- );

select * from Customer;
select * from Product;
select * from NewOrders;

select P.Price,C.* from NewOrders N
inner join Product P on N.ProductId=P.Id
inner join Customer C on N.CustomerID=C.Id;

select SUM(P.Price),AVG(P.Price),C.* from NewOrders N
inner join Product P on N.ProductId=P.Id
inner join Customer C on N.CustomerID=C.Id
group by c.LastName;






