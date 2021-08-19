import os
import random

import discord
from discord import file
from discord.ext import commands
from discord.flags import Intents

import custom
from custom import directoryPath

client = commands.Bot(command_prefix = custom.getPrefix)

@client.event
async def on_guild_join(guild):
    prefixes = custom.get_db(filePath=directoryPath["serverPrefixdb"])
    prefixes[str(guild.id)] = '.'
    custom.save_db(db=prefixes, filePath=directoryPath["serverPrefixdb"])

@client.event
async def on_guild_remove(guild):
    prefixes = custom.get_db(filePath=directoryPath["serverPrefixdb"])
    prefixes.pop(str(guild.id))
    custom.save_db(db=prefixes, filePath=directoryPath["serverPrefixdb"])

@client.event
async def on_member_join(member):
    await member.guild.system_channel.send(file=discord.File('Images/bababoey.gif'))
    await member.guild.system_channel.send(f'Welcome <@{member.id}>!')

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, discord.ext.commands.CommandNotFound):
        if custom.isItme(ctx):
            await ctx.send("Thats not a command my king!")
        else:
            await ctx.send("Thats not a command doo doo fart!")

@client.command()
async def dabMeUp(ctx):
    await ctx.send(file=discord.File('Images/Dab_me_up.png'))

@client.command()
async def aight(ctx):
    await ctx.send(file=discord.File('Images/ight.jpg'))
    await ctx.send(file=discord.File('Images/Dab.png'))

@client.command()
async def tu(ctx):
    await ctx.send('<:tumadre:833742332334702592>')

@client.command()
async def creepy(ctx):
    await ctx.send('<:yeahboi:828988729095094352>')

@client.command()
async def guhnaw(ctx):
    await ctx.send('<:blushflush:833362636640878673>')

@client.command()
async def acco(ctx):
    await ctx.send('<:blobcomf:864661919901679616>')

@client.command()
async def desp(ctx):
    await ctx.send(file=discord.File('Images/desp.png'))

@client.command()
async def rs(ctx):
    message = random.choice(["RoundStarling20 is so cool", "RoundStarling20 is so smart", "RoundStarling20 is the best programmer ever", "RoundStarling20 is so bad <:SHEESH:870453487899652106>", "RoundStarling20 is cute fr fr <:blushflush:833362636640878673>"])
    webhook = await ctx.channel.create_webhook(name="RSHook" , reason="For RS's bot")
    await webhook.send(content = message, username = ctx.author.display_name, avatar_url = ctx.author.avatar_url)
    await webhook.delete()

@client.command()
async def hammie(ctx):
    await ctx.send(file=discord.File('Images/stinky.gif'))

@client.command()
async def stewart(ctx):
    await ctx.send("That aint my name cuh")

@client.command()
async def av(ctx, member: discord.Member = None):
    if member is None:
        member = ctx.author
    embed = discord.Embed(
        title = f'{member.name}',
        url = f'{member.avatar_url}'
    )
    embed.set_image(url=member.avatar_url)
    await ctx.send(embed=embed)

@client.command()
async def jail(ctx):
    await ctx.send(file=discord.File('Images/jail.png'))

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f'cogs.{filename[:-3]}')


with open("token.txt", 'r', encoding="utf-8") as fp:
    client.run(f"{fp.read()}")

#rotate images
