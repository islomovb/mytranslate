import requests
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN="5065496513:AAGfJFGnLjJthV__vuWwRR6_YPKvSJ4V4Rs"

bot=Bot(API_TOKEN)
dp=Dispatcher(bot)




@dp.message_handler()
async def qaytar(message: types.Message):
    url=f"https://goweather.herokuapp.com/weather/{message.text}"
    response=requests.get(url)
    gradus=response.json()['temperature']
    shamol=response.json()['wind']
    await message.answer(f"{message.text}da {gradus}🌡 .Shamol {shamol}💨 esyapti!")



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)


    






