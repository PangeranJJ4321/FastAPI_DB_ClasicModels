-- Create tables


-- Create offices table
CREATE TABLE offices (
    officeCode VARCHAR(10) PRIMARY KEY,
    city VARCHAR(50) NOT NULL,
    phone VARCHAR(50) NOT NULL,
    addressLine1 VARCHAR(50) NOT NULL,
    addressLine2 VARCHAR(50),
    state VARCHAR(50),
    country VARCHAR(50) NOT NULL,
    postalCode VARCHAR(15) NOT NULL,
    territory VARCHAR(10) NOT NULL
);

-- Create employees table
CREATE TABLE employees (
    employeeNumber INTEGER PRIMARY KEY,
    lastName VARCHAR(50) NOT NULL,
    firstName VARCHAR(50) NOT NULL,
    extension VARCHAR(10) NOT NULL,
    email VARCHAR(100) NOT NULL,
    officeCode VARCHAR(10) NOT NULL,
    reportsTo INTEGER,
    jobTitle VARCHAR(50) NOT NULL,
    FOREIGN KEY (officeCode) REFERENCES offices (officeCode),
    FOREIGN KEY (reportsTo) REFERENCES employees (employeeNumber)
);

-- Create customers table
CREATE TABLE customers (
    customerNumber INTEGER PRIMARY KEY,
    customerName VARCHAR(50) NOT NULL,
    contactLastName VARCHAR(50) NOT NULL,
    contactFirstName VARCHAR(50) NOT NULL,
    phone VARCHAR(50) NOT NULL,
    addressLine1 VARCHAR(50) NOT NULL,
    addressLine2 VARCHAR(50),
    city VARCHAR(50) NOT NULL,
    state VARCHAR(50),
    postalCode VARCHAR(15),
    country VARCHAR(50) NOT NULL,
    salesRepEmployeeNumber INTEGER,
    creditLimit FLOAT,
    FOREIGN KEY (salesRepEmployeeNumber) REFERENCES employees (employeeNumber)
);

-- Create productlines table
CREATE TABLE productlines (
    productLine VARCHAR(50) PRIMARY KEY,
    textDescription VARCHAR(4000),
    htmlDescription TEXT,
    image VARCHAR(100)
);

-- Create products table
CREATE TABLE products (
    productCode VARCHAR(15) PRIMARY KEY,
    productName VARCHAR(70) NOT NULL,
    productLine VARCHAR(50) NOT NULL,
    productScale VARCHAR(10) NOT NULL,
    productVendor VARCHAR(50) NOT NULL,
    productDescription TEXT NOT NULL,
    quantityInStock INTEGER NOT NULL,
    buyPrice FLOAT NOT NULL,
    MSRP FLOAT NOT NULL,
    FOREIGN KEY (productLine) REFERENCES productlines (productLine)
);

-- Create orders table
CREATE TABLE orders (
    orderNumber INTEGER PRIMARY KEY,
    orderDate DATE NOT NULL,
    requiredDate DATE NOT NULL,
    shippedDate DATE,
    status VARCHAR(15) NOT NULL,
    comments TEXT,
    customerNumber INTEGER NOT NULL,
    FOREIGN KEY (customerNumber) REFERENCES customers (customerNumber)
);

-- Create orderdetails table
CREATE TABLE orderdetails (
    orderNumber INTEGER,
    productCode VARCHAR(15),
    quantityOrdered INTEGER NOT NULL,
    priceEach FLOAT NOT NULL,
    orderLineNumber INTEGER NOT NULL,
    PRIMARY KEY (orderNumber, productCode),
    FOREIGN KEY (orderNumber) REFERENCES orders (orderNumber),
    FOREIGN KEY (productCode) REFERENCES products (productCode)
);

-- Create payments table
CREATE TABLE payments (
    customerNumber INTEGER,
    checkNumber VARCHAR(50),
    paymentDate DATE NOT NULL,
    amount FLOAT NOT NULL,
    PRIMARY KEY (customerNumber, checkNumber),
    FOREIGN KEY (customerNumber) REFERENCES customers (customerNumber)
);

-- Insert sample data

-- Insert offices
INSERT INTO offices VALUES ('1', 'San Francisco', '+1 650 219 4782', '100 Market Street', 'Suite 300', 'CA', 'USA', '94080', 'NA');
INSERT INTO offices VALUES ('2', 'Boston', '+1 215 837 0825', '1550 Court Place', 'Suite 102', 'MA', 'USA', '02107', 'NA');
INSERT INTO offices VALUES ('3', 'NYC', '+1 212 555 3000', '523 East 53rd Street', 'apt. 5A', 'NY', 'USA', '10022', 'NA');
INSERT INTO offices VALUES ('4', 'Paris', '+33 14 723 4404', '43 Rue Jouffroy D''abbans', NULL, NULL, 'France', '75017', 'EMEA');
INSERT INTO offices VALUES ('5', 'Tokyo', '+81 33 224 5000', '4-1 Kioicho', NULL, 'Chiyoda-Ku', 'Japan', '102-8578', 'APAC');
INSERT INTO offices VALUES ('6', 'Sydney', '+61 2 9264 2451', '5-11 Wentworth Avenue', 'Floor #2', NULL, 'Australia', 'NSW 2010', 'APAC');
INSERT INTO offices VALUES ('7', 'London', '+44 20 7877 2041', '25 Old Broad Street', 'Level 7', NULL, 'UK', 'EC2N 1HN', 'EMEA');

-- Insert employees
INSERT INTO employees VALUES (1002, 'Murphy', 'Diane', 'x5800', 'dmurphy@classicmodelcars.com', '1', NULL, 'President');
INSERT INTO employees VALUES (1056, 'Patterson', 'Mary', 'x4611', 'mpatterso@classicmodelcars.com', '1', 1002, 'VP Sales');
INSERT INTO employees VALUES (1076, 'Firrelli', 'Jeff', 'x9273', 'jfirrelli@classicmodelcars.com', '1', 1002, 'VP Marketing');
INSERT INTO employees VALUES (1088, 'Patterson', 'William', 'x4871', 'wpatterson@classicmodelcars.com', '6', 1056, 'Sales Manager');
INSERT INTO employees VALUES (1102, 'Bondur', 'Gerard', 'x5408', 'gbondur@classicmodelcars.com', '4', 1056, 'Sale Manager');
INSERT INTO employees VALUES (1143, 'Bow', 'Anthony', 'x5428', 'abow@classicmodelcars.com', '1', 1056, 'Sales Manager');

-- Insert customers
INSERT INTO customers VALUES (103, 'Atelier graphique', 'Schmitt', 'Carine', '40.32.2555', '54, rue Royale', NULL, 'Nantes', NULL, '44000', 'France', 1370, 21000.00);
INSERT INTO customers VALUES (112, 'Signal Gift Stores', 'King', 'Jean', '7025551838', '8489 Strong St.', NULL, 'Las Vegas', 'NV', '83030', 'USA', 1166, 71800.00);
INSERT INTO customers VALUES (114, 'Australian Collectors, Co.', 'Ferguson', 'Peter', '03 9520 4555', '636 St Kilda Road', 'Level 3', 'Melbourne', 'Victoria', '3004', 'Australia', 1611, 117300.00);
INSERT INTO customers VALUES (119, 'La Rochelle Gifts', 'Labrune', 'Janine', '40.67.8555', '67, rue des Cinquante Otages', NULL, 'Nantes', NULL, '44000', 'France', 1370, 118200.00);
INSERT INTO customers VALUES (121, 'Baane Mini Imports', 'Bergulfsen', 'Jonas', '07-98 9555', 'Erling Skakkes gate 78', NULL, 'Stavern', NULL, '4110', 'Norway', 1504, 81700.00);

-- Insert productlines
INSERT INTO productlines VALUES ('Classic Cars', 'Attention car enthusiasts: Make your wildest car ownership dreams come true. Whether you are looking for classic muscle cars, dream sports cars or movie-inspired miniatures, you will find great choices in this category. These replicas feature superb attention to detail and craftsmanship and offer features such as working steering system, opening forward compartment, opening rear trunk with removable spare wheel, 4-wheel independent spring suspension, and so on. The models range in size from 1:10 to 1:24 scale and include numerous limited edition and several out-of-production vehicles. All models include a certificate of authenticity from their manufacturers and come fully assembled and ready for display in the home or office.', NULL, NULL);
INSERT INTO productlines VALUES ('Motorcycles', 'Our motorcycles are state of the art replicas of classic as well as contemporary motorcycle legends such as Harley Davidson, Ducati and Vespa. Models contain stunning details such as official logos, rotating wheels, working kickstand, front suspension, gear-shift lever, footbrake lever, and drive chain. Materials used include diecast and plastic. The models range in size from 1:10 to 1:50 scale and include numerous limited edition and several out-of-production vehicles. All models come fully assembled and ready for display in the home or office. Most include a certificate of authenticity.', NULL, NULL);
INSERT INTO productlines VALUES ('Planes', 'Unique, diecast airplane and helicopter replicas suitable for collections, as well as home, office or classroom decorations. Models contain stunning details such as official logos and insignias, rotating propellers and wheels, retractable wheels, and so on. Most come fully assembled and with a certificate of authenticity from their manufacturers.', NULL, NULL);
INSERT INTO productlines VALUES ('Ships', 'The perfect holiday or anniversary gift for executives, clients, friends, and family. These handcrafted model ships are unique, stunning works of art that will be treasured for generations! They come fully assembled and ready for display in the home or office. We guarantee the highest quality, and best value.', NULL, NULL);
INSERT INTO productlines VALUES ('Trains', 'Model trains are a rewarding hobby for enthusiasts of all ages. Whether you\'re looking for collectible wooden trains, electric train sets or accessories, Trains has got you covered. The wide variety of railway sets and accessories will satisfy any collector\'s need for the ultimate train experience.', NULL, NULL);
INSERT INTO productlines VALUES ('Trucks and Buses', 'The Truck and Bus models are realistic replicas of buses and specialized trucks produced from the early 1920s to present. The models range in size from 1:12 to 1:50 scale and include numerous limited edition and several out-of-production vehicles. Materials used include tin, diecast and plastic. All models include a certificate of authenticity from their manufacturers and are a perfect ornament for the home and office.', NULL, NULL);
INSERT INTO productlines VALUES ('Vintage Cars', 'Our Vintage Car models realistically portray automobiles produced from the early 1900s through the 1940s. Materials used include Bakelite, diecast, plastic and wood. Most of the replicas are in the 1:18 and 1:24 scale sizes, which provide the optimum in detail and accuracy. Prices range from $30.00 up to $180.00 for some special limited edition replicas. All models include a certificate of authenticity from their manufacturers and come fully assembled and ready for display in the home or office.', NULL, NULL);

-- Insert products (sample)
INSERT INTO products VALUES ('S10_1678', '1969 Harley Davidson Ultimate Chopper', 'Motorcycles', '1:10', 'Min Lin Diecast', 'This replica features working kickstand, front suspension, gear-shift lever, footbrake lever, drive chain, wheels and steering. All parts are particularly delicate due to their precise scale and require special care and attention.', 7933, 48.81, 95.70);
INSERT INTO products VALUES ('S10_1949', '1952 Alpine Renault 1300', 'Classic Cars', '1:10', 'Classic Metal Creations', 'Turnable front wheels; steering function; detailed interior; detailed engine; opening hood; opening trunk; opening doors; and detailed chassis.', 7305, 98.58, 214.30);
INSERT INTO products VALUES ('S10_2016', '1996 Moto Guzzi 1100i', 'Motorcycles', '1:10', 'Highway 66 Mini Classics', 'Official Moto Guzzi logos and insignias, saddle bags located on side of motorcycle, detailed engine, working steering, working suspension, two leather seats, luggage rack, dual exhaust pipes, small saddle bag located on handle bars, two-tone paint with chrome accents, superior die-cast detail , rotating wheels , working kick stand, diecast metal with plastic parts and baked enamel finish.', 6625, 68.99, 118.94);
INSERT INTO products VALUES ('S10_4698', '2003 Harley-Davidson Eagle Drag Bike', 'Motorcycles', '1:10', 'Red Start Diecast', 'Model features, official Harley Davidson logos and insignias, detachable rear wheelie bar, heavy diecast metal with resin parts, authentic multi-color tampo-printed graphics, separate engine drive belts, free-turning front fork, rotating tires and rear racing slick, certificate of authenticity, detailed engine, display stand, precision diecast replica, baked enamel finish, 1:10 scale model, removable fender, seat and tank cover piece for displaying the superior detail of the v-twin engine', 5582, 91.02, 193.66);
INSERT INTO products VALUES ('S10_4757', '1972 Alfa Romeo GTA', 'Classic Cars', '1:10', 'Motor City Art Classics', 'Features include: Turnable front wheels; steering function; detailed interior; detailed engine; opening hood; opening trunk; opening doors; and detailed chassis.', 3252, 85.68, 136.00);

-- Insert orders
INSERT INTO orders VALUES (10100, '2003-01-06', '2003-01-13', '2003-01-10', 'Shipped', NULL, 363);
INSERT INTO orders VALUES (10101, '2003-01-09', '2003-01-18', '2003-01-11', 'Shipped', 'Check on availability.', 128);
INSERT INTO orders VALUES (10102, '2003-01-10', '2003-01-18', '2003-01-14', 'Shipped', NULL, 181);
INSERT INTO orders VALUES (10103, '2003-01-29', '2003-02-07', '2003-02-02', 'Shipped', NULL, 121);
INSERT INTO orders VALUES (10104, '2003-01-31', '2003-02-09', '2003-02-01', 'Shipped', NULL, 141);

-- Insert orderdetails
INSERT INTO orderdetails VALUES (10100, 'S10_1678', 30, 98.00, 2);
INSERT INTO orderdetails VALUES (10100, 'S10_1949', 50, 214.30, 1);
INSERT INTO orderdetails VALUES (10100, 'S10_2016', 22, 118.94, 3);
INSERT INTO orderdetails VALUES (10101, 'S10_1678', 35, 95.70, 2);
INSERT INTO orderdetails VALUES (10102, 'S10_4698', 18, 193.66, 1);

-- Insert payments
INSERT INTO payments VALUES (103, 'HQ336336', '2004-10-19', 6066.78);
INSERT INTO payments VALUES (103, 'JM555205', '2003-06-05', 14571.44);
INSERT INTO payments VALUES (103, 'OM314933', '2004-12-18', 1676.14);
INSERT INTO payments VALUES (112, 'BO864823', '2004-12-17', 14191.12);
INSERT INTO payments VALUES (112, 'HQ55022', '2003-06-06', 32641.98);