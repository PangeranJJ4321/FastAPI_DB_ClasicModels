from sqlalchemy.orm import Session
from repositories.repositories import (
    CustomerRepository, EmployeeRepository, OfficeRepository, 
    OrderRepository, OrderDetailRepository, ProductRepository, 
    ProductLineRepository, PaymentRepository
)
from schemas.schema import (
    CustomerCreate, CustomerUpdate, EmployeeCreate, EmployeeUpdate,
    OfficeCreate, OfficeUpdate, OrderCreate, OrderUpdate,
    OrderDetailCreate, OrderDetailUpdate, ProductCreate, ProductUpdate,
    ProductLineCreate, ProductLineUpdate, PaymentCreate, PaymentUpdate
)
from typing import Dict, List, Any, Optional, Tuple
from fastapi import HTTPException

class BaseService:
    def __init__(self, db: Session, repository):
        self.db = db
        self.repository = repository
    
    def get_all(self, skip: int = 0, limit: int = 100):
        return self.repository.get_all(skip, limit)
    
    def get_paginated(self, page: int = 1, size: int = 10) -> Dict[str, Any]:
        items, total, pages = self.repository.get_paginated(page, size)
        return {
            "items": items,
            "total": total,
            "page": page,
            "size": size,
            "pages": pages
        }
    
    def get_by_id(self, id_value):
        db_item = self.repository.get_by_id(id_value)
        if db_item is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return db_item
    
    def create(self, item_create):
        return self.repository.create(item_create.dict())
    
    def update(self, id_value, item_update):
        db_item = self.repository.update(id_value, item_update.dict(exclude_unset=True))
        if db_item is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return db_item
    
    def delete(self, id_value) -> bool:
        success = self.repository.delete(id_value)
        if not success:
            raise HTTPException(status_code=404, detail="Item not found")
        return success

class CustomerService(BaseService):
    def __init__(self, db: Session):
        super().__init__(db, CustomerRepository(db))
    
    def get_customer_with_orders(self, customer_number: int):
        customer = self.repository.get_with_orders(customer_number)
        if customer is None:
            raise HTTPException(status_code=404, detail="Customer not found")
        return customer

class EmployeeService(BaseService):
    def __init__(self, db: Session):
        super().__init__(db, EmployeeRepository(db))
    
    def get_employees_by_office(self, office_code: str):
        return self.repository.get_by_office_code(office_code)

class OfficeService(BaseService):
    def __init__(self, db: Session):
        super().__init__(db, OfficeRepository(db))

class OrderService(BaseService):
    def __init__(self, db: Session):
        super().__init__(db, OrderRepository(db))
    
    def get_orders_by_customer(self, customer_number: int):
        return self.repository.get_by_customer(customer_number)
    
    def get_order_with_details(self, order_number: int):
        order = self.repository.get_orders_with_details(order_number)
        if order is None:
            raise HTTPException(status_code=404, detail="Order not found")
        return order

class OrderDetailService:
    def __init__(self, db: Session):
        self.db = db
        self.repository = OrderDetailRepository(db)
    
    def get_by_order_number(self, order_number: int):
        return self.repository.get_by_order_number(order_number)
    
    def get_by_composite_key(self, order_number: int, product_code: str):
        detail = self.repository.get_by_composite_key(order_number, product_code)
        if detail is None:
            raise HTTPException(status_code=404, detail="Order detail not found")
        return detail
    
    def create(self, detail_create: OrderDetailCreate):
        return self.repository.create(detail_create.dict())
    
    def update(self, order_number: int, product_code: str, detail_update: OrderDetailUpdate):
        detail = self.repository.get_by_composite_key(order_number, product_code)
        if detail is None:
            raise HTTPException(status_code=404, detail="Order detail not found")
        
        update_data = detail_update.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(detail, key, value)
        
        self.db.commit()
        self.db.refresh(detail)
        return detail
    
    def delete(self, order_number: int, product_code: str) -> bool:
        detail = self.repository.get_by_composite_key(order_number, product_code)
        if detail is None:
            raise HTTPException(status_code=404, detail="Order detail not found")
        
        self.db.delete(detail)
        self.db.commit()
        return True

class ProductService(BaseService):
    def __init__(self, db: Session):
        super().__init__(db, ProductRepository(db))
    
    def get_products_by_product_line(self, product_line: str):
        return self.repository.get_by_product_line(product_line)

class ProductLineService(BaseService):
    def __init__(self, db: Session):
        super().__init__(db, ProductLineRepository(db))

class PaymentService:
    def __init__(self, db: Session):
        self.db = db
        self.repository = PaymentRepository(db)
    
    def get_by_customer_number(self, customer_number: int):
        return self.repository.get_by_customer_number(customer_number)
    
    def get_by_composite_key(self, customer_number: int, check_number: str):
        payment = self.repository.get_by_composite_key(customer_number, check_number)
        if payment is None:
            raise HTTPException(status_code=404, detail="Payment not found")
        return payment
    
    def create(self, payment_create: PaymentCreate):
        return self.repository.create(payment_create.dict())
    
    def update(self, customer_number: int, check_number: str, payment_update: PaymentUpdate):
        payment = self.repository.get_by_composite_key(customer_number, check_number)
        if payment is None:
            raise HTTPException(status_code=404, detail="Payment not found")
        
        update_data = payment_update.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(payment, key, value)
        
        self.db.commit()
        self.db.refresh(payment)
        return payment
    
    def delete(self, customer_number: int, check_number: str) -> bool:
        payment = self.repository.get_by_composite_key(customer_number, check_number)
        if payment is None:
            raise HTTPException(status_code=404, detail="Payment not found")
        
        self.db.delete(payment)
        self.db.commit()
        return True