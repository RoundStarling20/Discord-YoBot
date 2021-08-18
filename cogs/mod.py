from os import name
import discord
from discord import message
from discord.ext import commands
import custom


class mod(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def kick(self, ctx, member: discord.Member = None, *, reason = None):
        if member != None:
            await member.kick(reason = reason)
            await ctx.send(f'Kicked {member.name}#{member.discriminator}')

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def ban(self, ctx, user: discord.abc.User, *, reason = None):
            await ctx.guild.ban(user)
            await ctx.send(f'Banned {user.name}#{user.discriminator}')

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unban(self, ctx, user: discord.abc.User):
        await ctx.guild.unban(user)
        await ctx.send(f'Unbanned {user.name}#{user.discriminator}')
                
    @commands.command(aliases=['haram'])
    @commands.check(custom.isItme)
    async def forbid(self, ctx, *, message):
        db = custom.get_db(filePath="cogs/Databases/database.json")
        if ':' in message:
            if message not in db["bannedEmojis"]:
                db["bannedEmojis"].append(message)
                custom.save_db(db, filePath="cogs/Databases/database.json")
                await ctx.message.add_reaction('<a:yes:820523959878418452>')
        elif message not in db["bannedWords"]:
            db["bannedWords"].append(message)
            custom.save_db(db, filePath="cogs/Databases/database.json")
            await ctx.message.add_reaction('<a:yes:820523959878418452>')

    @commands.command(aliases=['halal'])
    @commands.check(custom.isItme)
    async def unforbid(self, ctx, *, message):
        db = custom.get_db(filePath="cogs/Databases/database.json")
        if message in db["bannedWords"]:
            db["bannedWords"].remove(message)
            custom.save_db(db, filePath="cogs/Databases/database.json")
            await ctx.message.add_reaction('<a:yes:820523959878418452>')

    @commands.Cog.listener()
    async def on_message(self, message):
        db = custom.get_db(filePath="cogs/Databases/database.json")
        for x in range(0, len(db["bannedWords"])):
            if (db["bannedWords"][x] in message.content.lower() and not(custom.isItKing(message.author.id))):
                await message.add_reaction('<a:no:820524004594024459>')
                break

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount = 5):
        await ctx.channel.purge(limit = amount + 1)

    @commands.command()
    async def changePrefix(self, ctx, prefix):
        prefixes = custom.get_db(filePath="cogs/Databases/prefixes.json")
        prefixes[str(ctx.guild.id)] = prefix
        custom.save_db(db=prefixes, filePath='cogs/Databases/prefixes.json')
        await ctx.message.add_reaction('<a:yes:820523959878418452>')
    

def setup(client):
    client.add_cog(mod(client))