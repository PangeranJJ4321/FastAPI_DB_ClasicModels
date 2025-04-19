from fastapi import APIRouter
from controllers.controller import (
    CustomerController, EmployeeController, OfficeController, OrderController,
    OrderDetailController, ProductController, ProductLineController, PaymentController
)

def setup_routes() -> APIRouter:
    api_router = APIRouter()
    
    # Initialize controllers
    customer_controller = CustomerController()
    employee_controller = EmployeeController()
    office_controller = OfficeController()
    order_controller = OrderController()
    order_detail_controller = OrderDetailController()
    product_controller = ProductController()
    product_line_controller = ProductLineController()
    payment_controller = PaymentController()
    
    # Include routers
    api_router.include_router(customer_controller.router)
    api_router.include_router(employee_controller.router)
    api_router.include_router(office_controller.router)
    api_router.include_router(order_controller.router)
    api_router.include_router(order_detail_controller.router)
    api_router.include_router(product_controller.router)
    api_router.include_router(product_line_controller.router)
    api_router.include_router(payment_controller.router)
    
    return api_router