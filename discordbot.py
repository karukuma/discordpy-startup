from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

@bot.event
async def on_command_error(ctx, error):
    await ctx.send(str(error))


@bot.command()
async def ping(ctx):
    await ctx.send('pong')
    
@bot.command()
async def neko(ctx):
    await ctx.send('にゃーおーん')

client = discord.Client()

@client.event
async def on_message(message):
    # 挨拶する千枝ちゃん
    if message.content.startswith('おはよう') and client.user != message.author and message.channel == client.get_channel('411701523169411082'):
        reply = f'おはようございます、{message.author.mention} さん'
        await client.send_message(message.channel, reply)
        
bot.run(token)
