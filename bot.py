import discord
import random
import datetime
import calendar
from datetime import date
from discord.ext import commands
from run import token

client = commands.Bot(command_prefix='-')
today = date.today()
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
    await ctx.send(f'{round(client.latency * 1000)}ms')


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
    else:
        await ctx.send(f'{random.choice(wheel)} has been chosen!')
        wheel.clear()


@client.command(aliases=['info', 'infomanagement', 'im'])
async def infoman(ctx):
    await ctx.send(f'Information Management: https://tcd.blackboard.com/webapps/collab-ultra/tool/collabultra?course_id=_63426_1&mode=view')


@client.command(aliases=['arch', 'ca'])
async def comparch(ctx):
    await ctx.send(f'Computer Architecture II: https://tcd.blackboard.com/webapps/collab-ultra/tool/collabultra?course_id=_63424_1&mode=view')


@client.command(aliases=['software', 'sw'])
async def sweng(ctx):
    await ctx.send(f'Software Engineering: https://tcd.blackboard.com/webapps/collab-ultra/tool/collabultra?course_id=_63410_1&mode=view')


@client.command(aliases=['funcpro', 'functional'])
async def func(ctx):
    await ctx.send(f'Functional Programming: https://tcd.blackboard.com/webapps/collab-ultra/tool/collabultra?course_id=_63423_1&mode=view')


@client.command(aliases=['compmaths', 'cm'])
async def maths(ctx):
    await ctx.send(f'Computational Mathematics: https://tcd.blackboard.com/webapps/collab-ultra/tool/collabultra?course_id=_63415_1&mode=view')


@client.command(aliases=['symbolic', 'prolog', 'sp'])
async def symb(ctx):
    await ctx.send(f'Symbolic Programming: https://tcd.blackboard.com/webapps/collab-ultra/tool/collabultra?course_id=_63422_1&mode=view')


@client.command()
async def timetable(ctx, *, day=''):
    if(day == ''):
        x = datetime.datetime.now()

        day = x.strftime("%A")

        if day == 'Saturday' or day == 'Sunday' or day == 'Friday':
            await ctx.send(f'It is a {day}.\nYOU ARENT IN COLLEGE TODAY')

        elif day == 'Monday':
            await ctx.send(f'{day}\n\nLIVE LECTURES:\n12pm: Software Engineering\n1pm: Symbolic Programming\n2pm: Functional Programming\n4pm:[TUTORIAL] Symbolic Programming\n\nRECORDED LECTURES:\nComputer Architecture II')

        elif day == 'Tuesday':
            await ctx.send(f'{day}\n\nLIVE LECTURES:\n9am: Symbolic Programming\n2pm:[TUTORIAL] Symbolic Programming\n\nRECORDED LECTURES:\nSoftware Engineering')

        elif day == 'Wednesday':
            await ctx.send(f'{day}\n\nLIVE LECTURES:\n9am: Software Engineering\n2pm: Information Management II\n3pm:[Q&A] Computer Architecture II\n4pm: Functional Programming\n\nRECORDED LECTURES:\nComputational Mathematics')

        elif day == 'Thursday':
            await ctx.send(f'{day}\n\nLIVE LECTURES:\n1pm: Computational Mathematics\n2pm: Functional Programming\n4pm: Information Management II\n\nRECORDED LECTURES:\nComputer Architecture II\nComputational Mathematics\nInformation Managment II')

    else:
        day.lower()
        if day == 'saturday' or day == 'sunday' or day == 'friday':
            await ctx.send(f'It is a {day}.\nNO COLLEGE')

        elif day == 'monday':
            await ctx.send(f'{day}\n\nLIVE LECTURES:\n12pm: Software Engineering\n1pm: Symbolic Programming\n2pm: Functional Programming\n4pm:[TUTORIAL] Symbolic Programming\n\nRECORDED LECTURES:\nComputer Architecture II')

        elif day == 'tuesday':
            await ctx.send(f'{day}\n\nLIVE LECTURES:\n9am: Symbolic Programming\n2pm:[TUTORIAL] Symbolic Programming\n\nRECORDED LECTURES:\nSoftware Engineering')

        elif day == 'wednesday':
            await ctx.send(f'{day}\n\nLIVE LECTURES:\n9am: Software Engineering\n2pm: Information Management II\n3pm:[Q&A] Computer Architecture II\n4pm: Functional Programming\n\nRECORDED LECTURES:\nComputational Mathematics')

        elif day == 'thursday':
            await ctx.send(f'{day}\n\nLIVE LECTURES:\n1pm: Computational Mathematics\n2pm: Functional Programming\n4pm: Information Management II\n\nRECORDED LECTURES:\nComputer Architecture II\nComputational Mathematics\nInformation Managment II')

client.run(token)
