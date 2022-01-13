import os
from dotenv import load_dotenv
load_dotenv()
config = {
    'appName' : os.getenv("APP_NAME"),
    'appAbout' : 'Muqityat music downlode bot',
    'appIp' : os.getenv("APP_IP"),
    'appPort' : int(os.getenv("APP_PORT")),
    'appListen' : int(os.getenv("APP_LISTEN")),
    'botName' : os.getenv("BOT_NAME"),
    'botToken' : os.getenv("BOT_TOKEN"),
}
