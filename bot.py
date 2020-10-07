import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix='-')

wheel = []

@client.event
async def on_ready():
    print('Bot is Ready')


@client.event
async def on_member_join(member):
    print(f'{member} has joined a server.')


@client.event
async def on_member_remove(member):
    print(f'{member} has left a server.')


@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')


@client.command(aliases=['8ball'])
async def eightBall(ctx, *, question):
    responses = ["It is certain.",

                 "It is decidedly so.",

                 "Without a doubt.",

                 "Yes - definitely.",

                 "You may rely on it.",

                 "As I see it, yes.",

                 "Most likely.",

                 "Outlook good.",

                 "Yes.",

                 "Signs point to yes.",

                 "Reply hazy, try again.",

                 "Ask again later.",

                 "Better not tell you now.",

                 "Cannot predict now.",

                 "Concentrate and ask again.",

                 "Don't count on it.",

                 "My reply is no.",

                 "My sources say no.",

                 "Outlook not so good.",

                 "Very doubtful."]
    await ctx.send(f'Question: {question}\nAnswer : {random.choice(responses)}')

@client.command()
async def add(ctx, *, item):
    wheel.append(item)
    await ctx.send(f'{item} was added to the wheel')


@client.command()
async def spin(ctx):
    if not wheel:
        await ctx.send(f'The wheel is empty! \nType -add (item) to add to the wheel')
    else :
        await ctx.send(f'{random.choice(wheel)} has been chosen!')
        wheel.clear()

client.run('NzYyNjc3MDEzMTEwMTk0MjE3.X3soUQ.H-m1UGmP4V2d1Xn7Vn2i1VZAs8A')
