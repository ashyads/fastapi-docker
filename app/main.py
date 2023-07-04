from fastapi import FastAPI, Request

from app.constants import GET_API_RESPONSE_DATA, SUCCESS_DATA_FETCH_MESSAGE
from app.responses import SuccessResponse

app = FastAPI()


@app.get("/")
async def demo_get_api(request: Request):
    return SuccessResponse(data=GET_API_RESPONSE_DATA, message=SUCCESS_DATA_FETCH_MESSAGE)