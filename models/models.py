from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date, Text
from sqlalchemy.orm import relationship
from database.base import Base

class Customer(Base):
    __tablename__ = "customers"
    
    customerNumber = Column(Integer, primary_key=True, index=True)
    customerName = Column(String(50), nullable=False)
    contactLastName = Column(String(50), nullable=False)
    contactFirstName = Column(String(50), nullable=False)
    phone = Column(String(50), nullable=False)
    addressLine1 = Column(String(50), nullable=False)
    addressLine2 = Column(String(50))
    city = Column(String(50), nullable=False)
    state = Column(String(50))
    postalCode = Column(String(15))
    country = Column(String(50), nullable=False)
    salesRepEmployeeNumber = Column(Integer, ForeignKey("employees.employeeNumber", ondelete="SET NULL"))
    creditLimit = Column(Float)

    orders = relationship("Order", back_populates="customer", passive_deletes=True)
    employee = relationship("Employee", back_populates="customers")

class Employee(Base):
    __tablename__ = "employees"
    
    employeeNumber = Column(Integer, primary_key=True, index=True)
    lastName = Column(String(50), nullable=False)
    firstName = Column(String(50), nullable=False)
    extension = Column(String(10), nullable=False)
    email = Column(String(100), nullable=False)
    officeCode = Column(String(10), ForeignKey("offices.officeCode", ondelete="CASCADE"), nullable=False)
    reportsTo = Column(Integer, ForeignKey("employees.employeeNumber", ondelete="SET NULL"))
    jobTitle = Column(String(50), nullable=False)
    
    customers = relationship("Customer", back_populates="employee", passive_deletes=True)
    office = relationship("Office", back_populates="employees")
    subordinates = relationship("Employee", 
        foreign_keys=[reportsTo],
        backref="manager",
        remote_side=[employeeNumber],
        passive_deletes=True
    )

class Office(Base):
    __tablename__ = "offices"
    
    officeCode = Column(String(10), primary_key=True, index=True)
    city = Column(String(50), nullable=False)
    phone = Column(String(50), nullable=False)
    addressLine1 = Column(String(50), nullable=False)
    addressLine2 = Column(String(50))
    state = Column(String(50))
    country = Column(String(50), nullable=False)
    postalCode = Column(String(15), nullable=False)
    territory = Column(String(10), nullable=False)
    
    employees = relationship("Employee", back_populates="office", passive_deletes=True)

class Order(Base):
    __tablename__ = "orders"
    
    orderNumber = Column(Integer, primary_key=True, index=True)
    orderDate = Column(Date, nullable=False)
    requiredDate = Column(Date, nullable=False)
    shippedDate = Column(Date)
    status = Column(String(15), nullable=False)
    comments = Column(Text)
    customerNumber = Column(Integer, ForeignKey("customers.customerNumber", ondelete="CASCADE"), nullable=False)
    
    customer = relationship("Customer", back_populates="orders", passive_deletes=True)
    orderDetails = relationship("OrderDetail", back_populates="order", passive_deletes=True)

class OrderDetail(Base):
    __tablename__ = "orderdetails"
    
    orderNumber = Column(Integer, ForeignKey("orders.orderNumber", ondelete="CASCADE"), primary_key=True)
    productCode = Column(String(15), ForeignKey("products.productCode", ondelete="CASCADE"), primary_key=True)
    quantityOrdered = Column(Integer, nullable=False)
    priceEach = Column(Float, nullable=False)
    orderLineNumber = Column(Integer, nullable=False)
    
    order = relationship("Order", back_populates="orderDetails", passive_deletes=True)
    product = relationship("Product", back_populates="orderDetails", passive_deletes=True)

class Product(Base):
    __tablename__ = "products"
    
    productCode = Column(String(15), primary_key=True, index=True)
    productName = Column(String(70), nullable=False)
    productLine = Column(String(50), ForeignKey("productlines.productLine", ondelete="CASCADE"), nullable=False)
    productScale = Column(String(10), nullable=False)
    productVendor = Column(String(50), nullable=False)
    productDescription = Column(Text, nullable=False)
    quantityInStock = Column(Integer, nullable=False)
    buyPrice = Column(Float, nullable=False)
    MSRP = Column(Float, nullable=False)
    
    productLineInfo = relationship("ProductLine", back_populates="products", passive_deletes=True)
    orderDetails = relationship("OrderDetail", back_populates="product", passive_deletes=True)

class ProductLine(Base):
    __tablename__ = "productlines"
    
    productLine = Column(String(50), primary_key=True, index=True)
    textDescription = Column(String(4000))
    htmlDescription = Column(Text)
    image = Column(String(100))
    
    products = relationship("Product", back_populates="productLineInfo", passive_deletes=True)

class Payment(Base):
    __tablename__ = "payments"
    
    customerNumber = Column(Integer, ForeignKey("customers.customerNumber", ondelete="CASCADE"), primary_key=True)
    checkNumber = Column(String(50), primary_key=True)
    paymentDate = Column(Date, nullable=False)
    amount = Column(Float, nullable=False)
