from . import api_v1_blueprint, response_wrapper


@response_wrapper
@api_v1_blueprint.get('/test')
async def test_method():
    return {
        "status" : "ok!"
    }