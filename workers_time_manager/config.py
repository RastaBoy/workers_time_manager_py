from .parametrica import ParametricaSingletone, Field, Fieldset
from .parametrica.io import YAMLFileConfigIO, VirtualYAMLFileConfigIO


class ServerSettings(Fieldset):
    port = Field[int](default=3005).label('Порт, на котором будет запущен сервер')


class Config(ParametricaSingletone):
    server_settings = Field[ServerSettings]().label('Настройки сервера')
    log_level = Field[int](default=3).label("Уровень логирования")


class DevConfig(ParametricaSingletone):
    is_dev = Field[bool](default=False).label('Режим разработчика')
    
    
Config(YAMLFileConfigIO('settings.yaml'))
DevConfig(VirtualYAMLFileConfigIO('dev.env'))