from fastapi import status
from fastapi.responses import JSONResponse


class BaseResponse(JSONResponse):
    def __init__(self, data=None, message=None, status=True, headers=None):
        data_content = {
            'status': status,
            'message': message,
            'data': data,
        }
        super().__init__(content=data_content, headers=headers)


class NegativeResponse(BaseResponse):
    def __init__(self, data=None, message=None, status=False):
        super().__init__(data=data, status=status, message=message)


class PositiveResponse(BaseResponse):
    def __init__(self, data=None, message=None, status=True):
        super().__init__(data=data, status=status, message=message)


class SuccessResponse(PositiveResponse):
    status_code = status.HTTP_200_OK


class CreateResponse(PositiveResponse):
    status_code = status.HTTP_201_CREATED


class NoContentResponse(NegativeResponse):
    status_code = status.HTTP_204_NO_CONTENT


class BadRequestResponse(NegativeResponse):
    status_code = status.HTTP_400_BAD_REQUEST


class GoneResponse(NegativeResponse):
    status_code = status.HTTP_410_GONE


class AccessDeniedResponse(NegativeResponse):
    status_code = status.HTTP_401_UNAUTHORIZED


class ForbiddenErrorResponse(NegativeResponse):
    status_code = status.HTTP_403_FORBIDDEN


class NotAcceptableResponse(NegativeResponse):
    status_code = status.HTTP_406_NOT_ACCEPTABLE


class UnprocessableEntityResponse(NegativeResponse):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY


class NotFoundResponse(NegativeResponse):
    status_code = status.HTTP_404_NOT_FOUND
