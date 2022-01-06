#stops running with our code
import asyncio
import discord
import random
import time

client = discord.Client()

@client.event
async def on_ready():
    #runs when the code is activated on local
    print('now running', client)

state_dict = dict()

@client.event
async def on_message(message):
    #everytime a new message is written on the server
    global state_dict
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(message.author, message.content) #message.channel.name causes Ignoring exception in on_message

    try:
        thread, id = user_message.split(' ')[0], user_message.split(' ')[1]
        print(thread, id)
    except:
        pass

    #if message.channel_name == 'discord-bot tutorial':
    if thread == '!activate':
        state_dict[id] = 0
        await asyncio.sleep(5)
        if state_dict[id] == 'interrupted':
            await message.channel.send('end')
            return
        else:
            for a in range(3):
                await message.channel.send(state_dict)
            return

    if thread == '!interrupt':
        try:
            state_dict[id] = 'interrupted'
            await message.channel.send(state_dict)
            return
        except:
            return

    if thread == '!add':
        try:
            state_dict[id] += 1
            await message.channel.send(state_dict)
            return
        except:
            return

    if thread == '!reset':
        try:
            state_dict[id] = 0
            await message.channel.send(state_dict)
            return
        except:
            return

client.run('<bot_id>')