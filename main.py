import discord
import RandomPhrases

phrases = RandomPhrases.GetPhrases()
print(phrases)


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == 'ping':
            await message.channel.send('pong')

        elif message.content == 'Fuck you' or message.content == 'fuck you':
            await message.channel.send("why are you so mean to me ;'(")

        elif message.content == 'Hi!' or message.content == 'Hello!':
            

intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run('MTA1Nzc0NjU0MjAwMzQ5OTA1OQ.Gat8Ml.OLQX-9VN5NEhg_o3naboj7W-sZ38whf1IwlHP4')

#generates random compliments



