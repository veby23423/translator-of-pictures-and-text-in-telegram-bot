from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove



keybord = ReplyKeyboardMarkup(resize_keyboard=True)
keybutton1 = KeyboardButton(text="Старт")
keybutton2 = KeyboardButton(text="Помощь")
keybutton3 = KeyboardButton(text="Описание")
keybutton4 = KeyboardButton(text="О создателе")
keybutton5 = KeyboardButton(text="Перевод по тексту")
keybutton6 = KeyboardButton(text="Перевод по фото")

keybord.add(keybutton1, keybutton2).add(keybutton3, keybutton4).add(keybutton5, keybutton6)

