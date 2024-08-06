from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from commands import *
from keybord import keybord
from deep_translator import GoogleTranslator
from random import randint
from PIL import Image
import pytesseract
import os

with open("config.yaml") as ymlFile:
    config = yaml.load(ymlFile.read(), Loader=yaml.Loader)


bot = Bot(config.get("telegram").get("TOKEN"))
dp = Dispatcher(bot)

pytesseract.pytesseract.tesseract_cmd = r"F:\Program Files\Tesseract-OCR\tesseract.exe"


def get_perevod_ru(en_slovo):
	return GoogleTranslator(source="en", target="ru").translate(en_slovo)


def teseract_recognition(path_img):
    return pytesseract.image_to_string(Image.open(path_img), lang='rus+eng', config=r'--oem 3 --psm 6')


@dp.message_handler(lambda message: message.text.lower() == "старт" or message.text.lower() == "/start")
async def start_command(message: types.message):
	await message.answer(text=START_COMMAND,
						parse_mode="HTML",
						reply_markup=keybord)



@dp.message_handler(lambda message: message.text.lower() == "помощь")
async def help_command(message: types.message):
	await message.answer(text=HELP_COMMENT,
						parse_mode="HTML")


@dp.message_handler(lambda message: message.text.lower() == "описание")
async def deskription_command(message: types.message):
	await message.answer(text=DESKRIPTION_COMMAND,
						parse_mode="HTML")


@dp.message_handler(lambda message: message.text.lower() == "о создателе")
async def info_command(message: types.message):
	await message.answer(text=INFO_COMMAND,
						parse_mode="HTML")


@dp.message_handler(lambda message: message.text.lower() == "перевод по тексту")
async def info_perevod_text(message: types.message):
	await message.answer("Введите текст на англиском!")



@dp.message_handler(lambda message: message.text.lower() == "перевод по фото")
async def info_perevod_photo(message: types.message):
	text = """
Отправте фотку текста!
На фотке должен хороше заметен текст!
	"""

	await message.answer(text)



@dp.message_handler(content_types=["photo"])
async def perevod_photo(message: types.message):
	await message.answer("Ожидайте!")
	
	id_photo = randint(0, 10000)

	await message.photo[-1].download(f"photo/photo_{id_photo}.jpg")

	text = f"""
Перевод текста по картинке:
--> {get_perevod_ru(teseract_recognition(f"photo/photo_{id_photo}.jpg"))}
	"""

	await message.reply(text)

	os.remove(f"photo/photo_{id_photo}.jpg")




@dp.message_handler()
async def perevod_text(message: types.message):
	text = f"""
Перевод по слову "{message.text}"
--> {get_perevod_ru(message.text)}
	"""



	await message.answer(text)




if __name__ == "__main__":
	executor.start_polling(dp, skip_updates=True)