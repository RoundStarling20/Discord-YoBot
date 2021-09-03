import discord
import requests
from custom import directoryPath
from custom import emojiList
from discord import message
from discord.ext import commands


class emoji(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(manage_emojis=True)
    async def steal(self, ctx, url: str, emojiName: str):
        response = requests.get(url)
        with open(directoryPath["tempPNG"], 'wb') as f:
            f.write(response.content)
        with open(directoryPath["tempPNG"], 'rb') as f:
            await ctx.guild.create_custom_emoji(name=emojiName, image=f.read(), reason=f'Created by {ctx.author}')
        await ctx.message.add_reaction(emojiList["confirmed"])

    @commands.command()
    @commands.has_permissions(manage_emojis=True)
    async def delete(self, ctx, emoji: discord.Emoji):
        await emoji.delete(reason=f'Deleted by {ctx.author}')
        await ctx.message.add_reaction(emojiList["confirmed"])

    @commands.command()
    @commands.has_permissions(manage_emojis=True)
    async def update(self, ctx, emoji: discord.Emoji, *, newName):
        await emoji.edit(name=newName, reason=f'Renamed by {ctx.author}')
        await ctx.message.add_reaction(emojiList["confirmed"])

    @commands.command()
    async def listEmojiCount(self, ctx):
        animated = 0
        nonAnimated = 0
        for i in range(len(ctx.guild.emojis)):
            if ctx.guild.emojis[i].animated == 1:
                animated += 1

        for i in range(len(ctx.guild.emojis)):
            if ctx.guild.emojis[i].animated == 0:
                nonAnimated += 1
    
        if (animated == ctx.guild.emoji_limit):
            await ctx.send("This server has no animated emoji slots open")
            await ctx.send(f"There are {ctx.guild.emoji_limit - nonAnimated} static emoji slots open")
        elif (nonAnimated == ctx.guild.emoji_limit):
            await ctx.send("This server has no static emoji slots open")
            await ctx.send(f"There are {ctx.guild.emoji_limit - animated} animated emoji slots open")
        else:
            await ctx.send(f"There are {ctx.guild.emoji_limit - nonAnimated} static emoji slots open")
            await ctx.send(f"There are {ctx.guild.emoji_limit - animated} animated emoji slots open")


def setup(client):
    client.add_cog(emoji(client))