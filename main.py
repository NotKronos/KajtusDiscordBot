import discord
from discord.ext import commands
import nekos

f = open("token", "r")
token = f.read()
f.close()

client = commands.Bot(command_prefix="$")


@client.command(name="ping")
async def ping(ctx):
    await ctx.message.channel.send('Pong!')

@client.command(name="cycki")
async def cycki(ctx):
    if ctx.message.channel.is_nsfw():
        await ctx.message.channel.send(nekos.img("boobs"))
    else:
        await ctx.message.channel.send("Aby użyć tej komendy kanał musi być oznaczony jako NSFW")


client.run(token)
