#https://discordpy.readthedocs.io/en/latest/api.html?

import discord
import random

client = discord.Client()
players = []
mafia = None

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):

    global msg
    global players

        # filters messages to only ones with the command
    if message.content.startswith('!mafia'):
        players = []
        msg = await message.channel.send('. \nReact to this message to be added to the player list. \nSend \'!go\' to start.')
        print("________________________________________________________")

    if message.content.startswith('!go'):
        if len(players)>0:
            if random.randint(0,100) < 10:
                for player in players:
                    await player.send('You are the mafia. \nYou know what must be done')
            else:
                mafia = random.choice(players)
                for player in players:
                    if player is mafia:
                        await mafia.send('You are the mafia. \nYou know what must be done')
                    else:
                        await player.send('You are totally innocent! \nGood luck out there!')       

@client.event
async def on_reaction_add(reaction, user):

    global msg
    global players

    if reaction.message.id == msg.id:
        if user not in players:
            print(user)
            players.append(user)




    # step 6: profit?

client.run('[BOT TOKEN HERE, SINCE REMOVED]')
