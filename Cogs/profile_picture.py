from discord import Interaction, File
from discord import app_commands
from discord.ext import commands

from PIL import Image, ImageDraw, ImageFont
import io

class DiscordProfileImage(commands.Cog):
  def __init__(self, bot: commands.Bot) -> None:
    self.bot = bot

  @app_commands.command(name="get_user_pp", description="Get the profile picture of a member")
  async def get_profile_picture(self, interaction: Interaction, user:str):
    member = interaction.guild.get_member_named(user)

    if member is None:
        await interaction.response.send_message("There is no such user on the guild")
        return

    await interaction.response.send_message(member.display_avatar)

  @app_commands.command(name="write_user_pp", description="Write short text on member pp")
  async def write_profile_picture(self, interaction: Interaction, user:str, text:str):
    member = interaction.guild.get_member_named(user)

    if member is None:
        await interaction.response.send_message("There is no such user on the guild")
        return

    # Fetch the member's avatar from Discord
    member_pp = member.display_avatar

    # Read the binary data (bytes) of the member's avatar
    binary_data = await member_pp.read()

    # Open the avatar image and convert it to RGBA mode
    with Image.open(io.BytesIO(binary_data)).convert("RGBA") as base:
        # Create a blank image for the text, initialized with transparent text color
        txt = Image.new("RGBA", base.size, (255, 255, 255, 0))

        # Get a font for the text
        fnt = ImageFont.truetype("assets/OpenSans-Bold.ttf", 40)

        # Get a drawing context to draw the text on the image
        draw = ImageDraw.Draw(txt)

        # Draw text on the blank image with half opacity (RGBA: 255, 150, 255, 255)
        draw.text((10, 10), text, font=fnt, fill=(255, 150, 255, 255))

        # Combine the modified text image with the base avatar image using alpha compositing
        out = Image.alpha_composite(base, txt)

        # Convert the modified image to bytes and store it in an in-memory buffer
        modified_image_bytes = io.BytesIO()
        out.save(modified_image_bytes, format="PNG")

        # Move the file pointer back to the beginning of the buffer to read the data
        modified_image_bytes.seek(0)

        # Send the modified image as a file attachment in a Discord message
        await interaction.response.send_message(file=File(modified_image_bytes, filename="modified_avatar.png"))

async def setup(bot: commands.Bot) -> None:
  await bot.add_cog(DiscordProfileImage(bot))