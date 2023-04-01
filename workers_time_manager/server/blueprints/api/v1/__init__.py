from quart import Blueprint, Response

from typing import Awaitable

api_v1_blueprint = Blueprint(
    "api_v1",
    __name__
)


@api_v1_blueprint.errorhandler(Exception)
async def error_handler(e : Exception):
    return Response({
            "result" : False,
            "error_class" : e.__class__.__name__,
            "error_text" : str(e)
        }, status=417)
    

def response_wrapper(func : Awaitable):
    async def wrap(*args, **kwargs):
        return Response(
            {
                "result" : True,
                "data" : await func(*args, **kwargs)
            },
            status=200
        )
    return wrap
    
    
from .routes import *