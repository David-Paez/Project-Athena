import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
from tags import get_relevant_tags, age_guesser, ethnicity_guesser, isThisFood

bot = commands.Bot(command_prefix = "##")

@bot.event
async def on_ready():
    print("Ready to crush our enemies.")
    print("I have landed on " + bot.user.name)
    print("With the id: ")
    print(bot.user.id)

@bot.command()
async def greet(ctx):
    await ctx.send("Hello, do you require assistance?")

@bot.command()
async def add(ctx, a: int, b: int):
    await ctx.send(a+b)

@bot.command()
async def multiply(ctx, a: int, b: int):
    await ctx.send(a*b)

@bot.command()
async def how_old(ctx, user: discord.Member):
    await ctx.send("They've spent this long on this server: " + str(user.joined_at))

@bot.command()
async def defineImage(ctx, link: str):
    await ctx.send("From what I can see, this image has: " + ', '.join(get_relevant_tags(link)) + ".")

@bot.command()
async def guessMyAge(ctx, link: str):
    await ctx.send("Hmm you seem to be " + age_guesser(link) + " years old.")

@bot.command()
async def guessMyEthnicity(ctx, link: str):
    await ctx.send("Hmm you seem to be " + ethnicity_guesser(link) + ".")

@bot.command()
async def whoseHungryFor(ctx, link: str):
    await ctx.send("Well, the food I see is " + ", ".join(isThisFood(link)) + ".")

bot.run()
