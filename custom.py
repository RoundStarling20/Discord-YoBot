import discord
from discord.ext import commands
import json


def isItme(ctx):
    return ctx.message.author.id == 220327217312432129

def get_db():
    with open("database\database.json") as file:
        return json.load(file)

def save_db(db):
    with open("database\database.json", "w") as file:
        json.dump(db, file)