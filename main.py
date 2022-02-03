import discord
from discord.ext import commands
import nekos

token = "OTM4NDM1Mzg5MDQyMDczNjAx.YfqQEA.ZuEgGj3iujmul6EA0ya79Rp0kI0"

client = commands.Bot(command_prefix="$")


@client.command(name="ping")
async def ping(ctx):
    await ctx.message.channel.send('Pong!')


client.run(token)
