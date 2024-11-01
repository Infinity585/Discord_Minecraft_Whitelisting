import requests , json , discord , os
from discord import app_commands
from discord.ext import commands
from embed import newEmbed


class whitelistClass(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.API = 'https://api.mojang.com/users/profiles/minecraft/'
        self.jsonFile = os.getenv('jsonPath')
        self.logChannel = os.getenv('logChannel')

    @app_commands.command(name = 'whitelist' , description = '/whitelist <minecraft username>')
    @app_commands.describe(mcname = 'Your minecraft username')
    async def whitelist(self, interaction : discord.Interaction, mcname : str):
        await interaction.response.defer()

        try:
            response = requests.get(f"{self.API}{mcname}")
            response.raise_for_status()
            data = response.json()

            if data.get("errorMessage") != None:
                await interaction.followup.send(f"Error: {data['errorMessage']}", ephemeral=True)
                return

            uuid = data.get("id")
            name = data.get("name")


            if not uuid or not name:
                await interaction.followup.send("Invalid username", ephemeral=True)
                return

            with open(self.jsonFile, 'r') as file:
                whitelistData = json.load(file)

            if any(entry["uuid"] == uuid for entry in whitelistData):
                await interaction.followup.send(f"{name} is already whitelisted.", ephemeral=True)
                return

            whitelistData.append({"uuid": uuid, "name": name})


            with open(self.jsonFile, 'w') as file:
                json.dump(whitelistData, file, indent=2)
            await interaction.followup.send(f"{name} has been successfully whitelisted." , ephemeral=True)


            if self.logChannel:
                logChannel = self.bot.get_channel(int(self.logChannel))
                em = newEmbed(title="Whitelist", fields={"Name": name, "UUID": uuid , "Action": "Whitelisted" , "CMD USER": f"{interaction.user.global_name}({interaction.user.id})"  }, embedUrl=f"https://i.pinimg.com/736x/46/90/1a/46901a7b0f85435886c46fee15154f28.jpg")
                await logChannel.send(embed=em)



        except requests.exceptions.HTTPError as e:
            await interaction.followup.send(f"An error occurred while accessing the Mojang API: {e}")
        except json.JSONDecodeError:
            await interaction.followup.send("Failed to load the whitelist data.")





async def setup(bot : commands.Bot):
    await bot.add_cog(whitelistClass(bot))