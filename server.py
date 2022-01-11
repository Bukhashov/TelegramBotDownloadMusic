import os
import socket
import telebot
from dotenv import load_dotenv

load_dotenv()

bot = telebot.TeleBot(os.getenv("BOT_TOKEN"))


def startServer():
    try:
        server = socket.socket(socket.AF_AAL5, socket.SOCK_STREAM)
        server.bind((os.getenv("APP_IP"), int(os.getenv("APP_PORT"))))
        server.listen(int(os.getenv("LISTEN")))
    except KeyboardInterrupt:
        server.close()

startServer() 