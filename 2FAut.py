import os
import discord
from discord.ext import commands, tasks
import random
import hashlib

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='/', intents=intents)

TARGET_USER_ID = os.getenv("DISCORD_ID")  # Replace with real ID
Bot_ID = os.getenv("DISCORD_BOT_ID")
auty = None

@tasks.loop(seconds=60)  # For testing: every 60 seconds
async def send_auty_update():
    global auty
    print("Running auty update task...")
    auty = ''.join(random.choices('0123456789ABCDEF', k=6))
    print(f"Generated auty: {auty}")

    try:
        user = await bot.fetch_user(TARGET_USER_ID)
        await user.send(f"🔁 New auty: `{auty}`")
        print(f"✅ Sent auty to {user}")
        auty_hash = hashlib.md5(auty.encode()).hexdigest()
        with open("auty.txt", "w") as f:
            f.write(auty_hash)
    except discord.Forbidden:
        print(f"❌ Cannot DM user {TARGET_USER_ID}")
    except Exception as e:
        print(f"⚠️ Unexpected error: {e}")

@bot.event
async def on_ready():
    print(f'Bot connected as {bot.user}')
    send_auty_update.start()

bot.run(Bot_ID) #Bot id
