import discord
import asyncio

# Replace 'YOUR_TOKEN_HERE' with your bot's token
TOKEN = 'YOUR_TOKEN_HERE'

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
client = discord.Client(intents=intents)

channel_counter = 1

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name} ({client.user.id})')
    print('------')

    await create_new_channel_every_second()

async def create_new_channel_every_second():
    global channel_counter

    while True:
        # Replace 'YOUR_GUILD_ID_HERE' with your server ID
        guild = client.get_guild(YOUR_GUILD_ID_HERE)

        channel_name = f'NewChannel{channel_counter}'
        existing_channel = discord.utils.get(guild.text_channels, name=channel_name)
        if not existing_channel:
            try:
                new_channel = await guild.create_text_channel(channel_name)
                print(f'Created new channel: {channel_name}')
                channel_counter += 1

                if new_channel:
                    await send_everyone_ping(new_channel)
            except discord.Forbidden:
                print("Bot doesn't have permissions to create channels.")
            except discord.HTTPException as e:
                print(f"An error occurred: {e}")

        await asyncio.sleep(1)

async def send_everyone_ping(channel):
    try:
        await channel.send('@everyone')
    except discord.Forbidden:
        print("Bot doesn't have permissions to send messages in this channel.")
    except discord.HTTPException as e:
        print(f"An error occurred: {e}")

client.run(TOKEN)
