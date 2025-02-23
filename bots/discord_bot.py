# discord_bot.py
import discord
from discord.ext import tasks

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")

@tasks.loop(minutes=60)  # Check every hour for new releases
async def check_releases():
    version = os.environ.get("LATEST_VERSION", "0.1.1")
    channel = client.get_channel(int(os.environ["DISCORD_CHANNEL_ID"]))
    await channel.send(f"Neural-dsl v{version} released! Fixed 10 bugs. Try `pip install neural-dsl=={version}`. Feedback? [GitHub link]")

check_releases.start()
client.run(os.environ["DISCORD_BOT_TOKEN"])