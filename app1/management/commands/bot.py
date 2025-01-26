from aiogram import Bot, Dispatcher, executor, types
from models import Company
from models import Olimpiad    
from django.db import models
from django import forms
from django.utils.timezone import now
import datetime
import os
import sys
import django
from pyrogram import Client
from pyrogram.raw.functions.contacts import ResolveUsername

f = open('hh.txt','r')


API_TOKEN = '8175076947:AAGfDShPc9wI6S6JonXMJNC2p6rgMjd-oWA' #В одинарных кавычках размещаем токен, полученный от @BotFather.

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


def resolve_username_to_user_id(username: str) -> int | None:
    with bot:
        r = bot.invoke(ResolveUsername(username=username))
        if r.users:
            return r.users[0].id
        return None
now = datetime.datetime.now()
print(now)
jj=[]
for i in Company.objects.all():
    jj.append([i.name, i.telega])


@dp.message_handler(commands=['start']) #Явно указываем в декораторе, на какую команду реагируем.
async def send_welcome(message: types.Message):
   await message.reply("Привет!\n Ты хотел отправить своё резюме? \n Напиши компанию,в которой хотел бы стажироваться") #Так как код работает асинхронно, то обязательно пишем await.

@dp.message_handler()
async def echo(message: types.Message):   
    for i in jj:
        if i[0]==message.text:
            await bot.send_message(i[1], text='Вам было отправлено резюме. Хотите посмотреть?')

if __name__ == '__main__':
   executor.start_polling(dp, skip_updates=True)