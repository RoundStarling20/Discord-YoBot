import discord
import requests
from custom import directoryPath
from discord import message
from discord.ext import commands


class emoji(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(manage_emojis=True)
    async def steal(self, ctx, url: str, emojiName: str):
        if (len(ctx.guild.emojis) == ctx.guild.emoji_limit):
            await ctx.send("This server has the max number of emojis")
        else:
            response = requests.get(url)
            with open(directoryPath["tempPNG"], 'wb') as f:
                f.write(response.content)
            with open(directoryPath["tempPNG"], 'rb') as f:
                await ctx.guild.create_custom_emoji(name=emojiName, image=f.read(), reason=f'Created by {ctx.author}')
            await ctx.message.add_reaction('<a:yes:820523959878418452>')

    @commands.command()
    @commands.has_permissions(manage_emojis=True)
    async def delete(self, ctx, emoji: discord.Emoji):
        await emoji.delete(reason=f'Deleted by {ctx.author}')
        await ctx.message.add_reaction('<a:yes:820523959878418452>')

    @commands.command()
    @commands.has_permissions(manage_emojis=True)
    async def update(self, ctx, emoji: discord.Emoji, *, newName):
        await emoji.edit(name=newName, reason=f'Renamed by {ctx.author}')
        await ctx.message.add_reaction('<a:yes:820523959878418452>')


def setup(client):
    client.add_cog(emoji(client))