import os

from discord import Intents, utils
from dotenv import load_dotenv
from discord.ext import commands
from Cogs import moderation, poll, invitation_guild, profile_picture

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
    await bot.add_cog(profile_picture.DiscordProfileImage(bot))
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)

@bot.event
async def on_member_join(member):
    guild = member.guild
    if guild.system_channel is not None:
        await guild.system_channel.send(f"Welcome {member.mention} to the server {guild.name}")

@bot.event
async def on_member_remove(member):
    guild = member.guild
    channel = utils.get(guild.channels, name="bienvenue")
    
    if channel and channel.permissions_for(guild.me).send_messages:
        await channel.send(f"{member.mention} has left the server")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Command not found")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Missing required argument")

bot.run(TOKEN)