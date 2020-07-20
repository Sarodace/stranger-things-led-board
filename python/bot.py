# LIBRARIES
import LED
import os
import discord
from discord.ext import commands

import re


# SETUP
client = commands.Bot(command_prefix = '.')

# VARIABLES
emojis = ("👍", "👎")
messageBacklog = []

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
        description = "This is a test: "
    )

    embed.add_field(name = "Messages Sent:", value = "Yoyo has received and seen xx messages", inline = False)
    embed.set_footer(text = "Footer")

    await ctx.send(embed=embed)

@client.command()
async def send_message(ctx, arg):
    # TODO: Check to see if message is alphanumeric, if not then return it and point out
    # what characters aren't allowed. Maybe even try to auto-recommend something?

    # TODO: Incorporate some kinda delay to ensure that I don't mispell anything

    # TODO: Incorporate an embed, so that I could see info like "expected message display
    # length", "message seen yet?"

    # TODO: Support for "emotions", flash the LEDs in a certain way to make the message
    # more meaningful

    outbound = arg.upper()

    # Format message
    if all(x.isalpha() or x.isspace() for x in arg):
        # Construct embed
        embed = discord.Embed(
            colour=discord.Colour.green(),
            title = "Outgoing Message (No Invalid Characters!)",
            description="This message can be sent as is!"
        )

        # Construct embed (more in-depth)
        embed.add_field(name = "You wrote:", value = arg, inline = False)
        embed.add_field(name = "Message to be sent:", value = outbound, inline = False)

    else:
        outbound = re.sub(r'[^A-Za-z0-9 ]+', '', outbound)

        embed = discord.Embed(
            colour=discord.Colour.gold(),
            title = "Outgoing Message (Contains Invalid Characters!)",
            description="This message has errors that must be resolved before being sent!"
        )

        # Construct embed (more in-depth)
        embed.add_field(name = "You wrote:", value = arg, inline = False)
        embed.add_field(name = "Suggested message to be sent:", value = outbound, inline = False)

    embed.set_footer(text = "React with 👍 or 👎 to continue.")

    # Send embed
    msg = await ctx.send(embed = embed)

    # Add 👍 and 👎 as reactions
    for item in emojis:
        await msg.add_reaction(item)

    # Check for response
    def check(reaction, user):
        return user == ctx.message.author and str(reaction.emoji) in emojis

    reaction, user = await client.wait_for('reaction_add', timeout = 60.0, check = check)

    # Send different embeds depending on which response was selected
    if (reaction.emoji == "👍"):
        # Eventually invoke flickering and that kinda stuff
        success_embed = discord.Embed(
            colour = discord.Colour.green(),
            title = "Message Sent!",
            description = "Message succesfully sent at XX:XX:XX"
        )

        success_embed.add_field(name = "Message contents:", value = outbound, inline = False)

        await msg.edit(embed = success_embed)
        messageBacklog.append(outbound)

    if (reaction.emoji == "👎"):
        failed_embed = discord.Embed(
            colour = discord.Colour.red(),
            title = "Message not sent!",
            description = "Message was not sent"
        )

        failed_embed.add_field(name = "Message contents:", value = arg, inline = False)

        await msg.edit(embed = failed_embed)

@client.command()
async def christmas(ctx):
    LED.displayChristmasLEDs()


# Move into a function to be triggered by push button
@client.command()
async def display_message(ctx):
    if len(messageBacklog) > 0:
        msg = messageBacklog.pop(0)
        await ctx.send("Sending the following message: " + msg)
        LED.deconstruct_message(msg)
    else:
        await ctx.send("There are currently no messages to send!")



client.run(os.environ['ST_LED_DISCORD_BOT_KEY'])

