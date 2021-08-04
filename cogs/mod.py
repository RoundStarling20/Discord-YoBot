import discord
from discord.ext import commands
import custom


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
    async def ban(self, ctx, member: discord.Member = None, *, reason = None):
        if member != None:
            await member.ban(reason = reason)
            await ctx.send(f'Banned {member.name}#{member.discriminator}')

    #@commands.command()
    #@commands.check(custom.isItme)
    #async def unban(self, ctx, *, member): 
    #    bannedUsers = await ctx.guild.bans()
    #    member_name, member_discriminator = member.split('#')
    #    for ban_entry in bannedUsers:
    #        user = ban_entry.user
    #        if (user.name, user.discriminator) == (member_name, member_discriminator):
    #            await ctx.guild.unban(user)
    #            await ctx.send(f'Unbanned {user.name}#{user.discriminator}')
    #            return
    #        elif str(user.id) == member:
    #            await ctx.guild.unban(user)
    #            await ctx.send(f'Unbanned {user.name}#{user.discriminator}')
    #            return
                
    @commands.command()
    @commands.check(custom.isItme)
    async def forbid(self, ctx, *, message):
        db = custom.get_db()
        if ':' in message:
            if message not in db["bannedEmojis"]:
                db["bannedEmojis"].append(message)
                custom.save_db(db)
                await ctx.send(f'{[message]} has been forbidden')
        elif message not in db["bannedWords"]:
            db["bannedWords"].append(message)
            custom.save_db(db)
            await ctx.send(f'{[message]} has been forbidden')

    @commands.command()
    @commands.check(custom.isItme)
    async def unforbid(self, ctx, *, message):
        db = custom.get_db()
        if ':' in message:
            if message in db["bannedEmojis"]:
                db["bannedEmojis"].remove(message)
                custom.save_db(db)
                await ctx.send(f'{[message]} has been unforbidden')
        elif message in db["bannedWords"]:
            db["bannedWords"].remove(message)
            custom.save_db(db)
            await ctx.send(f'{[message]} has been unforbidden')

    @commands.Cog.listener()
    async def on_message(self, message):
        db = custom.get_db()
    #    phraseSaid = message.content.lower().split()
    #    for x in range(0, len(phraseSaid)):
    #        if phraseSaid[x] in db["bannedEmojis"] + db["bannedWords"]:
    #            await message.add_reaction('<a:no:820524004594024459>')
    #            break
        for x in range(0, len(db["bannedWords"])):
            if db["bannedWords"][x] in message.content.lower():
                await message.add_reaction('<a:no:820524004594024459>')
                break

    @commands.command()
    async def clear(self, ctx, amount = 5):
        await ctx.channel.purge(limit = amount + 1)
        
#ban and kick event

def setup(client):
    client.add_cog(TestCog(client))