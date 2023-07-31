from discord import Interaction
from discord import app_commands
from discord.ext import commands
from inviteButtons import InvitationButton

class Invitation(commands.Cog):
  def __init__(self, bot: commands.Bot) -> None:
    self.bot = bot
    
  @app_commands.command(name="invite", description="Create an invite of the server")
  async def invite(self, interaction: Interaction):
    inv = await interaction.channel.create_invite()
    await interaction.response.send_message("Click the button below to invite someone", view=InvitationButton(inv=str(inv)))

async def setup(bot: commands.Bot) -> None:
  await bot.add_cog(Invitation(bot))