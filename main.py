import discord
from discord.ext import commands
import nekos
import os
import datetime

token = os.environ.get('token')

client = commands.Bot(command_prefix="$")


@client.event
async def on_ready(): 
    print(datetime.now() + " Logged in as {0.user}".format(client))
 

@client.command(name="ping")
async def ping(ctx):
    await ctx.message.channel.send('Pong!')

    
@client.command(name="cycki")
async def cycki(ctx):
    if ctx.message.channel.is_nsfw():
        await ctx.message.channel.send(nekos.img("boobs"))
    else:
        await ctx.message.channel.send("Aby użyć tej komendy kanał musi być oznaczony jako NSFW")

        
@client.command(name="pusia")
async def pusia(ctx):
    if ctx.message.channel.is_nsfw():
        await ctx.message.channel.send(nekos.img("pussy"))
    else:
        await ctx.message.channel.send("Aby użyć tej komendy kanał musi być oznaczony jako NSFW")


client.run(token)
