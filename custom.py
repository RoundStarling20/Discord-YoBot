import discord
from discord.ext import commands
import json


def isItme(ctx):
    return ctx.message.author.id == 220327217312432129

def isItKing(author):
    king = {220327217312432129, 870467770846945290}
    return (author in king)

def get_db():
    with open("cogs\database.json", "r") as file:
        return json.load(file)

def save_db(db):
    with open("cogs\database.json", "w") as file:
        json.dump(db, file)