from asyncio.windows_events import NULL
import discord
import random
from discord.ext import commands
from discord.flags import Intents

client = commands.Bot(command_prefix = '.', intents=Intents.all())

@client.event
async def on_ready():
    print("Bot is ready.")

@client.event
async def on_member_join(member):
    print(f"{member} has joined [{member.guild.name}: {member.guild.id}].")
    await member.guild.system_channel.send(file=discord.File('bababoey.gif'))
    await member.guild.system_channel.send(f'Welcome! <@{member.id}>')

@client.event
async def on_member_remove(member):
    print(f"{member} has left [{member.guild.name}: {member.guild.id}].")

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, discord.ext.commands.CommandNotFound):
        await ctx.send("Thats not a command doo doo fart!")

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command()
async def dabMeUp(ctx):
    await ctx.send(file=discord.File('Dab_me_up.png'))

@client.command()
async def aight(ctx):
    await ctx.send(file=discord.File('ight.jpg'))
    await ctx.send(file=discord.File('Dab.png'))

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
    await ctx.send(file=discord.File('desp.png'))

@client.command()
async def rs(ctx):
    message = random.choice(["RoundStarling20 is so cool", "RoundStarling20 is so smart", "RoundStarling20 is the best programmer ever", "RoundStarling20 is so bad <:SHEESH:870453487899652106>", "RoundStarling20 is cute fr fr <:blushflush:833362636640878673>"])
    webhook = await ctx.channel.create_webhook(name = "RSHook" , reason = "For RS's bot")
    await webhook.send(content = message, username = ctx.author.display_name, avatar_url = ctx.author.avatar_url)
    await webhook.delete()

@client.command()
async def hammie(ctx):
    await ctx.send(file=discord.File('stinky.gif'))

@client.command()
async def clear(ctx, amount = 5):
    await ctx.channel.purge(limit = amount + 1)

@client.command()
async def commands(ctx):
    rsBotCommands = "```.ping: returns the latency in ms\n.clear <n>: purges n messages```"
    await ctx.send(content = rsBotCommands)

@client.command()
async def av(ctx, member: discord.Member = None):
    if member is None:
        member = ctx.author
    await ctx.send(member.avatar_url)

fp = open("token.txt", 'r')
client.run(f"{fp.read()}")
fp.close()

#rotate images