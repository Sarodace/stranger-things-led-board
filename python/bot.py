# LIBRARIES
import LED
import os
import discord
from discord.ext import commands

# SETUP
client = commands.Bot(command_prefix = '.')

# DISCORD COMMANDS + EVENTS
@client.event
async def on_ready():
    print('Bot is ready')

"""
Eventually turn this into something like "@client.event" so that I just have a 
dashboard that gets updated every so often with info like "messages sent", "uptime",
and other relevant stuff.
"""
@client.command()
async def embedt(ctx):

    embed = discord.Embed(
        colour=discord.Colour.blue(),
        title = "Dashboard",
        description="This is a test: "
    )

    embed.add_field(name="Messages Sent:", value="Yoyo has received and seen xx messages", inline=False)
    embed.set_footer(text="Footer")

    await ctx.send(embed=embed)

@client.command()
async def send_message(ctx, arg):
    # Check to see if message is alphanumeric, if not then return it and point out
    # what characters aren't allowed. Maybe even try to auto-recommend something?

    # Incorporate some kinda delay to ensure that I don't mispell anything

    # Incorporate an embed, so that I could see info like "expected message display
    # length", "message seen yet?"

    # Support for "emotions", flash the LEDs in a certain way to make the message
    # more meaningful
    embed = discord.Embed(
        colour=discord.Colour.blue(),
        title = "Outgoing Message",
        description="Double-check that the message is written exactly as you want it be sent!"
    )

    embed.add_field(name="You wrote:", value=arg, inline=False)
    embed.set_footer(text="React with 👍 or 👎 to continue.")

    msg = await ctx.send(embed=embed)
    emojis = ("👍","👎")
    for item in emojis:
        await msg.add_reaction(item)

    LED.deconstructMessage(arg)

@client.command()
async def christmas(ctx):
    LED.displayChristmasLEDs()


"""
Will have a "main.py" file that includes "bot.py" and "LED.py". When I execute that main
file, not much will happen with the LED board but I'll be able to send commands through
discord to activate pre-programmed behaviors!
"""

client.run(os.environ['ST_LED_DISCORD_BOT_KEY'])

