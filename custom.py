import discord
from discord.ext import commands
import json


def isItme(ctx):
    return ctx.message.author.id == 220327217312432129

def get_db():
    with open("cogs\database.json", "r") as file:
        print('opened')
        return json.load(file)

def save_db(db):
    print("you have saved the database")
    with open("cogs\database.json", "w") as file:
        json.dump(db, file)