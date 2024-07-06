
class ResponseUtil:
    @staticmethod
    def success(message, data):
        return {
            'status': 'success',
            'message': message,
            'data': data
        }

    @staticmethod
    def error(message, data):
        return {
            'status': 'error',
            'message': message,
            'data': data
        }