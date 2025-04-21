
CREATE DATABASE  IF NOT EXISTS classicmodels;

/* Switch to the classicmodels database */
USE classicmodels;

/* Drop existing tables  */
DROP TABLE IF EXISTS productlines;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS offices;
DROP TABLE IF EXISTS employees;
DROP TABLE IF EXISTS customers; 
DROP TABLE IF EXISTS payments;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS orderdetails;

-- Create tables first (same as before)

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

-- Insert data with Indonesian names and 2025 dates

-- Insert offices
INSERT INTO offices VALUES ('1', 'Jakarta', '+62 21 5559 8765', 'Jalan Sudirman 123', 'Lantai 12', 'DKI Jakarta', 'Indonesia', '10220', 'APAC');
INSERT INTO offices VALUES ('2', 'Surabaya', '+62 31 5559 1234', 'Jalan Pemuda 45', 'Tower A Lt. 5', 'Jawa Timur', 'Indonesia', '60271', 'APAC');
INSERT INTO offices VALUES ('3', 'Bandung', '+62 22 5559 4321', 'Jalan Asia Afrika 88', 'Gedung Merdeka', 'Jawa Barat', 'Indonesia', '40112', 'APAC');
INSERT INTO offices VALUES ('4', 'Medan', '+62 61 5559 6543', 'Jalan Diponegoro 15', NULL, 'Sumatera Utara', 'Indonesia', '20152', 'APAC');
INSERT INTO offices VALUES ('5', 'Makassar', '+62 411 5559 8901', 'Jalan Penghibur 10', NULL, 'Sulawesi Selatan', 'Indonesia', '90111', 'APAC');
INSERT INTO offices VALUES ('6', 'Denpasar', '+62 361 5559 2468', 'Jalan Legian 202', 'Lantai 3', 'Bali', 'Indonesia', '80361', 'APAC');
INSERT INTO offices VALUES ('7', 'Yogyakarta', '+62 274 5559 1357', 'Jalan Malioboro 77', NULL, 'DI Yogyakarta', 'Indonesia', '55271', 'APAC');

-- Insert employees
INSERT INTO employees VALUES (1002, 'Wijaya', 'Budi', 'x5800', 'bwijaya@classicmodelcars.com', '1', NULL, 'Presiden Direktur');
INSERT INTO employees VALUES (1056, 'Surya', 'Dewi', 'x4611', 'dsurya@classicmodelcars.com', '1', 1002, 'VP Penjualan');
INSERT INTO employees VALUES (1076, 'Sanjaya', 'Agus', 'x9273', 'asanjaya@classicmodelcars.com', '1', 1002, 'VP Pemasaran');
INSERT INTO employees VALUES (1088, 'Gunawan', 'Bambang', 'x4871', 'bgunawan@classicmodelcars.com', '6', 1056, 'Manajer Penjualan');
INSERT INTO employees VALUES (1102, 'Kusuma', 'Siti', 'x5408', 'skusuma@classicmodelcars.com', '4', 1056, 'Manajer Penjualan');
INSERT INTO employees VALUES (1143, 'Hidayat', 'Rudi', 'x5428', 'rhidayat@classicmodelcars.com', '1', 1056, 'Manajer Penjualan');

-- Insert customers
INSERT INTO customers VALUES 
(103, 'Toko Maju Jaya', 'Santoso', 'Joko', '021-5551234', 'Jalan Kebon Jeruk 15', NULL, 'Jakarta', 'DKI Jakarta', '11530', 'Indonesia', 1002, 21000.00),
(112, 'PT Sukses Makmur', 'Wati', 'Sri', '022-5557890', 'Jalan Pasteur 123', NULL, 'Bandung', 'Jawa Barat', '40161', 'Indonesia', 1056, 71800.00),
(114, 'CV Mitra Abadi', 'Saputra', 'Andi', '031-5553456', 'Jalan Basuki Rahmat 76', 'Lantai 3', 'Surabaya', 'Jawa Timur', '60271', 'Indonesia', 1076, 117300.00),
(119, 'UD Sejahtera', 'Nugraha', 'Hendra', '024-5554567', 'Jalan Pemuda 45', NULL, 'Semarang', 'Jawa Tengah', '50139', 'Indonesia', 1088, 118200.00),
(121, 'PT Indah Persada', 'Wulandari', 'Maya', '0274-5556789', 'Jalan Kaliurang KM 5', NULL, 'Yogyakarta', 'DI Yogyakarta', '55281', 'Indonesia', 1102, 81700.00),
(124, 'Toko Sentosa', 'Wijaya', 'Anton', '061-5558901', 'Jalan S. Parman 88', NULL, 'Medan', 'Sumatera Utara', '20112', 'Indonesia', 1143, 210500.00),
(128, 'PT Bintang Terang', 'Utami', 'Lina', '0361-5559012', 'Jalan Sunset Road 55', NULL, 'Denpasar', 'Bali', '80361', 'Indonesia', 1056, 69500.00),
(141, 'CV Prima Jaya', 'Hakim', 'Fajar', '0411-5550123', 'Jalan Ahmad Yani 22', NULL, 'Makassar', 'Sulawesi Selatan', '90111', 'Indonesia', 1102, 45000.00),
(181, 'UD Berkah Abadi', 'Permana', 'Dian', '0751-5551234', 'Jalan Sudirman 78', NULL, 'Padang', 'Sumatera Barat', '25129', 'Indonesia', 1088, 58900.00),
(363, 'Toko Sumber Makmur', 'Putra', 'Eko', '0561-5554321', 'Jalan Ahmad Dahlan 32', NULL, 'Pontianak', 'Kalimantan Barat', '78117', 'Indonesia', 1143, 94500.00);

-- Insert productlines
INSERT INTO productlines VALUES ('Mobil Klasik', 'Koleksi miniatur mobil klasik dengan kualitas premium dan detail yang sangat akurat. Setiap model dilengkapi dengan sertifikat keaslian dan dibuat dengan presisi tinggi.', NULL, NULL);
INSERT INTO productlines VALUES ('Sepeda Motor', 'Replika sepeda motor legendaris dari berbagai era, mencakup model klasik dan kontemporer. Dilengkapi dengan fitur detail seperti roda berputar dan sistem suspensi.', NULL, NULL);
INSERT INTO productlines VALUES ('Pesawat', 'Miniatur pesawat terbang dan helikopter yang cocok untuk koleksi maupun dekorasi. Detail akurat termasuk logo resmi dan propeler berputar.', NULL, NULL);
INSERT INTO productlines VALUES ('Kapal', 'Model kapal buatan tangan dengan detail mengagumkan. Merupakan hadiah istimewa untuk eksekutif, klien, dan keluarga.', NULL, NULL);
INSERT INTO productlines VALUES ('Kereta Api', 'Model kereta api untuk penggemar dari berbagai usia. Koleksi lengkap termasuk gerbong, lokomotif, dan aksesori rel.', NULL, NULL);
INSERT INTO productlines VALUES ('Truk dan Bus', 'Replika realistis dari truk dan bus dari era 1920-an hingga modern. Mencakup berbagai skala dan edisi terbatas.', NULL, NULL);
INSERT INTO productlines VALUES ('Mobil Antik', 'Model mobil antik dari awal 1900-an hingga 1940-an. Terbuat dari berbagai material berkualitas dan tersedia dalam berbagai skala.', NULL, NULL);

-- Insert products
INSERT INTO products VALUES ('S10_1678', 'Harley Davidson Ultimate Chopper 1969', 'Sepeda Motor', '1:10', 'Diecast Indonesia', 'Replika dengan kickstand yang berfungsi, suspensi depan, tuas pemindah gigi, tuas rem kaki, rantai penggerak, roda, dan kemudi.', 7933, 48.81, 95.70);
INSERT INTO products VALUES ('S10_1949', 'Alpine Renault 1300 1952', 'Mobil Klasik', '1:10', 'Kreasi Logam Klasik', 'Roda depan dapat berputar, fungsi kemudi, detail interior, mesin detail, kap terbuka, bagasi terbuka, pintu terbuka, dan sasis detail.', 7305, 98.58, 214.30);
INSERT INTO products VALUES ('S10_2016', 'Moto Guzzi 1100i 1996', 'Sepeda Motor', '1:10', 'Miniatur Jalur 66', 'Logo dan lambang Moto Guzzi resmi, tas sadel, mesin detail, kemudi berfungsi, suspensi berfungsi, dua kursi kulit, rak bagasi.', 6625, 68.99, 118.94);
INSERT INTO products VALUES ('S10_4698', 'Harley-Davidson Eagle Drag Bike 2003', 'Sepeda Motor', '1:10', 'Diecast Bintang Merah', 'Model fitur, logo Harley Davidson resmi, bilah wheelie belakang yang dapat dilepas, logam die-cast berat dengan bagian resin.', 5582, 91.02, 193.66);
INSERT INTO products VALUES ('S10_4757', 'Alfa Romeo GTA 1972', 'Mobil Klasik', '1:10', 'Seni Klasik Motor City', 'Fitur meliputi: Roda depan berputar; fungsi kemudi; interior detail; mesin detail; kap terbuka; bagasi terbuka; pintu terbuka; dan sasis detail.', 3252, 85.68, 136.00);

-- Insert orders with 2025 dates
INSERT INTO orders VALUES (10100, '2025-01-06', '2025-01-13', '2025-01-10', 'Dikirim', NULL, 363);
INSERT INTO orders VALUES (10101, '2025-01-09', '2025-01-18', '2025-01-11', 'Dikirim', 'Periksa ketersediaan.', 128);
INSERT INTO orders VALUES (10102, '2025-01-10', '2025-01-18', '2025-01-14', 'Dikirim', NULL, 181);
INSERT INTO orders VALUES (10103, '2025-01-29', '2025-02-07', '2025-02-02', 'Dikirim', NULL, 121);
INSERT INTO orders VALUES (10104, '2025-01-31', '2025-02-09', '2025-02-01', 'Dikirim', NULL, 141);

-- Insert orderdetails
INSERT INTO orderdetails VALUES (10100, 'S10_1678', 30, 98.00, 2);
INSERT INTO orderdetails VALUES (10100, 'S10_1949', 50, 214.30, 1);
INSERT INTO orderdetails VALUES (10100, 'S10_2016', 22, 118.94, 3);
INSERT INTO orderdetails VALUES (10101, 'S10_1678', 35, 95.70, 2);
INSERT INTO orderdetails VALUES (10102, 'S10_4698', 18, 193.66, 1);

-- Insert payments with 2025 dates
INSERT INTO payments VALUES (103, 'HQ336336', '2025-01-19', 6066.78);
INSERT INTO payments VALUES (103, 'JM555205', '2025-02-05', 14571.44);
INSERT INTO payments VALUES (103, 'OM314933', '2025-03-18', 1676.14);
INSERT INTO payments VALUES (112, 'BO864823', '2025-02-17', 14191.12);
INSERT INTO payments VALUES (112, 'HQ55022', '2025-03-06', 32641.98);
