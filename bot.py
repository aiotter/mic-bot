import discord
import os
import sys
from functools import partial
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
        self.play_mic(vc)

    def play_mic(self, voice_client, error=None):
        if error:
            raise error
        voice_client.play(
                discord.FFmpegPCMAudio(DEVICE, before_options='-f alsa -ac 1'),
                after=partial(self.play_mic, voice_client))

    async def on_error(*args, **kwargs):
        await super().on_error(*args, **kwargs)
        sys.exit(1)


client = MicrophoneClient()
client.run(TOKEN)
