import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command(name='melding', help='Maak een melding en stuur het naar de politie')
async def melding(ctx, *, melding: str):
    politie_channel = discord.utils.get(ctx.guild.text_channels, name='politie')
    if politie_channel:
        await politie_channel.send(f'Nieuwe melding van {ctx.author.mention}: {melding}')
        await ctx.send('Je melding is verzonden naar de politie!')
    else:
        await ctx.send('Politie kanaal niet gevonden.')

bot.run(TOKEN)