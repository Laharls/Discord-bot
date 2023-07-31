from discord import Interaction, Embed
from discord import app_commands
from discord.ext import commands

class Poll(commands.Cog):
  def __init__(self, bot: commands.Bot) -> None:
    self.bot = bot
    

  @app_commands.command(name="poll", description="Make a poll about a topic in particular")
  async def poll(self, interaction: Interaction, question:str, answers:str):
    if '/' in answers:
        answer_list = answers.split("/")
        print(answer_list)
    else:
        await interaction.response.send_message("You can't make a poll with only 1 answer")
        return

    if len(answer_list) <= 1:
        await interaction.response.send_message("You can't make a poll with only 1 answer")
        return
    
    if len(answer_list) > 10:
            await interaction.response.send_message('You cannot make a poll for more than 10 things!')
            return
    
    reactions = ['1⃣', '2⃣', '3⃣', '4⃣', '5⃣', '6⃣', '7⃣', '8⃣', '9⃣', '🔟']

    description = []
    for x, option in enumerate(answer_list):
        description += '\n {} {}'.format(reactions[x], option)
    embed = Embed(title=question, description=''.join(description))
    react_message = await interaction.channel.send(embed=embed)
    for reaction in reactions[:len(answer_list)]:
        await react_message.add_reaction(reaction)
    embed.set_footer(text='Poll ID: {}'.format(react_message.id))
    await react_message.edit(embed=embed)
    await interaction.response.send_message("Poll created successfully", ephemeral=True)

async def setup(bot: commands.Bot) -> None:
  await bot.add_cog(Poll(bot))