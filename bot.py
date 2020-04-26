import discord
import os
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv('TOKEN')
CHANNEL = os.getenv('CHANNEL')
DEVICE = os.getenv('DEVICE')  # hw:1


class MicrophoneClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user}')
        channel = self.get_channel(int(CHANNEL))
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio(DEVICE, before_options='-f alsa -ac 1'))


client = MicrophoneClient()
client.run(TOKEN)
