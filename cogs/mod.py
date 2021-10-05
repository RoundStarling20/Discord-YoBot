import custom
import discord
from custom import directoryPath
from custom import emojiList
from discord import message
from discord.ext import commands


class mod(commands.Cog, name="Moderator Tools", description="A set of tools use to moderate a server"):
    def __init__(self, client):
        self.client = client

    @commands.command(help= "kicks a member from the server")
    @commands.has_permissions(administrator=True)
    async def kick(self, ctx, member: discord.Member = None, *, reason = None):
        if member != None:
            await member.kick(reason = reason)
            await ctx.send(f'Kicked {member.name}#{member.discriminator}')

    @commands.command(help= "bans a member from the server")
    @commands.has_permissions(administrator=True)
    async def ban(self, ctx, user: discord.abc.User, *, reason = None):
            await ctx.guild.ban(user)
            await ctx.send(f'Banned {user.name}#{user.discriminator}')

    @commands.command(help= "unbanns a member from the server")
    @commands.has_permissions(administrator=True)
    async def unban(self, ctx, user: discord.abc.User):
        await ctx.guild.unban(user)
        await ctx.send(f'Unbanned {user.name}#{user.discriminator}')

    @commands.command(aliases=['haram'],help= "adds word restrictions")
    @commands.check(custom.isItme)
    async def forbid(self, ctx, *, message):
        db = custom.get_db(filePath=directoryPath["badWordDB"])
        if message not in db["bannedWords"]:
            db["bannedWords"].append(message)
            custom.save_db(db, filePath=directoryPath["badWordDB"])
            await ctx.message.add_reaction(emojiList["confirmed"])

    @commands.command(aliases=['halal'],help= "removes word restrictions")
    @commands.check(custom.isItme)
    async def unforbid(self, ctx, *, message):
        db = custom.get_db(filePath=directoryPath["badWordDB"])
        if message in db["bannedWords"]:
            db["bannedWords"].remove(message)
            custom.save_db(db, filePath=directoryPath["badWordDB"])
            await ctx.message.add_reaction(emojiList["confirmed"])

    @commands.Cog.listener()
    async def on_message(self, message):
        db = custom.get_db(filePath=directoryPath["badWordDB"])
        for x in range(0, len(db["bannedWords"])):
            if (db["bannedWords"][x] in message.content.lower() and not(custom.isItKing(message.author.id))):
                await message.add_reaction(emojiList["failed"])
                break

    @commands.command(help= "purges messages from chat")
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount = 5):
        await ctx.channel.purge(limit = amount + 1)

    @commands.command(help= "changes the server prefix default = .")
    @commands.has_permissions(administrator=True)
    async def changePrefix(self, ctx, prefix):
        prefixes = custom.get_db(filePath=directoryPath["serverPrefixdb"])
        prefixes[str(ctx.guild.id)] = prefix
        custom.save_db(db=prefixes, filePath=directoryPath["serverPrefixdb"])
        await ctx.message.add_reaction(emojiList["confirmed"])

    @commands.command(help= "sends a dm from the bot to a member")
    async def dm(self, ctx, member: discord.Member, *, message):
        await member.send(message)

def setup(client):
    client.add_cog(mod(client))
