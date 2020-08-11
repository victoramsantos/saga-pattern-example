from flask import (
    Blueprint)

from src.service.AppService import AppService
from src.web.controller.UtilController import UtilController

app_controller = Blueprint('AppController', __name__)

service: AppService = AppService()

class AppController:
    @staticmethod
    @app_controller.route('/health', methods=['GET'])
    def health():
        is_health, response = service.health_checker()

        return UtilController.build_response(response, 200 if is_health else 503)
