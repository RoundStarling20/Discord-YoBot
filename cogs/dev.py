import custom
import discord
import json
from custom import emojiList
from discord.ext import commands


class dev(commands.Cog, name="Developer Tools", description="A set of tools used for my development"):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_connect(self):
        print("Bot has connected to Discord!")

    @commands.Cog.listener()
    async def on_ready(self):
        print("Bot is ready!")

    @commands.command(help= "checks the ping of the bot")
    async def ping(self, ctx):
        await ctx.send(f'Pong! {round(self.client.latency * 1000)}ms')

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id == 870467770846945290:
            print("Yo? responded")
        else:
            print(f"{message.author} said {message.content}")

    @commands.command(help= "unloads and loads different cogs to keep the bot up during development")
    @commands.check(custom.isItme)
    async def reload(self, ctx, extension):
        self.client.unload_extension(f'cogs.{extension}')
        self.client.load_extension(f'cogs.{extension}')
        await ctx.send(f'[{extension}] has been unloaded and reloaded')

    @commands.command()
    @commands.check(custom.isItme)
    async def dump(self, ctx, dbName):
        await ctx.send(file=discord.File(f'cogs/Databases/{dbName}.json'))

    @commands.command(help= "lists the emojis used by the bot")
    @commands.check(custom.isItme)
    async def listEmojis(self, ctx):
        formatted = json.dumps(emojiList, indent=4)
        embed = discord.Embed()
        embed.add_field(name="List of Emojis Used by the Bot", value=f'{formatted}', inline=True)
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(dev(client))
