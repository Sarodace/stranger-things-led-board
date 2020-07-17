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

    # Construct embed (briefly)
    embed = discord.Embed(
        colour=discord.Colour.light_grey(),
        title = "Outgoing Message",
        description="Double-check that the message is written exactly as you want it be sent!"
    )

    # Format message
    if all(x.isalpha() or x.isspace() for x in arg):
        outbound = arg.upper()
    else:
        outbound = "INVALID"
        warning = "Message contains invalid characters"

    # Construct embed (more in-depth) 
    embed.add_field(name="You wrote:", value=arg, inline=False)
    embed.add_field(name="Warnings:", value=warning, inline=False)
    embed.add_field(name="Message to be sent:", value=outbound, inline=False)

    embed.set_footer(text="React with 👍 or 👎 to continue.")

    # Send embed
    msg = await ctx.send(embed=embed)

    # Add 👍 and 👎 as reactions
    emojis = ("👍","👎")
    for item in emojis:
        await msg.add_reaction(item)

    # Check for response
    def check(reaction, user):
        return user == ctx.message.author and str(reaction.emoji) in emojis

    reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=check)

    # Send different embeds depending on which response was selected
    if (reaction.emoji == "👍"):
        # Eventually invoke flickering and that kinda stuff
        success_embed = discord.Embed(
            colour=discord.Colour.green(),
            title = "Message Sent!",
            description="Message succesfully sent at XX:XX:XX"
        )

        success_embed.add_field(name="Message contents:", value=outbound, inline=False)

        await msg.edit(embed = success_embed)

        LED.deconstructMessage(outbound)

    if (reaction.emoji == "👎"):
        failed_embed = discord.Embed(
            colour=discord.Colour.red(),
            title = "Message not sent!",
            description="Message was not sent"
        )

        failed_embed.add_field(name="Message contents:", value=arg, inline=False)

        await msg.edit(embed = failed_embed)

@client.command()
async def christmas(ctx):
    LED.displayChristmasLEDs()


client.run(os.environ['ST_LED_DISCORD_BOT_KEY'])

