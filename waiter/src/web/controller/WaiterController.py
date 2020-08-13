from typing import List

from flask import Blueprint, request
from flask_cors import cross_origin

from src.model.Product import Product
from src.web.controller import service
from src.web.controller.UtilController import UtilController

waiter_controller = Blueprint('WaiterController', __name__)


class WaiterController:
    @staticmethod
    @cross_origin()
    @waiter_controller.route('/menu', methods=['GET'])
    def get_menu():
        response: dict
        status_code: int = 200
        try:
            products: List[Product] = service.get_products()
            response = [product.__dict__ for product in products]
        except Exception as exception:
            status_code = 500
            response = UtilController.build_error_payback(exception, status_code)

        return UtilController.build_response(response, status_code)

    @staticmethod
    @cross_origin()
    @waiter_controller.route('/order', methods=['POST'])
    def order():
        response: dict
        status_code: int = 200
        try:
            order = request.json
            service.make_items(order)
            response = {}
        except Exception as exception:
            status_code = 500
            response = UtilController.build_error_payback(exception, status_code)

        return UtilController.build_response(response, status_code)

    @staticmethod
    @cross_origin()
    @waiter_controller.route('/order', methods=['GET'])
    def get_order():
        response: dict
        status_code: int = 200
        try:
            orders = service.get_orders()
            response = [order.__dict__ for order in orders]
        except Exception as exception:
            status_code = 500
            response = UtilController.build_error_payback(exception, status_code)

        return UtilController.build_response(response, status_code)
