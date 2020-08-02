## LIBRARIES
import LED
import os
import discord
from discord.ext import commands
import re


## SETUP
client = commands.Bot(command_prefix = '.')


## VARIABLES
emojis = ("👍", "👎")
messageBacklog = []


## DISCORD EVENTS
# Verifies that bot actually turns on properly
@client.event
async def on_ready():
    print('Bot is ready')
    """
    Eventually turn this into something like "@client.event" so that I just have a 
    dashboard that gets updated every so often with info like "messages sent", "uptime",
    and other relevant stuff.
    """


## DISCORD COMMANDS
# Function used to test embeds, will probably be removed soon. 
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

# Function used to send messages to the Raspberry Pi
@client.command()
async def send_message(ctx, arg):
    # TODO: Incorporate some kinda delay to ensure that I don't mispell anything

    # TODO: Support for "emotions", flash the LEDs in a certain way to make the message
    # more meaningful

    # Make sure that message to be displayed is capitalized 
    outbound = arg.upper()

    # Check if message to be sent doesn't contain invalid characters (Numbers, Punctuation, etc..)
    if all(letter.isalpha() or letter.isspace() for letter in arg):
        # Construct embed
        embed = discord.Embed(
            colour = discord.Colour.green(),
            title = "Outgoing Message (No Invalid Characters!)",
            description = "This message can be sent as is!"
        )

        # Construct embed (more in-depth)
        embed.add_field(name = "You wrote:", value = arg, inline = False)
        embed.add_field(name = "Message to be sent:", value = outbound, inline = False)
    else:
        # Remove all non-Alphabetical characters except for spaces
        outbound = re.sub(r'[^A-Za-z0-9 ]+', '', outbound)

        # Construct embed
        embed = discord.Embed(
            colour=discord.Colour.gold(),
            title = "Outgoing Message (Contains Invalid Characters!)",
            description="This message has errors that must be resolved before being sent!"
        )

        # Construct embed (more in-depth)
        embed.add_field(name = "You wrote:", value = arg, inline = False)
        embed.add_field(name = "Suggested message to be sent:", value = outbound, inline = False)

    # Finish constructing the embed
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
        # Construct embed
        success_embed = discord.Embed(
            colour = discord.Colour.green(),
            title = "Message Sent!",
            description = "Message succesfully sent at XX:XX:XX"
        )

        # Construct embed (more in-depth)
        success_embed.add_field(name = "Message contents:", value = outbound, inline = False)

        # Store message to be displayed
        await msg.edit(embed = success_embed)
        messageBacklog.append(outbound)

    if (reaction.emoji == "👎"):
        # Construct embed
        failed_embed = discord.Embed(
            colour = discord.Colour.red(),
            title = "Message not sent!",
            description = "Message was not sent"
        )

        # Construct embed (more in-depth)
        failed_embed.add_field(name = "Message contents:", value = arg, inline = False)

        await msg.edit(embed = failed_embed)

# Function used to shine all the LEDs from A to Z
@client.command()
async def christmas(ctx):
    LED.displayChristmasLEDs()

# Function used to display the currently stored message, will eventually be triggered by push button
@client.command()
async def display_message(ctx):
    # Check if there's any stored messages
    if len(messageBacklog) > 0:
        # Remove message from backlog
        msg = messageBacklog.pop(0)
        
        # Send message
        await ctx.send("Sending the following message: " + msg)
        LED.deconstruct_message(msg)
    else:
        await ctx.send("There are currently no messages to send!")

client.run(os.environ['ST_LED_DISCORD_BOT_KEY'])