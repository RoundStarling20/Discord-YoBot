import discord
from discord.ext import commands

class TestCog(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def clear(self, ctx, amount = 5):
        await ctx.channel.purge(limit = amount + 1)
        
#ban and kick event

def setup(client):
    client.add_cog(TestCog(client))