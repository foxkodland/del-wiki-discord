import discord
import wikipedia


intents = discord.Intents.default() # Переменная intents - хранит привилегии бота
intents.message_content = True # Включаем привелегию на чтение сообщений
client = discord.Client(intents=intents) # Создаем бота в переменной client и передаем все привелегии


def api_wiki (query):
    wikipedia.set_lang ("ru")
    responce = wikipedia.summary(query)
    return responce


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    await message.channel.send(api_wiki(message.content))



client.run('token')
