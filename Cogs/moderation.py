from discord import utils, Interaction
from discord import app_commands
from discord.ext import commands

class Moderation(commands.Cog):
  def __init__(self, bot: commands.Bot) -> None:
    self.bot = bot

  @app_commands.command(name="create_channel", description="Create a new channel in a specific category (need admin perms)")
  @commands.has_permissions(manage_channels=True)
  async def create_guild_channel(self, interaction: Interaction, channel_name:str, category_name:str = None):
    print(interaction)
    guild = interaction.guild
    existing_channel = utils.get(guild.channels, name=channel_name)
    existing_category = utils.get(guild.categories, name=category_name)
    if not existing_category and category_name is not None:
        print(f"Category {category_name} doesn't exist, creating the category")
        await guild.create_category(category_name)
        existing_category = utils.get(guild.categories, name=category_name)

    if not existing_channel:
        print(f'Creating a new channel: {channel_name}')
        await guild.create_text_channel(channel_name, category= None if existing_category is None else existing_category)
        await interaction.response.send_message("The channel has been created")

  @app_commands.command(name="delete_channel", description="Delete a specified channel (need admin perms)")
  @commands.has_permissions(manage_channels=True)
  async def delete_guild_channel(self, interaction: Interaction, channel_name:str):
    guild = interaction.guild
    existing_channel = utils.get(guild.channels, name=channel_name)

    if not existing_channel:
        await interaction.response.send_message(f"The channel {channel_name} doesn't exist")

    await existing_channel.delete()
    await interaction.response.send_message(f"The channel {channel_name} has been deleted successfully ")

  @app_commands.command(name="create_category", description="Create a new category (need admin perms)")
  @commands.has_permissions(manage_channels=True)
  async def create_guild_category(self, interaction: Interaction, category_name:str):
    guild = interaction.guild
    existing_category = utils.get(guild.categories, name=category_name)

    if not existing_category:
        print(f'Creating the category {category_name}')
        await guild.create_category(category_name)
        await interaction.response.send_message(f"The category {category_name} has been created")
    else:
        await interaction.response.send_message(f'The category {category_name} already exists')

  @app_commands.command(name="delete_category", description="Delete a specified category (need admin perms)")
  @commands.has_permissions(manage_channels=True)
  async def delete_guild_category(self, interaction: Interaction, category_name:str):
    guild = interaction.guild
    existing_category = utils.get(guild.categories, name=category_name)

    if not existing_category:
        await interaction.response.send_message(f"The category {category_name} doesn't exist")
    
    await existing_category.delete()
    await interaction.response.send_message(f"The category {category_name} has been deleted successfully")

  @app_commands.command(name="purge", description="Delete x number of message in a channel (default: 100)")
  @commands.has_permissions(manage_messages=True)
  async def purge_channel(self, interaction: Interaction, nb_purge_message:int = 100):
    channel = interaction.channel
    await interaction.response.send_message(f"{nb_purge_message} messages have been deleted from channel {channel}", ephemeral=True)
    await channel.purge(limit=nb_purge_message)

  @app_commands.command(name="kick", description="Kick an user of the guild")
  @commands.has_permissions(kick_members=True)
  async def kick_user(self, interaction: Interaction, id_user:str, reason:str):
    member = interaction.guild.get_member(id_user)
    member.kick(reason= None if reason is None else reason)
    await interaction.response.send_message(f"The member {member.name} has been kicked from the guild")

  @app_commands.command(name="ban", description="Ban a member of a guild for an undetermine limit of time")
  @commands.has_permissions(ban_members=True)
  async def ban_user(self, interaction: Interaction, id_user:str, reason:str):
    member = interaction.guild.get_member(id_user)
    member.ban(delete_message_days=7, reason= None if reason is None else reason)
    await interaction.response.send_message(f"The member {member.name} has been bannned from the guild")

  @app_commands.command(name="add_role", description="Add a role to an user")
  @commands.has_permissions(manage_roles=True)
  async def add_role(self, interaction: Interaction, user:str, role:str):
     add_role = utils.get(interaction.guild.roles, name=role)
     add_to_user = interaction.guild.get_member_named(user)

     if add_role is None:
        await interaction.response.send_message("There is no input for the role to add")

     if add_to_user is None:
        await interaction.response.send_message("There is no such user on the guild")
        return
     
     await add_to_user.add_roles(add_role)
     await interaction.response.send_message(f"The role {role} has been attributed")

  @app_commands.command(name="remove_role", description="Remove the role of an user")
  @commands.has_permissions(manage_roles=True)
  async def remove_role(self, interaction: Interaction, user:str, role:str):
     add_role = utils.get(interaction.guild.roles, name=role)
     add_to_user = interaction.guild.get_member_named(user)

     if add_role is None:
        await interaction.response.send_message("There is no input for the role to add")

     if add_to_user is None:
        await interaction.response.send_message("There is no such user on the guild")
        return

     await add_to_user.remove_roles(add_role)
     await interaction.response.send_message(f"The role {role} has been removed")

async def setup(bot: commands.Bot) -> None:
  await bot.add_cog(Moderation(bot))