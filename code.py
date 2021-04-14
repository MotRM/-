import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run('ODMxNzA4Nzc0NTA2NTYxNTM3.YHZLKA.w05Asbj1-05l6bQYKSw1Y-a8CKs')