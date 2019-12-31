import discord
from discord.ext import commands
from discord import File
from discord.voice_client import VoiceClient
import random
import youtube_dl
import asyncio
import ffmpeg
import dropbox
import os
import io
from PIL import Image
import time
from discord import colour


#Used to check if bot is in voice channel
global vc
global connect_voice


description = "Discord Bot"
client = commands.Bot(command_prefix='', description=description)


# Initiates bot and prints username and id
@client.event
async def on_ready():
    activity = discord.Game(name="with LEGO's")
    await client.change_presence(status=discord.Status.idle, activity=activity)
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


# Send welcome message
@client.command()
async def on_member_join(ctx, member):
    await ctx.send(f'{member} hath arrived, welcome!')


# Send leave message
@client.command()
async def on_member_remove(ctx, member):
    await ctx.send(f'{member} have ascended from the server!')


# Respond to chats
@client.event
async def on_message(message):
    # Sends everything in image folder
    if 'spam all anime pics' in message.content.lower():
        # Makes a list all images
        files = os.listdir('img')
        # Read every image in binary and send it to the chat
        for picture in files:
            img = open('img/' + picture, 'rb')
            await message.channel.send(file=File(img))
            img.close()
    # Sends a random image
    elif 'anime pic' in message.content.lower():
        # Makes a list of all image names
        files = os.listdir('img')
        pic_list = []
        for i in files:
            pic_list.append(i)
        # Picks a random image and sends it to the chat
        rand_index = random.randint(0, len(pic_list) - 1)
        img = open('img/' + pic_list[rand_index], 'rb')
        await message.channel.send(file=File(img))
        img.close()
    # Plays a random song
    if 'gimme music' in message.content.lower():
        # Makes a list of all music files
        music_dir = "music"
        music_list = os.listdir(music_dir)
        # Makes sure the name is a folder, not a file
        still_folder = True
        # Goes into random folders until a file containing "." is found
        while still_folder:
            song = music_list[random.randint(0, len(music_list) - 1)]
            if '.' in song:
                still_folder = False
            else:
                music_dir += '/' + song
                music_list = os.listdir(music_dir)
        # Creates a sound source with the music at 20% volume
        source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(music_dir + '/' + song), volume=0.2)
        # Joins a voice channel and indicate that the bot is in a channel
        channel = message.author.voice.channel
        globals()['vc'] = await channel.connect()
        globals()['connect_voice'] = True
        # Sends the song name to the chat
        await message.channel.send(content='Playing ' + song)
        # Leave the channel after the song is finished
        globals()['vc'].play(source, after=lambda: print('done'))
    # Leave the voice channel if bot is in a channel
    if 'stop music' in message.content.lower():
        if 'vc' in globals():
            if globals()['vc']:
                globals()['connect_voice'] = False
                await globals()['vc'].disconnect()
    # Reconnects the bot and plays a new random song
    if 'new music' in message.content.lower():
        if 'vc' in globals():
            if globals()['vc']:
                globals()['connect_voice'] = False
                await globals()['vc'].disconnect()
        music_dir = "music"
        music_list = os.listdir(music_dir)
        still_folder = True
        while still_folder:
            song = music_list[random.randint(0, len(music_list) - 1)]
            if '.' in song:
                still_folder = False
            else:
                music_dir += '/' + song
                music_list = os.listdir(music_dir)
        source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(music_dir + '/' + song), volume=0.2)
        channel = message.author.voice.channel
        globals()['vc'] = await channel.connect()
        globals()['connect_voice'] = True
        await message.channel.send(content='Playing ' + song)
        globals()['vc'].play(source, after=lambda: print('done'))
    # Manually pick a song
    if 'find music' in message.content.lower():
        # Leave the channel if the bot is in a channel
        if 'vc' in globals():
            if globals()['vc']:
                globals()['connect_voice'] = False
                await globals()['vc'].disconnect()
        # Lists all music files
        music_dir = "music"
        music_list = os.listdir(music_dir)
        # Split the message into a list
        msg_list = message.content.split(' ')
        num_list = []
        # Create a list of all numbers in the message
        for i in msg_list:
            if i.isdigit():
                num_list.append(i)
        # Looks for the file based on the numbers given
        if len(num_list) == 2:
            # List all files
            music_dir = os.listdir('music/' + music_list[int(num_list[0]) - 1])
            # Generates a directory to the song based on numbers given
            music_dir1 = 'music/' + music_list[int(num_list[0]) - 1] + '/' + music_dir[int(num_list[1]) - 1]
            # Plays the song if the directory leads to a music file, and sends a message if it does not
            if '.' in music_dir1:
                source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(music_dir1), volume=0.2)
                await message.channel.send(content='Playing ' + music_dir[int(num_list[1]) - 1])
                channel = message.author.voice.channel
                globals()['vc'] = await channel.connect()
                globals()['connect_voice'] = True
                globals()['vc'].play(source, after=lambda: print('done'))
            else:
                await message.channel.send(content='Directory Does Not Lead to Music')
        elif len(num_list) == 3:
            # Makes a list of all file names
            music_dir = os.listdir('music/' + music_list[int(num_list[0]) - 1])
            # Generates the directory to the parent folder
            music_dir1 = os.listdir('music/' + music_list[int(num_list[0]) - 1] + '/' + music_dir[int(num_list[1]) - 1])
            # Generates directory to the song
            music_dir2 = 'music/' + music_list[int(num_list[0]) - 1] + '/' + music_dir[int(num_list[1]) - 1] + '/' + \
                         music_dir1[int(num_list[2]) - 1]
            # Plays the song if the directory leads to a music file, and sends a message if it does not
            if '.' in music_dir2:
                source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(music_dir2), volume=0.2)
                channel = message.author.voice.channel
                globals()['vc'] = await channel.connect()
                globals()['connect_voice'] = True
                await message.channel.send(content='Playing ' + music_dir1[int(num_list[2]) - 1])
                globals()['vc'].play(source, after=lambda: print('done'))
            else:
                await message.channel.send(content='Directory Does Not Lead to Music')
        elif len(num_list) == 4:
            # Same as before
            music_dir = os.listdir('music/' + music_list[int(num_list[0]) - 1])
            music_dir1 = os.listdir('music/' + music_list[int(num_list[0]) - 1] + '/' + music_dir[int(num_list[1]) - 1])
            music_dir2 = os.listdir(
                'music/' + music_list[int(num_list[0]) - 1] + '/' + music_dir[int(num_list[1]) - 1] +
                '/' + music_dir1[int(num_list[2]) - 1])
            music_dir3 = 'music/' + music_list[int(num_list[0]) - 1] + '/' + music_dir[int(num_list[1]) - 1] + '/' + \
                         music_dir[int(num_list[2]) - 1] + '/' + music_dir2[int(num_list[3]) - 1]
            if '.' in music_dir3:
                source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(music_dir), volume=0.2)
                channel = message.author.voice.channel
                globals()['vc'] = await channel.connect()
                globals()['connect_voice'] = True
                await message.channel.send(content='Playing ' + song)
                globals()['vc'].play(source, after=lambda: print('done'))
            else:
                await message.channel.send(content='Directory Does Not Lead to Music')
        else:
            await message.channel.send(content='Your Path Is Too Short To Lead to Music')
    # Puts a list of all song or directory names in the chat
    if 'list music' in message.content.lower():
        # Create a list of all directory names and a list of all numbers in the message
        music_dir = "music"
        music_list = os.listdir(music_dir)
        msg_list = message.content.split(' ')
        num_list = []
        for i in msg_list:
            if i.isdigit():
                num_list.append(i)
        # Lists home folder if no numbers give
        if len(num_list) == 0:
            music_list = os.listdir(music_dir)
            counter = 1
            msg_send = []
            # Generates a numbered list of the folder contents and sends it in a message
            for i in music_list:
                msg_send.append(str(counter) + '. ' + i + '\n')
                counter += 1
            await message.channel.send(''.join(msg_send))
        # Lists folders in the home folder
        elif len(num_list) == 1:
            music_list = os.listdir(music_dir + '/' + music_list[int(num_list[0]) - 1])
            counter = 1
            msg_send = []
            for i in music_list:
                msg_send.append(str(counter) + '. ' + i + '\n')
                counter += 1
            await message.channel.send(''.join(msg_send))
        # Lists folders that are 2 levels deep
        elif len(num_list) == 2:
            sub_list = os.listdir('music/' + music_list[int(num_list[0]) - 1])
            sub_list = os.listdir('music/' + music_list[int(num_list[0]) - 1] + '/' + sub_list[int(num_list[1]) - 1])
            counter = 1
            msg_send = []
            for i in sub_list:
                msg_send.append(str(counter) + '. ' + i + '\n')
                msg_send.append(str(counter) + '. ' + i + '\n')
                counter += 1
            await message.channel.send(''.join(msg_send))
        # The numbers given exceeds the depth of the music folder
        else:
            await message.channel.send('Too Much Numbers')
    # Rapidly changes the color of a role
    if 'rainbow name' in message.content.lower():
        gld = message.author.guild

        # Used to bypass an API error
        class rand_color:
            def __init__(self, value):
                self.value = value

        # Gives the message sender the rainbow name role
        await gld.get_member(message.author.id).add_roles(gld.get_role('role_id'))
        while True:
            try:
                # Generates a random integer less than the hex 0xFFFFFF and change the role color
                rand_c = random.randint(0, 16777215)
                await gld.get_role('role_id').edit(colour=rand_color(rand_c))
                # Waits 1 second to reach the request limit slower
                time.sleep(1)
            except:
                # Stops the loop when there is an error due to request counts
                break


# Runs the program or give an error
if __name__ == '__main__':
    try:
        client.run('bot_token')
    except Exception as e:
        input('An Error Has Occurred ' + str(e))
