from os import name
import discord
from discord import message
from discord.ext import commands
import custom

from PIL import Image
import requests
from io import BytesIO

class TestCog(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.check(custom.isItme)
    async def kick(self, ctx, member: discord.Member = None, *, reason = None):
        if member != None:
            await member.kick(reason = reason)
            await ctx.send(f'Kicked {member.name}#{member.discriminator}')

    @commands.command()
    @commands.check(custom.isItme)
    async def ban(self, ctx, user: discord.abc.User, *, reason = None):
            await ctx.guild.ban(user)
            await ctx.send(f'Banned {user.name}#{user.discriminator} ')

    @commands.command()
    @commands.check(custom.isItme)
    async def unban(self, ctx, user: discord.abc.User):
        await ctx.guild.unban(user)
        await ctx.send(f'Unbanned {user.name}#{user.discriminator} ')
                
    @commands.command()
    @commands.check(custom.isItme)
    async def forbid(self, ctx, *, message):
        db = custom.get_db()
        if ':' in message:
            if message not in db["bannedEmojis"]:
                db["bannedEmojis"].append(message)
                custom.save_db(db)
                await ctx.message.add_reaction('<a:yes:820523959878418452>')
        elif message not in db["bannedWords"]:
            db["bannedWords"].append(message)
            custom.save_db(db)
            await ctx.message.add_reaction('<a:yes:820523959878418452>')

    @commands.command()
    @commands.check(custom.isItme)
    async def unforbid(self, ctx, *, message):
        db = custom.get_db()
        if message in db["bannedWords"]:
            db["bannedWords"].remove(message)
            custom.save_db(db)
            await ctx.message.add_reaction('<a:yes:820523959878418452>')

    @commands.Cog.listener()
    async def on_message(self, message):
        db = custom.get_db()
        for x in range(0, len(db["bannedWords"])):
            if (db["bannedWords"][x] in message.content.lower() and not(custom.isItKing(message.author.id))):
                await message.add_reaction('<a:no:820524004594024459>')
                break

    @commands.command()
    @commands.check(custom.isItme)
    async def clear(self, ctx, amount = 5):
        await ctx.channel.purge(limit = amount + 1)

    @commands.command()
    @commands.check(custom.isItme)
    async def steal(self, ctx, url: str, emojiName: str):
        if (len(ctx.guild.emojis) == ctx.guild.emoji_limit):
            await ctx.send("This server has than the max number of emojis")
        else:
            response = requests.get(url)
            with open('cogs/tempFiles/temp.png', 'wb') as f:
                f.write(response.content)
            with open('cogs/tempFiles/temp.png', 'rb') as f:
                await ctx.guild.create_custom_emoji(name=emojiName, image=f.read())
            await ctx.message.add_reaction('<a:yes:820523959878418452>')


def setup(client):
    client.add_cog(TestCog(client))