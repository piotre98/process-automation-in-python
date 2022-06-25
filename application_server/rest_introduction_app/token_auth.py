import uvicorn
from fastapi import FastAPI
from application_server.rest_introduction_app.api.fundamentals import token_authentication

app = FastAPI(
    title='HTTP - REST API training',
    description="Token authentication training",
    version="0.1",
    docs_url="/",
    redoc_url=None
)

app.include_router(router=token_authentication.router,
                   tags=["Token Authentication"])


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8080)