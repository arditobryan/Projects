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

val = 0

@client.event
async def code(message, val):
    await asyncio.sleep(1)
    await message.channel.send(val)
    return

@client.event
async def on_message(message):
    #everytime a new message is written on the server
    global val
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(message.author, message.content) #message.channel.name causes Ignoring exception in on_message

    try:
        thread, id = message.content.split(' ')[0], message.content.split(' ')[1]
    except:
        pass

    if user_message.lower() == '!try':
        for a in range(10):
            await code(message, 8) #we pass in the message that contains channel info
    
    #if message.channel_name == 'discord-bot tutorial':
    if user_message.lower() == '!random':
        await asyncio.sleep(5)
        if val < 2:
            await message.channel.send('keep going')
            return
        else:
            #from 2 or higher
            await message.channel.send('kill')
            return

    if user_message.lower() == '!add':
        val += 1
        await message.channel.send('added, now'+str(val))
        return

    if user_message.lower() == '!reset':
        val = 0
        await message.channel.send('reset, now'+str(val))
        return


client.run('<bot_id>')
