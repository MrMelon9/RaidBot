import discord
import asyncio

# Define your Discord token
TOKEN = 'Your Discord Bot Token'

# Create a client instance
intents = discord.Intents.default()
intents.typing = False
intents.presences = False
client = discord.Client(intents=intents)

# Global variable to hold the number of channels created
channel_counter = 1

# Event handler for bot login
@client.event
async def on_ready():
     print(f'Logged in as {client.user.name} ({client.user.id})')
     print('------')

     # Run a loop to create new channels
     await create_new_channel_every_hour()

# Function to create new channels every hour
async def create_new_channel_every_hour():
     global channel_counter # Define global variable usage

     while True:
         # Get the server (guild) where the bot is active
         guild = client.get_guild(00000000000000) # Replace with your server ID

         # Create a new channel named "new-channelX", where X is a numeric index
         channel_name = f'NewChannel{channel_counter}' # Change "NewChannel" to the name of the channel you want to spam everywhere
         existing_channel = discord.utils.get(guild.text_channels, name=channel_name)
         if not existing_channel:
             await guild.create_text_channel(channel_name)
             print(f'Created new channel: {channel_name}')
             channel_counter += 1 # Increase the numeric index

             # Ping @everyone
             new_channel = discord.utils.get(guild.text_channels, name=channel_name)
             await send_everyone_ping_with_gifs(new_channel)

         # Cooldown
         await asyncio.sleep(1) # 3600 seconds = 1 hour

# Function to send @everyone ping
async def send_everyone_ping_with_gifs(channel):
     # Ping @everyone
     await channel.send('@everyone')

# Start the bot
client.run(TOKEN)
