import discord
from discord.ext import commands

def isItme(ctx):
        return ctx.message.author.id == 220327217312432129

class dev(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_connect(self):
        print("Bot has connected to Discord!")

    @commands.Cog.listener()
    async def on_ready(self):
        print("Bot is ready!")

    @commands.Cog.listener()
    async def on_member_join(self, member):   
        print(f"{member} has joined [{member.guild.name}: {member.guild.id}].")

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        print(f"{member} has left [{member.guild.name}: {member.guild.id}].")

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Pong! {round(self.client.latency * 1000)}ms')

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id == 870467770846945290:
            print("Yo? responded")
        else:
            print(f"{message.author} said {message.content}")

    @commands.command()
    @commands.check(isItme)
    async def reload(self, ctx, extension):
        self.client.unload_extension(f'cogs.{extension}')
        self.client.load_extension(f'cogs.{extension}')
        await ctx.send(f'[{extension}] has been unloaded and reloaded')


def setup(client):
    client.add_cog(dev(client))