import os

from discord import Intents, utils, Interaction
from dotenv import load_dotenv
from discord.ext import commands
from Cogs import moderation, poll, invitation_guild

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
INTENTS = Intents.all()

bot = commands.Bot(command_prefix="!", intents=INTENTS)

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord !')
    await bot.add_cog(moderation.Moderation(bot))
    await bot.add_cog(poll.Poll(bot))
    await bot.add_cog(invitation_guild.Invitation(bot))
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)

@bot.event
async def on_member_join(member):
    guild = member.guild
    channel = utils.get(guild.channels, name="bienvenue")

    if channel and channel.permissions_for(guild.me).send_messages:
        await channel.send(f"Welcome {member.mention} to the server {guild.name}")

@bot.event
async def on_member_remove(member):
    guild = member.guild
    channel = utils.get(guild.channels, name="bienvenue")
    
    if channel and channel.permissions_for(guild.me).send_messages:
        await channel.send(f"{member.mention} has left the server")

@bot.tree.command(name="get_user_pp", description="Get the profile picture of a member")
async def get_profile_picture(interaction: Interaction, user:str):
    member = interaction.guild.get_member_named(user)

    if member is None:
        await interaction.response.send_message("There is no such user on the guild")
        return

    await interaction.response.send_message(member.display_avatar)


bot.run(TOKEN)