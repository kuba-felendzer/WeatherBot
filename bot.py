import discord
from discord.ext import commands
import asyncio 

import random

import python_weather

token = open("data/TOKEN", "r").read()

bot = commands.Bot(command_prefix="??")

@bot.event
async def on_ready():
    print("------------\nBot Ready!\n------------")

@bot.command()
async def weather(ctx):
    client = python_weather.Client(format=python_weather.IMPERIAL)

    weather = await client.find("Dallas")

    c_temp = weather.current.temperature

    embed = discord.Embed(title="__The Weather is as such:__", color=discord.Color.blue())
    embed.set_author(name="Weatherman (Kuba's illegitimate grandson)", icon_url="https://thumbor.forbes.com/thumbor/fit-in/416x416/filters%3Aformat%28jpg%29/https%3A%2F%2Fspecials-images.forbesimg.com%2Fimageserve%2F5ed00f17d4a99d0006d2e738%2F0x0.jpg%3Fbackground%3D000000%26cropX1%3D154%26cropX2%3D4820%26cropY1%3D651%26cropY2%3D5314")
    
    embed.add_field(name="Current Forecast:", value=f"I think it's like {c_temp} bro idk")

    f = weather.forecasts

    del f[0]

    forecast = f[1]
    embed.add_field(name=f"Today", value=f"It'll be {forecast.sky_text} and it'll be between **{forecast.low}°** and **{forecast.high}°** with a rain chance of *{forecast.precip}%*", inline=False)
    
    forecast = f[2]
    embed.add_field(name=f"Tomorrow", value=f"It'll be {forecast.sky_text} and it'll be between **{forecast.low}°** and **{forecast.high}°** with a rain chance of *{forecast.precip}%*", inline=False)

    forecast = f[3]
    embed.add_field(name=f"Overmorrow", value=f"It'll be {forecast.sky_text} and it'll be between **{forecast.low}°** and **{forecast.high}°** with a rain chance of *{forecast.precip}%*", inline=False)

    embed.set_footer(text="Tʜɪs ʜᴀs ᴄᴀᴜsᴇᴅ ᴍᴇ sᴏ ᴍᴜᴄʜ ᴘᴀɪɴ ᴀɴᴅ ɪᴛ's ᴅɪsᴛʀᴀᴄᴛᴇᴅ ᴍᴇ ғʀᴏᴍ Kᴀᴛᴇ sɪᴍᴘɪɴɢ ᴛɪᴍᴇ sᴏ ᴘʟᴇᴀsᴇ ᴇɴᴊᴏʏ ɪᴛ")
    
    await ctx.send(embed=embed)
    
    await client.close()

@bot.command()
async def whatdoido(ctx):
    things_to_do = ["go outside lol", 
                    "practice", 
                    "uninstall league", 
                    "uninstall dota", 
                    "bump donda", 
                    "read a book once in your life dickshit", 
                    "make fun of zach hall", 
                    "finish your hw", 
                    "contemplate the impermanence of marching band, time, and our own existence", 
                    "cry.", 
                    "add something new to the list",
                    "nothing",
                    "throw a lifesaver at a duck (don't)",
                    "learn to program bots so kuba is out of a job",
                    "watch some yt or smth what do kids even do these days",
                    "just think about it",
                    "¯\_(ツ)_/¯",
                    ":)",
                    "xD rip bozo mf can't even figure it out himself lmfao",
                    "<@498969025733197844>",
                    "<@446437469424975882>",
                    "find kuba's bell cover"
                    ]

    await ctx.send(random.choice(things_to_do))

@bot.command()
async def poll(ctx, *, question):
    qmark = "?" if (question[-1] != "?") else ""
    msg = await ctx.send(f"**{question}{qmark}**")
    await msg.add_reaction("👍") # thumbs up emoji
    await msg.add_reaction("👎") # thumbs down emoji

bot.run(token)