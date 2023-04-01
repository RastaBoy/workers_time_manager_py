from quart import Quart
from hypercorn.config import Config as HypercornConfig
from hypercorn.asyncio import serve

from ..config import ServerSettings

from .blueprints.api.v1 import api_v1_blueprint

def build_app(is_dev : bool = False) -> Quart:
    app = Quart(__name__)
    app.register_blueprint(api_v1_blueprint, url_prefix="/api/v1")
    
    
    if is_dev:
        from quart_cors import cors
        app = cors(app, allow_origin='*')
    
    return app


async def run_server(server_settings : ServerSettings, is_dev : bool = False):
    hyper_cfg = HypercornConfig()
    hyper_cfg.bind = f'0.0.0.0:{server_settings.port}'

    return await serve(build_app(is_dev), hyper_cfg)