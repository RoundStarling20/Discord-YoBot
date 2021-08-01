import discord
from discord.ext import commands

def isItme(ctx):
        return ctx.message.author.id == 220327217312432129

class dev(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Pong! {round(self.client.latency * 1000)}ms')

    @commands.Cog.listener()
    async def on_message(self, message):
        print(f"{message.author} said {message.content}")

    @commands.command()
    @commands.check(isItme)
    async def reload(self, ctx,extension):
        self.client.unload_extension(f'cogs.{extension}')
        self.client.load_extension(f'cogs.{extension}')
        await ctx.send(f'Cogs have been unloaded and loaded [{extension}]')


def setup(client):
    client.add_cog(dev(client))