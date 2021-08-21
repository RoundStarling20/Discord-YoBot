import random

import discord
from discord.ext import commands


class fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def jail(self, ctx):
        await ctx.send(file=discord.File('cogs/Images/jail.png'))

    @commands.command()
    async def tu(self, ctx):
        await ctx.send('<:tumadre:833742332334702592>')

    @commands.command()
    async def dabMeUp(self, ctx):
        await ctx.send(file=discord.File('cogs/Images/Dab_me_up.png'))

    @commands.command()
    async def aight(self, ctx):
        await ctx.send(file=discord.File('cogs/Images/ight.jpg'))
        await ctx.send(file=discord.File('cogs/Images/Dab.png'))

    @commands.command()
    async def creepy(self, ctx):
        await ctx.send('<:yeahboi:828988729095094352>')

    @commands.command()
    async def guhnaw(self, ctx):
        await ctx.send('<:blushflush:833362636640878673>')

    @commands.command()
    async def acco(self, ctx):
        await ctx.send('<:blobcomf:864661919901679616>')

    @commands.command()
    async def desp(self, ctx):
        await ctx.send(file=discord.File('cogs/Images/desp.png'))

    @commands.command()
    async def rs(self, ctx):
        message = random.choice(["RoundStarling20 is so cool", "RoundStarling20 is so smart", "RoundStarling20 is the best programmer ever", "RoundStarling20 is so bad <:SHEESH:870453487899652106>", "RoundStarling20 is cute fr fr <:blushflush:833362636640878673>"])
        webhook = await ctx.channel.create_webhook(name="RSHook" , reason="For RS's bot")
        await webhook.send(content = message, username = ctx.author.display_name, avatar_url = ctx.author.avatar_url)
        await webhook.delete()

    @commands.command()
    async def hammie(self, ctx):
        await ctx.send(file=discord.File('cogs/Images/stinky.gif'))

    @commands.command()
    async def stewart(self, ctx):
        await ctx.send("That aint my name cuh")

    @commands.command()
    async def pickupLine(self, ctx):
        with open("cogs/Databases/pickUpLines.txt") as fp:
            pickUpLines = fp.read().split("\n")
        await ctx.send(pickUpLines[random.randint(0, len(pickUpLines))])


def setup(client):
    client.add_cog(fun(client))