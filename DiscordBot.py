#Bot de telegram que spammea a un usuario con menciones en un servidor de Discord

import discord
import asyncio

discord_client = discord.Client()
TOKEN = token_marcador_de_posición

for server in client.guilds:
    print(f'{server.name}(id: {server.id})')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("/spam_ping"):
        # Encuentra al usuario que se quiere spammear
        user = message.mentions[0]
        # Encuentra el servidor donde se encuentra el usuario
        server = user.guild
        # Encuentra el canal donde se encuentra el usuario
        channel = user.channel
        # Encuentra el rol del usuario
        role = user.roles[0]
        # Encuentra el mensaje de spam
        spam_message = message.content[14:]
        # Encuentra el número de veces que se quiere enviar el mensaje
        spam_times = int(message.content[10])
        # Encuentra el tiempo de espera entre mensajes
        spam_wait = int(message.content[12])
        
