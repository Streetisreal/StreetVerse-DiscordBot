import discord
from discord.ext import commands
import datetime

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.presences = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged on as {bot.user}!')

@bot.command()
async def nes(ctx):
    await ctx.send("https://www.youtube.com/shorts/_FcnrS_gdus")

@bot.command()
async def edrinvite(ctx):
    await ctx.send("https://discord.gg/tvK3TrAJFJ")

@bot.command()
async def latest(ctx):
    await ctx.send("https://github.com/Streetisreal/Project-StreetVerse/commit/750adad63a97f7d77e7347219ebe06f14bee78b0")

@bot.command()
async def info(ctx):
    await ctx.send("StreetVerse is a service that lets you communicate with other players from around the world. It is accessible via the web. StreetVerse is still developing so stay tuned for more updates!")

@bot.command()
async def checkonline(ctx):
    online = 0
    offline = 0
    for member in ctx.guild.members:
        if str(member.status) == "online":
            online += 1
        elif str(member.status) == "offline":
            offline += 1
    await ctx.send(f"Online: {online} 🟢 | Offline: {offline} 🔴")

@bot.command()
async def mute(ctx, member: discord.Member, duration: int = 300):
    await member.timeout(discord.utils.utcnow() + datetime.timedelta(seconds=duration))
    await ctx.send(f"{member.mention} has been muted for {duration} seconds.")

@bot.command()
async def teedle(ctx):
    await ctx.send("https://cdn.teedleyt.com/teedle.mp4")
bot.run('Enter Token here')
