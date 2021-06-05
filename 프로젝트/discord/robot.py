import discord
#한국에서 하시길

token = "ODQwNTMxNDAxNDk2NTkyNDI1.YJZj3g.YgLhNkIdoOc16Bclh3gN3xlt5UM"

client = discord.Client()
 
@client.event
async def on_ready():
    print('we had logged in as {0.user}'.format(client)) 


@client.event
async def on_message(message):
  if message.author == client.user:
     return

  if message.content.startswith("//hello"):
    await message.channel.send("hello!")

client.run(token)

