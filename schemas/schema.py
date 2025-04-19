from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any
from datetime import date

# Customer Schemas
class CustomerBase(BaseModel):
    customerName: str
    contactLastName: str
    contactFirstName: str
    phone: str
    addressLine1: str
    addressLine2: Optional[str] = None
    city: str
    state: Optional[str] = None
    postalCode: Optional[str] = None
    country: str
    salesRepEmployeeNumber: Optional[int] = None
    creditLimit: Optional[float] = None
    
class CustomerCreate(CustomerBase):
    pass

class CustomerUpdate(CustomerBase):
    customerName: Optional[str] = None
    contactLastName: Optional[str] = None
    contactFirstName: Optional[str] = None
    phone: Optional[str] = None
    addressLine1: Optional[str] = None
    city: Optional[str] = None
    country: Optional[str] = None

class CustomerResponse(CustomerBase):
    customerNumber: int
    
    class Config:
        orm_mode = True

# Employee Schemas
class EmployeeBase(BaseModel):
    lastName: str
    firstName: str
    extension: str
    email: str
    officeCode: str
    reportsTo: Optional[int] = None
    jobTitle: str

class EmployeeCreate(EmployeeBase):
    pass

class EmployeeUpdate(EmployeeBase):
    lastName: Optional[str] = None
    firstName: Optional[str] = None
    extension: Optional[str] = None
    email: Optional[str] = None
    officeCode: Optional[str] = None
    reportsTo: Optional[int] = None
    jobTitle: Optional[str] = None

class EmployeeResponse(EmployeeBase):
    employeeNumber: int
    
    class Config:
        orm_mode = True

# Office Schemas
class OfficeBase(BaseModel):
    city: str
    phone: str
    addressLine1: str
    addressLine2: Optional[str] = None
    state: Optional[str] = None
    country: str
    postalCode: str
    territory: str

class OfficeCreate(OfficeBase):
    officeCode: str

class OfficeUpdate(OfficeBase):
    city: Optional[str] = None
    phone: Optional[str] = None
    addressLine1: Optional[str] = None
    country: Optional[str] = None
    postalCode: Optional[str] = None
    territory: Optional[str] = None

class OfficeResponse(OfficeBase):
    officeCode: str
    
    class Config:
        orm_mode = True

# Order Schemas
class OrderBase(BaseModel):
    orderDate: date
    requiredDate: date
    shippedDate: Optional[date] = None
    status: str
    comments: Optional[str] = None
    customerNumber: int

class OrderCreate(OrderBase):
    pass

class OrderUpdate(OrderBase):
    orderDate: Optional[date] = None
    requiredDate: Optional[date] = None
    status: Optional[str] = None
    customerNumber: Optional[int] = None

class OrderResponse(OrderBase):
    orderNumber: int
    
    class Config:
        orm_mode = True

# OrderDetail Schemas
class OrderDetailBase(BaseModel):
    orderNumber: int
    productCode: str
    quantityOrdered: int
    priceEach: float
    orderLineNumber: int

class OrderDetailCreate(OrderDetailBase):
    pass

class OrderDetailUpdate(BaseModel):
    quantityOrdered: Optional[int] = None
    priceEach: Optional[float] = None
    orderLineNumber: Optional[int] = None

class OrderDetailResponse(OrderDetailBase):
    class Config:
        orm_mode = True

# Product Schemas
class ProductBase(BaseModel):
    productName: str
    productLine: str
    productScale: str
    productVendor: str
    productDescription: str
    quantityInStock: int
    buyPrice: float
    MSRP: float

class ProductCreate(ProductBase):
    productCode: str

class ProductUpdate(ProductBase):
    productName: Optional[str] = None
    productLine: Optional[str] = None
    productScale: Optional[str] = None
    productVendor: Optional[str] = None
    productDescription: Optional[str] = None
    quantityInStock: Optional[int] = None
    buyPrice: Optional[float] = None
    MSRP: Optional[float] = None

class ProductResponse(ProductBase):
    productCode: str
    
    class Config:
        orm_mode = True

# ProductLine Schemas
class ProductLineBase(BaseModel):
    productLine: str
    textDescription: Optional[str] = None
    htmlDescription: Optional[str] = None
    image: Optional[str] = None

class ProductLineCreate(ProductLineBase):
    pass

class ProductLineUpdate(BaseModel):
    textDescription: Optional[str] = None
    htmlDescription: Optional[str] = None
    image: Optional[str] = None

class ProductLineResponse(ProductLineBase):
    class Config:
        orm_mode = True

# Payment Schemas
class PaymentBase(BaseModel):
    customerNumber: int
    checkNumber: str
    paymentDate: date
    amount: float

class PaymentCreate(PaymentBase):
    pass

class PaymentUpdate(BaseModel):
    paymentDate: Optional[date] = None
    amount: Optional[float] = None

class PaymentResponse(PaymentBase):
    class Config:
        orm_mode = True

# Common response models
class PaginatedResponse(BaseModel):
    items: List[Dict[str, Any]]
    total: int
    page: int
    size: int
    pages: int