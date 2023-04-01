import os

from loguru import logger as log

from .config import Config, DevConfig
from .server import run_server

from .db import *

__version__ = (1,0,0,0)

log.add(
    os.path.join(os.getcwd(), 'logs', '{time:DD-MM-YYYY}.log'), 
    format='{time:HH:mm:ss.SSSZ} | [{level}]\t| {message}'
)
log.critical('='*15 + ' Инициализация Workers Time Manager v'+".".join(str(x) for x in __version__) + ' ' +'='*15)


async def run_application():
    await Database.create_database()
    await run_server(Config().server_settings, DevConfig().is_dev)
