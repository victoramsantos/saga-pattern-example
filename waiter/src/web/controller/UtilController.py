import json

from src.library.logger.Logger import Logger


class UtilController:
    @staticmethod
    def build_response_with_json(response: str, status_code: int):
        return response, status_code, {'Content-Type': 'application/json'}

    @staticmethod
    def build_response(response, status_code: int):
        return json.dumps(response), status_code, {'Content-Type': 'application/json'}

    @staticmethod
    def build_error_payback(exception: Exception, status_code: int) -> dict:
        Logger.error("Exception Error", str(exception))
        status: str

        if status_code == 400:
            status = str(exception)
        else:
            status = "Internal Server Error"

        return {
            "error_message": status,
            "status_code": status_code
        }
