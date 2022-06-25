from fastapi import APIRouter

from application_server.rest_introduction_app.api.challenges.challenge_2 import challenge_2
from application_server.rest_introduction_app.api.challenges.challenge_primer import challenge_primer
from application_server.rest_introduction_app.api.fundamentals import token_authentication, playing_with_headers, \
    cookies, basic_authentication, client_error, successful, serving_images, server_error

api_router = APIRouter()

api_router.include_router(router=successful.router,
                          tags=["Successful requests responses"])
api_router.include_router(router=client_error.router,
                          tags=["Client error requests responses"])
api_router.include_router(router=server_error.router,
                          tags=["Server error requests responses"])
api_router.include_router(router=playing_with_headers.router,
                          tags=["Playing with headers responses"])
api_router.include_router(router=basic_authentication.router,
                          tags=["Basic auth example"])
api_router.include_router(router=token_authentication.router,
                          tags=["Token Authentication"])
api_router.include_router(router=serving_images.router,
                          tags=["Serving images"])
api_router.include_router(router=cookies.router,
                          tags=["Cookies"])

api_router.include_router(router=challenge_primer.router,
                          tags=[challenge_primer.challenge_tag])
api_router.include_router(router=challenge_2.router,
                          tags=[challenge_2.challenge_tag])
