from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from services.service import (
    CustomerService, EmployeeService, OfficeService, OrderService,
    OrderDetailService, ProductService, ProductLineService, PaymentService
)
from schemas.schema import (
    CustomerCreate, CustomerUpdate, CustomerResponse,
    EmployeeCreate, EmployeeUpdate, EmployeeResponse,
    OfficeCreate, OfficeUpdate, OfficeResponse,
    OrderCreate, OrderUpdate, OrderResponse,
    OrderDetailCreate, OrderDetailUpdate, OrderDetailResponse,
    ProductCreate, ProductUpdate, ProductResponse,
    ProductLineCreate, ProductLineUpdate, ProductLineResponse,
    PaymentCreate, PaymentUpdate, PaymentResponse,
    PaginatedResponse
)
from database.session import get_db
from typing import List

class BaseController:
    def __init__(self, prefix: str, tags: List[str]):
        self.router = APIRouter(prefix=prefix, tags=tags)
        self.setup_routes()
    
    def setup_routes(self):
        pass

class CustomerController(BaseController):
    def __init__(self):
        super().__init__("/customers", ["customers"])
    
    def setup_routes(self):
        @self.router.get("/", response_model=List[CustomerResponse])
        def get_customers(skip: int = 0, limit: int = 2, db: Session = Depends(get_db)):
            service = CustomerService(db)
            return service.get_all(skip, limit)
        
        @self.router.get("/paginated", response_model=PaginatedResponse)
        def get_customers_paginated(page: int = 1, size: int = 10, db: Session = Depends(get_db)):
            service = CustomerService(db)
            return service.get_paginated(page, size)
        
        @self.router.get("/{customer_number}", response_model=CustomerResponse)
        def get_customer(customer_number: int, db: Session = Depends(get_db)):
            service = CustomerService(db)
            return service.get_by_id(customer_number)
        
        @self.router.get("/{customer_number}/orders")
        def get_customer_orders(customer_number: int, db: Session = Depends(get_db)):
            service = CustomerService(db)
            customer = service.get_customer_with_orders(customer_number)
            return customer.orders
        
        @self.router.post("/", response_model=CustomerResponse)
        def create_customer(customer: CustomerCreate, db: Session = Depends(get_db)):
            service = CustomerService(db)
            return service.create(customer)
        
        @self.router.put("/{customer_number}", response_model=CustomerResponse)
        def update_customer(customer_number: int, customer: CustomerUpdate, db: Session = Depends(get_db)):
            service = CustomerService(db)
            return service.update(customer_number, customer)
        
        @self.router.delete("/{customer_number}")
        def delete_customer(customer_number: int, db: Session = Depends(get_db)):
            service = CustomerService(db)
            return service.delete(customer_number)

class EmployeeController(BaseController):
    def __init__(self):
        super().__init__("/employees", ["employees"])
    
    def setup_routes(self):
        @self.router.get("/", response_model=List[EmployeeResponse])
        def get_employees(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
            service = EmployeeService(db)
            return service.get_all(skip, limit)
        
        @self.router.get("/paginated", response_model=PaginatedResponse)
        def get_employees_paginated(page: int = 1, size: int = 10, db: Session = Depends(get_db)):
            service = EmployeeService(db)
            return service.get_paginated(page, size)
        
        @self.router.get("/{employee_number}", response_model=EmployeeResponse)
        def get_employee(employee_number: int, db: Session = Depends(get_db)):
            service = EmployeeService(db)
            return service.get_by_id(employee_number)
        
        @self.router.get("/office/{office_code}", response_model=List[EmployeeResponse])
        def get_employees_by_office(office_code: str, db: Session = Depends(get_db)):
            service = EmployeeService(db)
            return service.get_employees_by_office(office_code)
        
        @self.router.post("/", response_model=EmployeeResponse)
        def create_employee(employee: EmployeeCreate, db: Session = Depends(get_db)):
            service = EmployeeService(db)
            return service.create(employee)
        
        @self.router.put("/{employee_number}", response_model=EmployeeResponse)
        def update_employee(employee_number: int, employee: EmployeeUpdate, db: Session = Depends(get_db)):
            service = EmployeeService(db)
            return service.update(employee_number, employee)
        
        @self.router.delete("/{employee_number}")
        def delete_employee(employee_number: int, db: Session = Depends(get_db)):
            service = EmployeeService(db)
            return service.delete(employee_number)

class OfficeController(BaseController):
    def __init__(self):
        super().__init__("/offices", ["offices"])
    
    def setup_routes(self):
        @self.router.get("/", response_model=List[OfficeResponse])
        def get_offices(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
            service = OfficeService(db)
            return service.get_all(skip, limit)
        
        @self.router.get("/paginated", response_model=PaginatedResponse)
        def get_offices_paginated(page: int = 1, size: int = 10, db: Session = Depends(get_db)):
            service = OfficeService(db)
            return service.get_paginated(page, size)
        
        @self.router.get("/{office_code}", response_model=OfficeResponse)
        def get_office(office_code: str, db: Session = Depends(get_db)):
            service = OfficeService(db)
            return service.get_by_id(office_code)
        
        @self.router.post("/", response_model=OfficeResponse)
        def create_office(office: OfficeCreate, db: Session = Depends(get_db)):
            service = OfficeService(db)
            return service.create(office)
        
        @self.router.put("/{office_code}", response_model=OfficeResponse)
        def update_office(office_code: str, office: OfficeUpdate, db: Session = Depends(get_db)):
            service = OfficeService(db)
            return service.update(office_code, office)
        
        @self.router.delete("/{office_code}")
        def delete_office(office_code: str, db: Session = Depends(get_db)):
            service = OfficeService(db)
            return service.delete(office_code)

class OrderController(BaseController):
    def __init__(self):
        super().__init__("/orders", ["orders"])
    
    def setup_routes(self):
        @self.router.get("/", response_model=List[OrderResponse])
        def get_orders(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
            service = OrderService(db)
            return service.get_all(skip, limit)
        
        @self.router.get("/paginated", response_model=PaginatedResponse)
        def get_orders_paginated(page: int = 1, size: int = 10, db: Session = Depends(get_db)):
            service = OrderService(db)
            return service.get_paginated(page, size)
        
        @self.router.get("/{order_number}", response_model=OrderResponse)
        def get_order(order_number: int, db: Session = Depends(get_db)):
            service = OrderService(db)
            return service.get_by_id(order_number)
        
        @self.router.get("/{order_number}/details")
        def get_order_with_details(order_number: int, db: Session = Depends(get_db)):
            service = OrderService(db)
            order = service.get_order_with_details(order_number)
            return order.orderDetails
        
        @self.router.get("/customer/{customer_number}", response_model=List[OrderResponse])
        def get_orders_by_customer(customer_number: int, db: Session = Depends(get_db)):
            service = OrderService(db)
            return service.get_orders_by_customer(customer_number)
        
        @self.router.post("/", response_model=OrderResponse)
        def create_order(order: OrderCreate, db: Session = Depends(get_db)):
            service = OrderService(db)
            return service.create(order)
        
        @self.router.put("/{order_number}", response_model=OrderResponse)
        def update_order(order_number: int, order: OrderUpdate, db: Session = Depends(get_db)):
            service = OrderService(db)
            return service.update(order_number, order)
        
        @self.router.delete("/{order_number}")
        def delete_order(order_number: int, db: Session = Depends(get_db)):
            service = OrderService(db)
            return service.delete(order_number)

class OrderDetailController(BaseController):
    def __init__(self):
        super().__init__("/orderdetails", ["orderdetails"])
    
    def setup_routes(self):
        @self.router.get("/order/{order_number}", response_model=List[OrderDetailResponse])
        def get_order_details(order_number: int, db: Session = Depends(get_db)):
            service = OrderDetailService(db)
            return service.get_by_order_number(order_number)
        
        @self.router.get("/{order_number}/{product_code}", response_model=OrderDetailResponse)
        def get_order_detail(order_number: int, product_code: str, db: Session = Depends(get_db)):
            service = OrderDetailService(db)
            return service.get_by_composite_key(order_number, product_code)
        
        @self.router.post("/", response_model=OrderDetailResponse)
        def create_order_detail(order_detail: OrderDetailCreate, db: Session = Depends(get_db)):
            service = OrderDetailService(db)
            return service.create(order_detail)
        
        @self.router.put("/{order_number}/{product_code}", response_model=OrderDetailResponse)
        def update_order_detail(
            order_number: int, 
            product_code: str, 
            order_detail: OrderDetailUpdate, 
            db: Session = Depends(get_db)
        ):
            service = OrderDetailService(db)
            return service.update(order_number, product_code, order_detail)
        
        @self.router.delete("/{order_number}/{product_code}")
        def delete_order_detail(order_number: int, product_code: str, db: Session = Depends(get_db)):
            service = OrderDetailService(db)
            return service.delete(order_number, product_code)

class ProductController(BaseController):
    def __init__(self):
        super().__init__("/products", ["products"])
    
    def setup_routes(self):
        @self.router.get("/", response_model=List[ProductResponse])
        def get_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
            service = ProductService(db)
            return service.get_all(skip, limit)
        
        @self.router.get("/paginated", response_model=PaginatedResponse)
        def get_products_paginated(page: int = 1, size: int = 10, db: Session = Depends(get_db)):
            service = ProductService(db)
            return service.get_paginated(page, size)
        
        @self.router.get("/{product_code}", response_model=ProductResponse)
        def get_product(product_code: str, db: Session = Depends(get_db)):
            service = ProductService(db)
            return service.get_by_id(product_code)
        
        @self.router.get("/productline/{product_line}", response_model=List[ProductResponse])
        def get_products_by_product_line(product_line: str, db: Session = Depends(get_db)):
            service = ProductService(db)
            return service.get_products_by_product_line(product_line)
        
        @self.router.post("/", response_model=ProductResponse)
        def create_product(product: ProductCreate, db: Session = Depends(get_db)):
            service = ProductService(db)
            return service.create(product)
        
        @self.router.put("/{product_code}", response_model=ProductResponse)
        def update_product(product_code: str, product: ProductUpdate, db: Session = Depends(get_db)):
            service = ProductService(db)
            return service.update(product_code, product)
        
        @self.router.delete("/{product_code}")
        def delete_product(product_code: str, db: Session = Depends(get_db)):
            service = ProductService(db)
            return service.delete(product_code)

class ProductLineController(BaseController):
    def __init__(self):
        super().__init__("/productlines", ["productlines"])
    
    def setup_routes(self):
        @self.router.get("/", response_model=List[ProductLineResponse])
        def get_product_lines(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
            service = ProductLineService(db)
            return service.get_all(skip, limit)
        
        @self.router.get("/paginated", response_model=PaginatedResponse)
        def get_product_lines_paginated(page: int = 1, size: int = 10, db: Session = Depends(get_db)):
            service = ProductLineService(db)
            return service.get_paginated(page, size)
        
        @self.router.get("/{product_line}", response_model=ProductLineResponse)
        def get_product_line(product_line: str, db: Session = Depends(get_db)):
            service = ProductLineService(db)
            return service.get_by_id(product_line)
        
        @self.router.post("/", response_model=ProductLineResponse)
        def create_product_line(product_line: ProductLineCreate, db: Session = Depends(get_db)):
            service = ProductLineService(db)
            return service.create(product_line)
        
        @self.router.put("/{product_line}", response_model=ProductLineResponse)
        def update_product_line(product_line: str, product_line_update: ProductLineUpdate, db: Session = Depends(get_db)):
            service = ProductLineService(db)
            return service.update(product_line, product_line_update)
        
        @self.router.delete("/{product_line}")
        def delete_product_line(product_line: str, db: Session = Depends(get_db)):
            service = ProductLineService(db)
            return service.delete(product_line)

class PaymentController(BaseController):
    def __init__(self):
        super().__init__("/payments", ["payments"])
    
    def setup_routes(self):
        @self.router.get("/customer/{customer_number}", response_model=List[PaymentResponse])
        def get_payments_by_customer(customer_number: int, db: Session = Depends(get_db)):
            service = PaymentService(db)
            return service.get_by_customer_number(customer_number)
        
        @self.router.get("/{customer_number}/{check_number}", response_model=PaymentResponse)
        def get_payment(customer_number: int, check_number: str, db: Session = Depends(get_db)):
            service = PaymentService(db)
            return service.get_by_composite_key(customer_number, check_number)
        
        @self.router.post("/", response_model=PaymentResponse)
        def create_payment(payment: PaymentCreate, db: Session = Depends(get_db)):
            service = PaymentService(db)
            return service.create(payment)
        
        @self.router.put("/{customer_number}/{check_number}", response_model=PaymentResponse)
        def update_payment(
            customer_number: int, 
            check_number: str, 
            payment: PaymentUpdate, 
            db: Session = Depends(get_db)
        ):
            service = PaymentService(db)
            return service.update(customer_number, check_number, payment)
        
        @self.router.delete("/{customer_number}/{check_number}")
        def delete_payment(customer_number: int, check_number: str, db: Session = Depends(get_db)):
            service = PaymentService(db)
            return service.delete(customer_number, check_number)