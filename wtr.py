from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from pyowm.utils.config import get_default_config

config_dict = get_default_config()
config_dict['language'] = 'ru'

owm = OWM('1e7c30df357a3d1c5bcb070184731643', config=config_dict)
mgr = owm.weather_manager()

city = input("Which city are you in: ")

observation = mgr.weather_at_place(city)
w = observation.weather
temp = w.temperature('celsius')

print("Current weather in " + city + ": " + str(temp))