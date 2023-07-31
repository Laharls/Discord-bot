from discord import ui, ButtonStyle, Interaction

class InvitationButton(ui.View):
    def __init__(self, *, inv:str):
        super().__init__()
        self.inv = inv

    @ui.button(label="Invite button", style=ButtonStyle.blurple)
    async def inviteBtn(self, interaction: Interaction, button: ui.Button):
        await interaction.response.send_message(self.inv, ephemeral=True)