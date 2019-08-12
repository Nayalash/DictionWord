# Diction Word
# Developed By Nayalash Mohammad
# bot.py

import discord
import fetch

TOKEN = "INSERT_TOKEN"

client = discord.Client()


@client.event
async def on_ready():
    print("Bot is ready!")


@client.event
async def on_message(message):

    rawMessage = message.content.split(" ")

    if rawMessage[0] == "!fetch":
        await message.channel.trigger_typing()
        fetch.word = rawMessage[1]
        res_data = fetch.getData()
        await message.channel.send(f""" ```{res_data}``` """)

    elif message.content == "!help":
        await message.channel.trigger_typing()
        embed = discord.Embed(title="Diction Word", description="The DictionWord bot can find you any definition of a word, at the convenience of just one command")
        embed.add_field(name="!fetch word", value="Returns definition of the word")
        embed.add_field(name="Contact", value="https://github.com/Nayalash/DictionWord")
        await message.channel.send(content=None, embed=embed)


client.run(TOKEN)
