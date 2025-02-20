try:
    from config import *
except:
    print("Unable to find config.py")
    exit()

from config import token
import discord, requests, json
from discord import app_commands
from discord.ext import commands
from datetime import datetime

tokischa22 = commands.Bot(command_prefix="!",
                    intents=discord.Intents.all(),
                        help_command=None)

@tokischa22.event
async def on_ready():
    # Bot presence
    await tokischa22.change_presence(activity=discord.Activity(type=discord.ActivityType.watching,
                                                                                         name="/claim"))
    print(f'Logged in as {tokischa22.user}')

    try:
        # Slash command
        synced = await tokischa22.tree.sync()
        print(f"Synced {len(synced)} commands")

        # Id of command /claim
        claim_command = next((cmd for cmd in await tokischa22.tree.fetch_commands() if cmd.name == "claim"), None)
        if claim_command:
            command_id = claim_command.id
            # Updating stupid description
            await bot_description(token, command_id)
            # print(f"Description updatezz: {command_id}")

    except Exception as e:
        print(e)
        
@tokischa22.tree.command(name="claim",
                   description="Claim your Active Developer Badge")
async def claim(interaction: discord.Interaction):
    now = datetime.now()
    formatted_date = now.strftime("%d %B %Y %H:%M:%S")
    seconds_ago = (now - now).total_seconds()  
    seconds_ago_text = f"{int(seconds_ago)} seconds ago"

    # embed
    fanny = discord.Embed(
        title="🚀 Command Ran Successfully",
        description=(
            "You have successfully executed the command to get the **Active Developer Badge!**\n\n"
            "After Discord processes the execution of the command, **you will be able** to claim the badge by pressing the button below. Please note that Discord may take up to **24 hours** to process your eligibility.\n\n"
            f"_You've first ran this command on **{formatted_date}**, **{seconds_ago_text}**._"
        ),
        color=discord.Color.gold())

    # button
    button = discord.ui.Button(

        label="⏳ Claim Badge",
            style=discord.ButtonStyle.link,
                url="https://discord.com/developers/active-developer"

    )

    view = discord.ui.View()
    view.add_item(button)
    await interaction.response.send_message(embed=fanny,
                                                view=view)

# 💫
async def bot_description(token, command_id):   
    url = "https://discord.com/api/v10/applications/@me"
    headers = {
        "Authorization": f"Bot {token}",
        "Content-Type": "application/json"
    }
    data = {
        "description": f"_**Use the command </claim:{command_id}> to claim your badge.**_"
    }
    response = requests.patch(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        print("Description updated ~~")
    else:
        print(f"~~ Failed to update description: {response.status_code} - {response.text}")

tokischa22.run(token)
