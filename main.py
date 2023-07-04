from fastapi import FastAPI, Request

from constants import SUCCESS_DATA_FETCH_MESSAGE, GET_API_RESPONSE_DATA
from responses import SuccessResponse

app = FastAPI()


@app.get("/")
async def demo_get_api(request: Request):
    return SuccessResponse(data=GET_API_RESPONSE_DATA, message=SUCCESS_DATA_FETCH_MESSAGE)
