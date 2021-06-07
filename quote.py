import discord
import requests
import json
import os

client = discord.Client()

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('quote'):
    quote = get_quote()
    await message.channel.send(quote)

client.run('ODQ3MTA0NjI5MzY4MDI5MjE0.YK5Nqg.zcclr4RFzNJ2GkZf8ZLzZqINyow')

from discord.ext import commands

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
