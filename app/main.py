from fastapi import FastAPI, Depends, Request
from fastapi.responses import JSONResponse

from app.routers.dog import router as dog_router
from app.routers.health import router as health_router
# from dog_api.routers.auth import verify_api_key
from schemas import Output


app = FastAPI()
app.include_router(
    router=dog_router,
    prefix="/dog",
    # dependencies=[Depends(verify_api_key)]
)
app.include_router(health_router)


@app.exception_handler(Exception)
async def app_error_handler(
    request: Request,
    exception: Exception
) -> JSONResponse:
    return JSONResponse(
        status_code=401,
        content={"output": Output(success=False, message="Unauthorized")}
    )










