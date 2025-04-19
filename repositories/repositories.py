from sqlalchemy.orm import Session
from sqlalchemy import func
from models.models import Customer, Employee, Office, Order, OrderDetail, Product, ProductLine, Payment
from typing import List, Dict, Any, Optional, Tuple, Type
from sqlalchemy.ext.declarative import DeclarativeMeta
import math

class BaseRepository:
    def __init__(self, db: Session, model: Type[DeclarativeMeta]):
        self.db = db
        self.model = model
    
    def get_all(self, skip: int = 0, limit: int = 100) -> List[Any]:
        return self.db.query(self.model).offset(skip).limit(limit).all()
        
    def get_paginated(self, page: int = 1, size: int = 10) -> Tuple[List[Any], int, int]:
        total = self.db.query(func.count(self.model.__table__.c.get(list(self.model.__table__.primary_key)[0].name))).scalar()
        pages = math.ceil(total / size)
        
        items = self.db.query(self.model).offset((page - 1) * size).limit(size).all()
        return items, total, pages
        
    def get_by_id(self, id_value) -> Any:
        return self.db.query(self.model).filter(
            getattr(self.model, self._get_primary_key_name()) == id_value
        ).first()
    
    def create(self, data: Dict[str, Any]) -> Any:
        db_item = self.model(**data)
        self.db.add(db_item)
        self.db.commit()
        self.db.refresh(db_item)
        return db_item
    
    def update(self, id_value, data: Dict[str, Any]) -> Optional[Any]:
        db_item = self.get_by_id(id_value)
        if not db_item:
            return None
            
        for key, value in data.items():
            if hasattr(db_item, key) and value is not None:
                setattr(db_item, key, value)
                
        self.db.commit()
        self.db.refresh(db_item)
        return db_item
    
    def delete(self, id_value) -> bool:
        db_item = self.get_by_id(id_value)
        if not db_item:
            return False
            
        self.db.delete(db_item)
        self.db.commit()
        return True
    
    def _get_primary_key_name(self) -> str:
        return list(self.model.__table__.primary_key)[0].name

class CustomerRepository(BaseRepository):
    def __init__(self, db: Session):
        super().__init__(db, Customer)
    
    def get_by_customer_number(self, customer_number: int) -> Customer:
        return self.db.query(Customer).filter(Customer.customerNumber == customer_number).first()
    
    def get_with_orders(self, customer_number: int) -> Customer:
        return self.db.query(Customer).filter(
            Customer.customerNumber == customer_number
        ).first()

class EmployeeRepository(BaseRepository):
    def __init__(self, db: Session):
        super().__init__(db, Employee)
    
    def get_by_employee_number(self, employee_number: int) -> Employee:
        return self.db.query(Employee).filter(Employee.employeeNumber == employee_number).first()
    
    def get_by_office_code(self, office_code: str) -> List[Employee]:
        return self.db.query(Employee).filter(Employee.officeCode == office_code).all()

class OfficeRepository(BaseRepository):
    def __init__(self, db: Session):
        super().__init__(db, Office)
    
    def get_by_office_code(self, office_code: str) -> Office:
        return self.db.query(Office).filter(Office.officeCode == office_code).first()

class OrderRepository(BaseRepository):
    def __init__(self, db: Session):
        super().__init__(db, Order)
    
    def get_by_order_number(self, order_number: int) -> Order:
        return self.db.query(Order).filter(Order.orderNumber == order_number).first()
    
    def get_by_customer(self, customer_number: int) -> List[Order]:
        return self.db.query(Order).filter(Order.customerNumber == customer_number).all()
    
    def get_orders_with_details(self, order_number: int) -> Order:
        return self.db.query(Order).filter(Order.orderNumber == order_number).first()

class OrderDetailRepository(BaseRepository):
    def __init__(self, db: Session):
        super().__init__(db, OrderDetail)
    
    def get_by_composite_key(self, order_number: int, product_code: str) -> OrderDetail:
        return self.db.query(OrderDetail).filter(
            OrderDetail.orderNumber == order_number,
            OrderDetail.productCode == product_code
        ).first()
    
    def get_by_order_number(self, order_number: int) -> List[OrderDetail]:
        return self.db.query(OrderDetail).filter(
            OrderDetail.orderNumber == order_number
        ).all()

class ProductRepository(BaseRepository):
    def __init__(self, db: Session):
        super().__init__(db, Product)
    
    def get_by_product_code(self, product_code: str) -> Product:
        return self.db.query(Product).filter(Product.productCode == product_code).first()
    
    def get_by_product_line(self, product_line: str) -> List[Product]:
        return self.db.query(Product).filter(Product.productLine == product_line).all()

class ProductLineRepository(BaseRepository):
    def __init__(self, db: Session):
        super().__init__(db, ProductLine)
    
    def get_by_product_line(self, product_line: str) -> ProductLine:
        return self.db.query(ProductLine).filter(ProductLine.productLine == product_line).first()

class PaymentRepository(BaseRepository):
    def __init__(self, db: Session):
        super().__init__(db, Payment)
    
    def get_by_composite_key(self, customer_number: int, check_number: str) -> Payment:
        return self.db.query(Payment).filter(
            Payment.customerNumber == customer_number,
            Payment.checkNumber == check_number
        ).first()
    
    def get_by_customer_number(self, customer_number: int) -> List[Payment]:
        return self.db.query(Payment).filter(Payment.customerNumber == customer_number).all()