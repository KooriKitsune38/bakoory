import os
import random
import discord
from discord.ext import commands
from quart import Quart

app = Quart(__name__)

PORT = "65535"
bot = commands.Bot('!')

token = os.getenv("TOKEN")
my_guild = os.getenv("GUILD")

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == my_guild:
            break

    print(f"{client.user} is connected to the following guild:\n"
          f"{guild.name}(id: {guild.id})")


@client.event
async def on_member_join(member):
    # Add Dessert role on join
    dessertRole = member.guild.get_role(926872788801831012)
    await member.add_roles(dessertRole, atomic=True)


@client.event
async def on_message(message):
    # Strings
    aiem = ["i'm", "i am", "imma", "fuck me please i need to be a", "im"]

    selectedRole = None
    message_content = message.content.lower()
    # If the author is not bot, check for those statements
    if message.author != client.user:

        # Simple Message
        if "fuck me" in message_content:
            rand_int = random.randint(0, 1)
            if rand_int == 0:
                results = "No u."
            else:
                results = ":lamo:"
            await message.channel.send(results)

        if message.channel.id == 926864304463048734:
            await message.delete(delay=2)
            # Check for aiem strings and role name
            if any(char in message_content for char in aiem):

                # Check role selection
                if "pancake" in message_content:
                    selectedRole = message.guild.get_role(926866170760556554)
                if "muffin" in message_content:
                    selectedRole = message.guild.get_role(92686645994940825)
                if "musicer" in message_content:
                    selectedRole = message.guild.get_role(960989425934934036)

                if selectedRole != None:
                    # If specified "not" remove role, else add it
                    if "not" in message_content:
                        await message.channel.send(
                            "Aight, if you insist I guess I'll just remove it...",
                            delete_after=2)
                        await message.author.remove_roles(
                            selectedRole,
                            reason="The bitch didn't want it",
                            atomic=True)
                    else:
                        await message.channel.send("Yes ok calm down now",
                                                   delete_after=2)
                        await message.author.add_roles(
                            selectedRole,
                            reason="The Bitch wanted it",
                            atomic=True)

                else:
                    await message.channel.send(
                        "Rethink your life choices 'cause I can't find that role.",
                        delete_after=2)

bot.loop.create_task(app.run_task('0.0.0.0', PORT))

client.run(token)
