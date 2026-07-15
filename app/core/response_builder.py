class ResponseBuilder:

    @staticmethod
    def success(

        response_type,

        data

    ):

        return {

            "success": True,

            "type": response_type,

            "data": data

        }

    @staticmethod
    def error(

        message

    ):

        return {

            "success": False,

            "type": "error",

            "data": {

                "message": message

            }

        }