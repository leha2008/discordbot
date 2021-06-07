import json
import requests
import discord
from discord.ext import commands
import os
bot = commands.Bot(command_prefix='!')

@bot.command(pass_context=True)
async def trytext(ctx, arg):
    await ctx.send(arg)

@bot.command()
async def fox(ctx):
    response = requests.get('https://some-random-api.ml/img/fox') # Get-запрос
    json_data = json.loads(response.text) # Извлекаем JSON
    
    embed = discord.Embed(color = 0xff9900, title = 'Random Fox') # Создание Embed'a
    embed.set_image(url = json_data['link']) # Устанавливаем картинку Embed'a
    await ctx.send(embed = embed) # Отправляем Embed
@bot.command()
async def meme(ctx):
    response = requests.get('https://meme-api.herokuapp.com/gimme') # Get-запрос
    json_data = json.loads(response.text) # Извлекаем JSON

    embed = discord.Embed(color = 0xff9900, title = json_data['title']) # Создание Embed'a
    embed.set_image(url = json_data['url']) # Устанавливаем картинку Embed'a
    await ctx.send(embed = embed) # Отправляем Embed

bot.run('ODQ3MTA0NjI5MzY4MDI5MjE0.YK5Nqg.zcclr4RFzNJ2GkZf8ZLzZqINyow')
