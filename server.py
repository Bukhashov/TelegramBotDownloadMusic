import telebot
from telebot import types
from config import config
# import pymongo

bot = telebot.TeleBot(config['botToken'])
print("{} >>> server connected to Telegram bot across TOKEN".format(config['appName']))

@bot.message_handler(commands=['start', 'Start', 'START'])
def botStartComand(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    itemYoutube = types.InlineKeyboardButton('YouTube', callback_data='youtube')
    itemInstagram = types.InlineKeyboardButton('Instagram', callback_data='instagram')
    itemSpotify = types.InlineKeyboardButton('Spotify', callback_data='spotify')
    itemTiktok = types.InlineKeyboardButton('TikTok', callback_data='tiktok')
    itemVK = types.InlineKeyboardButton('VK', callback_data='vk')
    itemBack = types.InlineKeyboardButton('Back to bot', callback_data='back')
    markup.add(itemYoutube, itemSpotify, itemInstagram, itemTiktok, itemVK, itemBack)
    bot.send_message(message.chat.id, "Berik Bukhashov Sayranbek uli", reply_markup=markup)

@bot.callback_query_handler(func=lambda call:True)
def answer(call):
    if call.message:
        if call.data == 'youtube':
            bot.send_message(call.message.chat.id, "YouTube")
        if call.data == 'spotify':
            bot.send_message(call.message.chat.id, "Spotify")
        if call.data == 'instagram':
            bot.send_message(call.message.chat.id, "Instagram")
        if call.data == 'tiktok':
            bot.send_message(call.message.chat.id, "TikTok")
        if call.data == 'vk':
            bot.send_message(call.message.chat.id, "VK")
        if call.data == 'back':
            bot.send_message(call.message.chat.id, "back")

@bot.message_handler(content_types=['text'])
def botContentText(message):
    if message.text.lower() == 'привет' or message.text.lower() == 'hi' or message.text.lower() == 'hello' or message.text.lower() == 'start':
        botStartComand(message)

# Help
# About
# @bot.message_handler(commands=['about','About'])
# async def botAboutCommand(message):
    # await bot.send_message(message.chat.id, config['appAbout'])

bot.infinity_polling()