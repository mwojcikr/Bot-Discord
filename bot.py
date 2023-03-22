import discord
from discord.ext import commands
import dialogue
from quoteparser import get_quote,parse_good_reads
from youtube import get_new_urls
from dotenv import load_dotenv
import os

def get_response(user_message):
    return dialogue.handle_response(user_message)


def configure():
    load_dotenv()
    parse_good_reads("aristotle.txt","w","Aristotle")
    parse_good_reads("aurelius.txt","a","Marcus Aurelius")
    parse_good_reads("plato.txt","a","Plato")


def run_bot():

    configure()
    TOKEN = os.getenv('DISCORD_TOKEN')
    intents = discord.Intents(messages=True,guilds = True)
    client = commands.Bot(intents=intents,command_prefix= '!')
    

    async def youtube():
        ytchannel = client.get_channel(int(os.getenv('DICORD_CHANNEL_ID_YOUTUBE')))
        vids = get_new_urls()
        if len(vids) == 0:
            await ytchannel.send("No new videos :(")
        else:
            for url in vids:
                await ytchannel.send(url)


    @client.command()
    async def update(ctx):
        await youtube()
        fbchannel = client.get_channel(int(os.getenv('DICORD_CHANNEL_ID_FACEBOOK')))
        await fbchannel.send("Not implemented yet")

    #updates only yt vids
    @client.command()
    async def getvids(ctx):
        await youtube()

    #updates only fb 
    @client.command()
    async def facebook(ctx):
        chan = client.get_channel(int(os.getenv('DICORD_CHANNEL_ID_FACEBOOK')))
        await chan.send("Page Public Content Access required")

    #sends a quote to quote channel
    @client.command()
    async def getquote(ctx):
        chan = client.get_channel(int(os.getenv('DICORD_CHANNEL_ID_QUOTES')))
        await chan.send(get_quote())

    @client.command()
    async def addauthor(ctx):
        author = ctx.message.content
        await ctx.send(f"your author is: {author}")


    @client.event
    async def on_ready():
        print(f"{client.user} is running as well")
        main_channel = client.get_channel(int(os.getenv('DISCORD_CHANNEL_ID_MAIN')))
        await main_channel.send("Hi there! I am ready! If you need to know something just say: help ")

    @client.event
    async def on_message(message):

        await client.process_commands(message)     #activates client.command

        if message.author == client.user or message.content[0] == '!': #don't respond to commands or to yourself
            return
        
        if message.content in ['getquote','update','getvids','facebook']:
            await message.channel.send("You need to begin a command with a  !  prefix")

        elif get_response(message.content) != '':
            await message.channel.send(get_response(message.content))
        else:
            await message.channel.send(f"Received: {message.content}")
        
        #await message.author.send(f"Received: {message.content}") sends an info to priv


    client.run(TOKEN)

run_bot()