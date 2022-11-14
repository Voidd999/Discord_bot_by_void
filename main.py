#------------------------------------------------------------------------------------------------------------------------------------------------------#
import discord
from PIL import Image
from io import BytesIO
from discord import activity
from discord import member
#from discord_components import Button, ButtonStyle
from math import *
import asyncio
from discord.member import Member
#import aiohttp
import requests
import random
import pyrandmeme
from pyrandmeme import *
from itertools import cycle
from discord.ext.commands.help import _HelpCommandImpl, HelpCommand
import json
from PIL import Image,ImageFilter
import datetime
from discord.client import Client
from player import WebPlayer
from dotenv import load_dotenv
from discord import Activity, ActivityType
from discord.colour import Color
from discord.ext import commands,tasks
from requests import get
import asyncio
import os
#from discord_components import DiscordComponents, Button, ButtonStyle
from math import *
import asyncio
from random import choice, randint
#---------------------------------------------------------------------import libs-------------------------------------------------------------------------#
load_dotenv('.env')
#TOKEN = 'OTIxMTAxMjQ3ODEyMTA0MjMy.YbuAYg.-T5JChXEV-tix_PU299nf543lyo' #discord bot token/key

TOKEN=os.getenv('DISCORD_TOKEN')

#---------------------------------------------------------------------------------------------------------------------------------------------------------#



bot = commands.Bot(command_prefix='_',)   #command prefix
bot.remove_command('help')

cryptocompare= 'https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD,EUR,INR&api_key=ad22b345bd40409693c9fdee5a5a7916a29d01ce414296588de3ae26da2516f2'
from requests import get
import json
price = get(cryptocompare).text
data = json.loads(price,)

eth = data["USD"]
ethinr= data["INR"]
print(eth)
# status = cycle(
    # [f'ETH Price ${eth}',f'ETH Price ₹{ethinr}'])

status = cycle(
     ['_help','Never gonna give you up | _help','Never gonna let you down | _help','Never gonna run around and desert you | _help'])


bot.lava_nodes = [
 #lavalink
     { 
        'host' : 'lava.link',
        'port' : 80,
        'rest_uri' : f'http://lava.link:80',
        'identifier' : 'MAIN',
        'password' : 'dipanshu12345',
        'region' : 'singapore'

     }
]

# @bot.command()
# @commands.cooldown(1, 10, commands.BucketType.user)
# async def memeloop(ctx):
#     stop_var = False
#     while (not stop_var):
     
#      content = get("https://meme-api.herokuapp.com/gimme").text
#      data = json.loads(content,)
#      meme = discord.Embed(title=f"{data['title']}", colour=discord.Color.purple() ).set_image(url=f"{data['url']}")
#      await ctx.reply(embed=meme)
     
#      await asyncio.sleep(5)

#      def check(ctx):
#             return not ctx.author.bot and ctx.command.name == "memestop"
#      try:
#             if await bot.wait_for("command", check=check, timeout=5.5):
#                 stop_var = True
#      except asyncio.TimeoutError:
#             print()




# @bot.command(name='memestop')
# @commands.cooldown(1, 10, commands.BucketType.user)
# async def memestop(ctx):
#     await ctx.send("stopped meme loop")
#     stop_var = True

#@bot.command()
#async def karuta(ctx):
   # bot.loop.create_task(my_task(ctx))

#------------------------------------------------------------------music---------------------------------------------------------------------------------#
@bot.command()
async def hello(ctx): #greet command
    await ctx.reply('*hi ' + format(ctx.author.mention) + '!*')



@bot.event   #ready
async def on_ready():
  change_status.start()

  print("\n\n Host started") 
  print(f" Name: {bot.user.name}")
  print(f" ID: {bot.user.id}\n\n")
  bot.load_extension('dismusic')

@tasks.loop(seconds=5)#status loop

# async def change_status(): 
    
#  cryptocompare= os.getenv('cc_api')

#  price = get(cryptocompare).text
#  data = json.loads(price,)

#  eth = data["USD"]
#  ethinr= data["INR"]

#  status = (f'ETH Price  ${eth} | ₹{ethinr}')
#  await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=status))


async def change_status():
    await bot.change_presence(activity=discord.Game(next(status)))
#-------------------------------COMMANDS---------------------------------------------------------------------------


@bot.command()
async def clear(ctx, limit: int=None):
    passed = 0
    failed = 0
    async for msg in ctx.message.channel.history(limit=limit):
        if msg.author.id == bot.user.id:
            try:
                await msg.delete()
                passed += 1
            except:
                failed += 1
    await ctx.send(f"**Removed {passed} messages with {failed} fails**")
    
@bot.command(name='ping', help='this command shows the latency')
async def ping(ctx):


    await ctx.send(f'latency : {round(bot.latency * 1000)}ms')


@bot.command() #wave command
async def wave(ctx):
    await ctx.reply(f'*(waves at ' + format(ctx.author.display_name) + f')*^-^')


@bot.command(name='pfp', help="this command displays the mentioned users's profile picture") #user avatar command
async def pfp(ctx, member: discord.Member = None):
    if not member:
        member = ctx.author
    show_pfp = discord.Embed(title='*' + format(member.display_name) + "'s" + ' profile picture*' ,
        colour = discord.Color.dark_gold()
        
    )

    show_pfp.set_image(url='{}'.format(member.avatar_url))
    
    await ctx.send(embed=show_pfp)
   

# @bot.command(name='dm', help="this command DM's the mentioned user") #rickroll dm command
# @commands.cooldown(1, 3, commands.BucketType.user)
# async def dm(ctx, member: discord.Member = None):
#     if not member:
#         member = ctx.author

#     await member.send(file=discord.File('please.gif',))
#     await member.send('**Hey!' + format(member.display_name) + ', check out our latest upload :pray: it took us 10+ HRS  to edit, it will mean a lot if you show some support to the creator :smiling_face_with_3_hearts:' +
#      '<https://www.youtube.com/watch?v=dQw4w9WgXcQ>**'
#     )
    

@bot.command(name='meme' , help='this command sends a random meme from a subreddit') #meme command
async def meme(ctx):
    content = get(os.getenv('meme_api_key')).text
    data = json.loads(content,)
    meme = discord.Embed(title=f"{data['title']}", colour=discord.Color.random() ).set_image(url=f"{data['url']}")
    await ctx.reply(embed=meme)

@bot.command()
async def meme2(ctx):
    await ctx.send(embed=await pyrandmeme())
    

@bot.command(name = "bruh", help = 'this command turns anyone into a "bruh moment"')     #bruh command
@commands.cooldown(1, 5, commands.BucketType.user)
async def bruh(ctx,member: discord.Member = None):
    if not member:
        member = ctx.author

    bruh = Image.open('resources/bruh.jpg')    

    asset = member.avatar_url_as(size=128)
    data = BytesIO(await asset.read())
    pfp = Image.open(data)

    pfp = pfp.resize((967,529))
    bruh.paste(pfp ,(466,282))
    
    bruh.save('resources/manipulatedbruh.jpg')
   
    await ctx.send(file = discord.File('resources/manipulatedbruh.jpg') )

@bot.command(aliases = ['insult','burn']) #roast
@commands.cooldown(1, 4, commands.BucketType.user)
async def roast(ctx,member: discord.Member = None):
    if not member:
        member = ctx.author


    content = get(os.getenv("insult_api_key")).text

    await ctx.send(format(member.mention) + ', ' + content)

    
# @bot.command(name="invite" ,help="this command sends the link to invite this bot in your guild")
# async def invite(ctx):
#     await ctx.send("*invite Void's bot to your server by clicking on this link " + 'https://discord.com/api/oauth2/authorize?client_id=900345340782346260&permissions=532613168192&scope=bot' + '*')
 
@bot.command(name ='roll', help = 'this command rolls the dice for you')#dice roll
@commands.cooldown(1, 5, commands.BucketType.user)
async def roll(ctx):
    

    dice = random.randint(0,6)
    await ctx.send('**Rolling the dice for ' + format(ctx.author.mention) + '......**')
    await ctx.send('*The dice rolled ' + str(dice) + '*')#integer to string

@bot.command(name ='toss', help='this command flips the coin for you')#coinflip
@commands.cooldown(1, 5, commands.BucketType.user)
async def toss(ctx):
    

    result = random.choice(["Heads","Tails"])
    embed=discord.Embed(title= 'Tossing the coin for ' + format(ctx.author.display_name) ,description = '.........' , colour=0xffd480 , timestamp=ctx.message.created_at)
    embed.set_thumbnail(url='https://c.tenor.com/eW8l2UmVFFkAAAAM/railgun-anime.gif')


    toss = await ctx.send(embed=embed)
    embed2 = discord.Embed(title = f'Tossing the coin for '+ format(ctx.author.display_name),description = f'The coin tossed {result}',color=0xffd480,timestamp=ctx.message.created_at)
    embed2.set_thumbnail(url='https://c.tenor.com/eW8l2UmVFFkAAAAM/railgun-anime.gif')
    await toss.edit(embed=embed2) 

@bot.command(name='wink')
@commands.cooldown(1, 5, commands.BucketType.user)
async def wink(ctx): 
    content = get("https://some-random-api.ml/animu/wink").text
    data = json.loads(content,)
    wink= discord.Embed(title=f"wink :wink: ",Color = discord.Color.random()).set_image(url=f"{data['link']}")
    await ctx.send(embed=wink)
@bot.command(name = 'aquote', help = 'this command sends a random quote from an anime')
@commands.cooldown(1, 5, commands.BucketType.user)
async def aquote(ctx):
    cont = get(os.getenv('anime_quotes_key')).text
   
    data = json.loads(cont,)
    animename = data["anime"]
    quote = data["quote"]
    char = data["character"]
    embed=discord.Embed(title= '"' + quote + '"',Color=discord.Color.dark_grey(),description = '- ' + char + ' from ' + animename,timestamp=ctx.message.created_at)
    await ctx.send(embed=embed)
        

@bot.command(name= 'joke',help='this command sends a joke')
@commands.cooldown(1, 5, commands.BucketType.user)
async def joke(ctx):
    cont = get(os.getenv('joke_api_key')).text
    data = json.loads(cont,)
    await ctx.send(data["joke"])
@bot.command(name= 'uselessfact' ,help='this command sends a random useless fact')
@commands.cooldown(1, 5, commands.BucketType.user)
async def uselessfact(ctx):
    cont = get(os.getenv('useless_facts')).text
    data = json.loads(cont,)
    await ctx.send('*' + data["data"] + '*') 

# @bot.command()
# async def covid( ctx, *, countryName = None):
#         try:
#             if countryName is None:
#                 embed=discord.Embed(title="This command is used like this: _covid [country] ", colour=0xff0000, timestamp=ctx.message.created_at)
#                 await ctx.send(embed=embed)


#             else:
#                 url = f"https://coronavirus-19-api.herokuapp.com/countries/{countryName}"
#                 stats = requests.get(url)
#                 json_stats = stats.json()
#                 country = json_stats["country"]
#                 totalCases = json_stats["cases"]
#                 todayCases = json_stats["todayCases"]
#                 totalDeaths = json_stats["deaths"]
#                 todayDeaths = json_stats["todayDeaths"]
#                 recovered = json_stats["recovered"]
#                 active = json_stats["active"]
#                 critical = json_stats["critical"]
#                 casesPerOneMillion = json_stats["casesPerOneMillion"]
#                 deathsPerOneMillion = json_stats["deathsPerOneMillion"]
#                 totalTests = json_stats["totalTests"]
#                 testsPerOneMillion = json_stats["testsPerOneMillion"]

                

#                 embed2 = discord.Embed(title=f"**COVID-19 Status Of {country}**", description="This Information Isn't realtime so it may not be accurate", colour=discord.Color.random(), timestamp=ctx.message.created_at)
               
#                 embed2.add_field(name="**Total Cases**", value=totalCases, inline=True)
#                 embed2.add_field(name="**Cases Today**", value=todayCases, inline=True)
#                 embed2.add_field(name="**Total Deaths**", value=totalDeaths, inline=True)
#                 embed2.add_field(name="**Deaths Today**", value=todayDeaths, inline=True)
#                 embed2.add_field(name="**Recovered**", value=recovered, inline=True)
#                 embed2.add_field(name="**Active**", value=active, inline=True)
#                 embed2.add_field(name="**Critical**", value=critical, inline=True)
#                 embed2.add_field(name="**Cases Per Million**", value=casesPerOneMillion, inline=True)
#                 embed2.add_field(name="**Deaths Per Million**", value=deathsPerOneMillion, inline=True)
#                 embed2.add_field(name="**Total Tests**", value=totalTests, inline=True)
#                 embed2.add_field(name="**Tests Per Million**", value=testsPerOneMillion, inline=True)
                

#                 embed2.set_thumbnail(url="https://media.discordapp.net/attachments/442643886566014986/902923708501487627/covid.jpg")
#                 await ctx.send(embed=embed2)

#         except:
#             embed3 = discord.Embed(title="Couldn't resolve country name Or API Error!, please try again", colour=0xff0000, timestamp=ctx.message.created_at)
#             embed3.set_author(name="Error!")
#             await ctx.send(embed=embed3)
@bot.command(aliases = ['ym'])#yomama
@commands.cooldown(1, 5, commands.BucketType.user)
async def yomama(ctx,member: discord.Member = None):
    if not member:
       member = ctx.author
    
    content2 = get(os.getenv('yomama_api')).text
    
    data2 = json.loads(content2,)
    ym = data2["joke"]
    await ctx.send(format(member.mention) + ', ' + ym )


@bot.command(name='anime') #command
async def anime(ctx):
    content = get(os.getenv('subreddit_api')).text
    data = json.loads(content,)
    anime_post = discord.Embed(title=f"{data['title']}", colour=discord.Color.random() ).set_image(url=f'{data["image"] }')
    await ctx.reply(embed=anime_post)


@bot.command(name='gay' , help = 'this commands tells you your gay percentage' )
@commands.cooldown(1, 5, commands.BucketType.user)
async def gay(ctx,member: discord.Member = None):
    if member is None:
        member = ctx.author
    gay = str(random.randrange(101))   
    embed=discord.Embed(title= format(member.display_name) + "'s " 'Gay percentage', colour=0xff80ff,description = format(member.display_name) + 'is ' + gay + '%'  + ' Gay :smirk:' )   
    embed.set_thumbnail(url='https://i.gifer.com/GOq.gif')
    await ctx.send(embed=embed)
    if gay == str(100):
        await ctx.send(format(member.mention) + '0_0')
#-------------------------------------------------------economy sys------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
@bot.command(aliases=['bal'])
async def balance(ctx,user: discord.Member = None):
    if not user:
        user = ctx.author

    await open_account(user)
    user = user
    users = await get_eco_data()
    wallet_amt = users[str(user.id)]['wallet']
    bank_amt = users[str(user.id)]['bank']

    bal = discord.Embed(title = f"{user.name}'s poro balance ", colour=0xff004d ,description ='**Wallet**: '+ '\🔸'+ str(wallet_amt) + '\n**Bank**:  ' + '\🔸' +str(bank_amt) ,timestamp=ctx.message.created_at)
    
    await ctx.send(embed = bal)
@bot.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def beg(ctx):
    user = ctx.author
    await open_account(ctx.author)
    beg_list= ['Donald Trump','Billie Eilish','The Trans dude', 'Drake', 'Biden', 'Shenron','Luffy','Joesph Joestar','The Karen']

    response = ['true','false']

    beg_choice= random.choice(beg_list)
    response_res= random.choice(response)
    refuse = ['said : **NO**', 'said : *Go away you peasant*','*Whined like a cow and refused*','said : *Go beg somewhere else*']
    res_confirm=random.choice(response)
    earning = random.randrange(501)
    if response_res == res_confirm:

      await update_bank(ctx.author,1*earning)
      
      await ctx.send(f'**{ctx.author.mention} begged {beg_choice}**') 
      await ctx.send(f'*{beg_choice} gave you **{earning}** poros!*')
      return
    else:
      
      await ctx.send(f'**{ctx.author.mention} begged {beg_choice}.**')
      await ctx.send(f'{beg_choice} {random.choice(refuse)}')
      return

@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def search(ctx):
    user = ctx.author
    await open_account(ctx.author)
    users = await get_eco_data()
    search_list = ['homeless person','grass','car','purse','road','backyard']
    loc = random.choice(search_list)
    earning = random.randrange(251)
    await ctx.send(f'*You searched the {loc} and found {earning} poros*')

    users[str(user.id)]['wallet'] += earning
    with open("bank.json","w") as f:
     json.dump(users,f)

@bot.command(aliases=['with'])
async def withdraw(ctx,amount = None):
    await open_account(ctx.author)
    if amount == None:
        await ctx.send("Please enter the amount to be withdrawn")
        return
    user = ctx.author
    users = await get_eco_data()    
    
   
    
        

    bal = await update_bank(ctx.author)

    amount = int(amount)
    
    if amount > bal[1]:
        await ctx.send('insufficient balance')
        return
    if amount < 0:
        await ctx.send('Amount must be positive! you dumbass')
        return
    users = await get_eco_data()    
    wallet_amt = users[str(user.id)]['wallet']
    bank_amt = users[str(user.id)]['bank']

    await update_bank(ctx.author,amount)
    await update_bank(ctx.author,-1*amount,'bank')
    await ctx.send(f'{ctx.author.mention} You withdrew {amount} poros!')


@bot.command(aliases=['dep'])
async def deposit(ctx,amount = None):
    await open_account(ctx.author)
    
    
    if amount == None:
        await ctx.send("Please enter the amount to be deposited")
        return
    user = ctx.author
    bal = await update_bank(ctx.author)
    
    amount = int(amount)
    users = await get_eco_data()    
    
    
    if amount > bal[0]:
        await ctx.send('insufficient balance')
        return
    if amount < 0:
        await ctx.send('Amount must be positive! you dumbass')
        return
    users = await get_eco_data()    
    
    await update_bank(ctx.author,-1*amount)
    await update_bank(ctx.author,amount,'bank')
    await ctx.send(f'{ctx.author.mention} You deposited {amount} poros!')
    bank_amt = users[str(user.id)]['bank']
    wallet_amt = users[str(user.id)]['wallet']

@bot.command(aliases=['give'])
async def send(ctx,member: discord.Member,amount = None):
    await open_account(ctx.author)
    await open_account(member)
    
    if amount == None:
        await ctx.send("Please enter the amount you want to send")
        return
    user = ctx.author
    bal = await update_bank(ctx.author)

    amount = int(amount)
    
    if amount > bal[1]:
        await ctx.send('insufficient balance')
        return
    if amount < 0:
        await ctx.send('Amount must be positive! you dumbass')
        return
    users = await get_eco_data()    
    
    await update_bank(ctx.author,-1*amount,"bank")
    await update_bank(member,amount,'bank')
    await ctx.send(f'{ctx.author.display_name} gave {member.display_name} {amount} poros!')
@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def slots(ctx,amount=None):  
    await open_account(ctx.author)

    if amount == None:
        await ctx.send("Please enter the amount you want to put")
        return
    bal = await update_bank(ctx.author)
    amount = int(amount)
    if amount> bal[0]:
        await ctx.send('insufficient balance')
        return
    if amount < 0:
        await ctx.send('Amount must be positive! you dumbass')
        return
    if amount < 50:
        await ctx.send('Minimum amount must be at least 50')
        return
    
    slot = ["\💮" , "\💠" , "\🌟" ,"\👑" , "\💰" , "\💗"  , "\🌞"]
    slot1 = random.choice(slot)
    slot2 = random.choice(slot)
    slot3 = random.choice(slot)
    slotOutput = f' {slot1}  {slot2}  {slot3} '.format(slot1, slot2, slot3)

    if slot1 == slot2 == slot3:
        await update_bank(ctx.author,4*amount)
        em18 = discord.Embed(title = f"Slots Machine for {ctx.author}",color = discord.Color.green(), timestamp=ctx.message.created_at)
        em18.add_field(name = slotOutput.format(slotOutput), value = f"You quadrupled your **{amount}** poros!:moneybag: :moneybag: ")
        await ctx.send(embed = em18)
        return

    elif slot1 == slot2 or slot1 == slot3 or slot2 == slot3:
        await update_bank(ctx.author,2*amount)
        em17 = discord.Embed(title = f"Slots Machine for {ctx.author} ",color = discord.Color.green(), timestamp=ctx.message.created_at)
        em17.add_field(name = slotOutput.format(slotOutput), value = f"You doubled your **{amount}** poros!:money_with_wings: :money_with_wings: ")
        await ctx.send(embed = em17)
        return

    else:
        await update_bank(ctx.author,-1*amount)
        em19 = discord.Embed(title = "Slots Machine",color = discord.Color.red(),timestamp=ctx.message.created_at)
        em19.add_field(name = slotOutput.format(slotOutput), value = f"You lost **{amount}** poros!**\n **Better luck next time.")
        await ctx.send(embed = em19)
        return

@bot.command(aliases=['steal'])
@commands.cooldown(1, 5, commands.BucketType.user)
async def rob(ctx,member : discord.Member):
    await open_account(ctx.author)
    await open_account(member)
    bal = await update_bank(member)
    bal2 = await update_bank(ctx.author)


    if bal[0]<200:
        await ctx.send('**The person you are trying to rob is already broke:sneezing_face:**')
        return
    if bal2[0] < 500:
        await ctx.send('**You need atleast 1000 poros in your wallet to rob someone**')
        return

    theft = ['true','false']
    res = random.choice(theft)
    res_confirm = random.choice(theft)
    earning = random.randrange(100,bal[0])
    
   
    if res == res_confirm:

      await update_bank(ctx.author,earning)
      await update_bank(member,-1*earning)
      await ctx.send(f'**{ctx.author.mention} robbed {member} and got {earning} poros! :dollar::dollar: **') 
      return
    else:
      
      await ctx.send(f'*You got caught stealing and spent some time in prison and were fined for **1000** poros*')
      await update_bank(ctx.author,-1*1000)

      return

@bot.command(aliases=['daily'])
@commands.cooldown(1, 60*60*24, commands.BucketType.user)
async def bonus(ctx):
     await open_account(ctx.author)
     await update_bank(ctx.author,1*1000)
     bonus = discord.Embed(title=f'**{ctx.author} daily poro bonus!**',description = f'Your bonus **1000** poros were added to your balance ',color =discord.Color.dark_gold(), timestamp=ctx.message.created_at)
     await ctx.send(embed=bonus)
 
@bot.command()
async def giveaway(ctx):

        
        timeout = 60
        embedq1 = discord.Embed(title="**:gift: | Host a Giveaway**",
                                description=f"Welcome to the Setup Wizard. Answer the following questions within ``{timeout}`` Seconds!",color = discord.Color.dark_theme())
        embedq1.add_field(name="Channel for hosting",
                          value="where to host the Giveaway?\n\n **Example**: ``#General``")
        embedq2 = discord.Embed(title="**:gift: | Host a Giveaway**",description="Setting up...."
                                ,color = discord.Color.dark_theme())
        embedq2.add_field(name="Duration",
                          value="Enter the duration of the giveaway ``<s|m|h|d|w>``\n\n **Example**:\n ``1d``\n``1h``\n``1m``")
        embedq3 = discord.Embed(title="**:gift: Host a Giveaway**",
                                description="Almost done setting up",color = discord.Color.dark_theme())
        embedq3.add_field(name="Prize",
                          value="Enter the prize the winner will receive \n\n **Example**:\n ``Discord Nitro``")

        questions = [embedq1,
                     embedq2,
                     embedq3]

        answers = []

        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel

        for i in questions:
            await ctx.send(embed=i)

            try:
                msg = await bot.wait_for('message', timeout=20, check=check)
            except asyncio.TimeoutError:
                embed = discord.Embed(title=":gift: **Host a Giveaway**", description=":x: You didn't answer in time!",color = discord.Color.dark_theme())
                await ctx.send(embed=embed)
                return
            else:
                answers.append(msg.content)

        try:
            c_id = int(answers[0][2: -1])
        except:
            embed = discord.Embed(title=":gift: **Host a Giveaway**", description=":x: You didn't specify a channel correctly!",color = discord.Color.dark_theme())
            await ctx.send(embed=embed)
            return

        channel = bot.get_channel(c_id)

        time = convert(answers[1])
        if time == -1:
            embed = discord.Embed(title=":gift: **Host a Giveaway**",
                                description=":x: You didn't set duration properly",color = discord.Color.dark_theme())
            await ctx.send(embed=embed)
            return
        elif time == -2:
            embed = discord.Embed(title=":gift: **Host a Giveaway**",
                                  description=":x: Duration unit **MUST** be an integer",color = discord.Color.dark_theme())
            await ctx.send(embed=embed)
            return
        prize = answers[2]

        embed = discord.Embed(title=":gift: **Host a Giveaway**",
                              description="Done setting up. The Giveaway will now begin!"+'\n'+f"**Hosted in Channel**: {channel.mention}\n**Duration**: {answers[1]}\n**Prize**: {prize}",color = discord.Color.dark_theme())
        
        await ctx.send(embed=embed)
        await ctx.send(
            f"New Giveaway Started. Hosted By {ctx.author.mention}. Hosted in {channel.mention} for {answers[1]}. The  Prize is **{prize}**")
        
        embed = discord.Embed(title=f":tada: **GIVEAWAY FOR  {prize}**",
                              description=f"React with :cookie: to enter!"+'\n'+f"**Hosted in Channel**: {channel.mention}\n**Duration**: {answers[1]}\n**Prize**: {prize}",color = discord.Color.teal(),timestamp=ctx.message.created_at)
        embed.add_field(name="Lasts:", value=answers[1])
        embed.add_field(name=f"Hosted By:", value=ctx.author.mention)
        await channel.send('@everyone react with :cookie: to enter!')
        msg = await channel.send(embed=embed)
        

        await msg.add_reaction('🍪')
        await asyncio.sleep(time)

        new_msg = await channel.fetch_message(msg.id)
        users = await new_msg.reactions[0].users().flatten()
        print(users)
        users.pop(users.index(bot.user))


        winner = random.choice(users)
        ping_winner_message = True
        if ping_winner_message == True:
            await channel.send(f":tada: Congratulations! {winner.mention} you won the giveaway. Your prize is **{prize}**!")
            
            

        embed2 = discord.Embed(title=f":tada: **GIVEAWAY ENDED**",
                               description=f":trophy: **Winner:** {winner.mention} \n**Prize: {prize}\n**Duration: {answers[1]}", colour=discord.Color.teal(), timestamp=ctx.message.created_at)
        embed2.set_footer(text="Giveaway Has Ended")
        embed2.add_field(name='Participants', value= f'{len(users)}')
        await msg.edit(embed=embed2)

@bot.command()
async def poll(ctx, *, content:str):
  await ctx.channel.purge(limit=1)
  embed=discord.Embed(title=f"{content}", description="React to this message with ✅ for yes\n❌ for no.",  color=discord.Color.random())
  message = await ctx.channel.send(embed=embed)
  
  await message.add_reaction("✅")
  await message.add_reaction("❎")
  new_msg = await ctx.channel.fetch_message(message.id)
  users = await new_msg.reactions[0].users().flatten()
  embed.add_field(name="Participants",value=f'{len(users)}')
  
#---------------------------------------help-command-----------------------------------------------------------------------------------------------------------------------
@bot.command(aliases=["commands"])
async def help(ctx):
    page1 = discord.Embed(
        title = '      __Help Page 1/4__',
        description = "      Void's Bot's General Commands\nPrefix = '_'\n**COMMANDS**",
        colour = discord.Colour.red()
    
    )
    page1.set_author(name = f'{bot.user.name}',icon_url='https://media.discordapp.net/attachments/805723485372284932/912702901841981470/1634727211621.jpg')
    page1.add_field(name='``Help  ``', value='Shows the list of commands', inline=False)
    page1.add_field(name='``Clear  ``', value='Clears the amount of messages mentioned', inline=False)
    page1.add_field(name='``hello  ``', value='Hi;)', inline=False)
    page1.add_field(name='``Invite  ``', value='Sends the link to invite this bot in your guild', inline=False)
   
    page2 = discord.Embed (
        title = '      __Help Page 2/4__',
        description = "       Void's Bot's Music Commands\nPrefix = '_'\nThis bot uses a pre built music library 'dismusic'\n**COMMANDS**",
        colour = discord.Colour.purple()
    )
    page2.add_field(name='``connect ``', value='Connect the player to voice channel', inline=False)
    page2.add_field(name='``disconnect ``', value='Disconnect the player from voice channel', inline=False)
    page2.add_field(name='``equalizer ``', value='Set equalizer', inline=False)
    page2.add_field(name='``loop ``', value='Set loop to ``NONE``, ``CURRENT`` or ``PLAYLIST``', inline=False)
    page2.add_field(name='``nowplaying ``', value="What's playing now?", inline=False)
    page2.add_field(name='``pause ``', value='Pause the player', inline=False)
    page2.add_field(name='``play ``', value='Play or add song to queue', inline=False)
    page2.add_field(name='``queue ``', value="Player's current queue", inline=False)
    page2.add_field(name='``resume ``', value='Resume the player', inline=False)
    page2.add_field(name='``seek ``', value='Seek the player backward or forward', inline=False)
    page2.add_field(name='``skip ``', value='Skip currently playing song', inline=False)
    page2.add_field(name='``volume ``', value='Set volume', inline=False)
    page2.set_author(name = f'{bot.user.name}',icon_url='https://media.discordapp.net/attachments/805723485372284932/912702901841981470/1634727211621.jpg')



    page3 = discord.Embed (
        title = '      __Help Page 3/5__',
        description = f"       Void's Bot's Currency Commands\nPrefix = '_'\n**COMMANDS**",
        colour = discord.Colour.gold()
    )
    page3.add_field(name='``about  ``', value='To see info about the bot', inline=False)
    page3.add_field(name='``balance  ``', value='To see your poro balance', inline=False)
    page3.add_field(name='``beg  ``', value='To beg some poros', inline=False)
    page3.add_field(name='``bonus  ``', value='To get the daily bonus', inline=False)
    page3.add_field(name='``deposit  ``', value='To deposit poros in bank', inline=False)
    page3.add_field(name='``withdraw  ``', value='To withdraw poros from bank', inline=False)
    page3.add_field(name='``send  ``', value='Send poros to someone', inline=False)
    page3.add_field(name='``rob  ``', value='Rob someone ', inline=False)
    page3.add_field(name='``slots  ``', value='To use the slot machine some', inline=False)
    #page3.add_field(name='``shop  ``', value='To view shop', inline=False)
    #page3.add_field(name='``buy  ``', value='To, buy an item', inline=False)
    #page3.add_field(name='``sell  ``', value='To sell an item', inline=False)
    #page3.add_field(name='``bag  ``', value='To view your invetory', inline=False)
    #page3.add_field(name='``lb  ``', value='To view leaderboard', inline=False)
    page3.set_author(name = f'{bot.user.name}',icon_url='https://media.discordapp.net/attachments/805723485372284932/912702901841981470/1634727211621.jpg')

    page4 = discord.Embed(
        title = '      __Help Page 4/5__',
        description = f"       Void's Bot's MEME Commands\nPrefix = '_'\n**COMMANDS**",
        colour = discord.Colour.magenta()
    
    )
    page4.add_field(name='``meme  ``', value='Sends a random meme from a subreddit', inline=False)
    page4.add_field(name='``joke  ``', value='Sends a joke', inline=False)
    page4.add_field(name='``roast  ``', value='Roasts you or whom you wish', inline=False)
    page4.add_field(name='``bruh  ``', value='Turns anyone into a BRUH MOMENT', inline=False)
    page4.add_field(name='``yomama  ``', value="Sends a yomama joke", inline=False)
    page4.add_field(name='``gay  ``', value='Shoes you gay percentage', inline=False)
    page4.set_author(name = f'{bot.user.name}',icon_url='https://media.discordapp.net/attachments/805723485372284932/912702901841981470/1634727211621.jpg')
    
    
    page5 = discord.Embed (
        title = '      __Help Page 5/5__',
        description = f"       Void's Bot's Misc. Commands\nPrefix = '_'\n**COMMANDS**",
        colour = discord.Colour.green()
    )
    page5.add_field(name='``anime  ``', value='Sends a random post from the ``r/anime`` subreddit', inline=False)
    page5.add_field(name='``aquote  ``', value='Sends a random quote from an anime', inline=False)
    page5.add_field(name='``toss  ``', value='Tosses the coin for you', inline=False)
    page5.add_field(name='``roll  ``', value='Rolls the dice for you', inline=False)
    page5.add_field(name='``wink  ``', value=';)', inline=False)
    page5.add_field(name='``wave  ``', value='👋', inline=False)
    page5.add_field(name='``uselessfact  ``', value='Sends a useless fact', inline=False)
    page5.add_field(name='``giveaway  ``', value='Starts the giveaway set up', inline=False)
    page5.add_field(name='``covid  ``', value='View the covid details of any country', inline=False)
    page5.add_field(name='``dm  ``', value='DM a user', inline=False)
    page5.add_field(name='``ping  ``', value='Check the latency', inline=False)
    page5.add_field(name='``pfp  ``', value="See anyone's profile picture", inline=False)
    page5.set_author(name = f'{bot.user.name}',icon_url='https://media.discordapp.net/attachments/805723485372284932/912702901841981470/1634727211621.jpg')

    pages = [page1, page2, page3, page4, page5]

    message = await ctx.send(embed = page1)
    await message.add_reaction('⏮')
    await message.add_reaction('◀')
    await message.add_reaction('▶')
    await message.add_reaction('⏭')

    def check(reaction, user):
        return user == ctx.author

    i = 0
    reaction = None

    while True:
        if str(reaction) == '⏮':
            i = 0
            await message.edit(embed = pages[i])
        elif str(reaction) == '◀':
            if i > 0:
                i -= 1
                await message.edit(embed = pages[i])
        elif str(reaction) == '▶':
            if i < 4:
                i += 1
                await message.edit(embed = pages[i])
        elif str(reaction) == '⏭':
            i = 4
            await message.edit(embed = pages[i])
        
        try:
            reaction, user = await bot.wait_for('reaction_add', timeout = 30.0, check = check)
            await message.remove_reaction(reaction, user)
        except:
            break

    await message.clear_reactions()

@bot.command(aliases = ["rich"])
async def leaderboard(ctx,x = 1):
    users = await get_eco_data()
    leader_board = {}
    total = []
    for user in users:
        name = int(user)
        total_amount = users[user]["wallet"] + users[user]["bank"]
        leader_board[total_amount] = name
        total.append(total_amount)

    total = sorted(total,reverse=True)    

    em = discord.Embed(title = f"Top {x} Richest People" , description = "This is decided on the basis of raw money in the bank and wallet",color = discord.Color(0xfa43ee))
    index = 1
    for amt in total:
        id_ = leader_board[amt]
        member = bot.get_user(id_)
        name = member.name
        em.add_field(name = f"{index}. {name}" , value = f"{amt}",  inline = False)
        if index == x:
            break
        else:
            index += 1

    await ctx.send(embed = em)



#---------------------------------------calculator------------------------------------------------------------------------------------------------------------------------------------------------

#


#---------------------------------------helper-functions------------------------------------------------------------------------------------------------------------------------------
async def open_account(user):
    users = await get_eco_data()
   
    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]['wallet'] = 0
        users[str(user.id)]['bank'] = 100
    with open("bank.json","w") as f:
        json.dump(users, f,indent=4)
    return True

async def get_eco_data():
    with open("bank.json","r") as f:
        users = json.load(f)
    return users
    
    
async def update_bank(user, change = 0,mode = 'wallet'):
    users =  await get_eco_data()
    users[str(user.id)][mode] += change

    with open("bank.json" ,"w") as f:
        json.dump(users, f,indent=4)

    bal = [users[str(user.id)]["wallet"],users[str(user.id)]["bank"]]
    return bal

def convert(time):
    pos = ["s", "m", "h", "d", "w"]
    time_dict = {"s": 1, "m": 60, "h": 3600, "d": 3600 * 24, "w": 3600 * 24 * 7}
    unit = time[-1]

    if unit not in pos:
        return -1
    try:
        val = int(time[:-1])
    except:
        return -2

    return val * time_dict[unit]

reac_data= []
@bot.event
async def on_reaction_add(reaction, user):
    channel = reaction.message.channel

    i = 0

    if str(reaction.emoji) == ':cookie:' and user != bot.user:
        print(reac_data)

        if user.name in reac_data:

            i += 1
        else:
            print(user.name)
            reac_data.append(user.name)


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(title=f"Hang on! Command On Cooldown...", description=f"Try again in {error.retry_after:.1f}s.")
        await ctx.reply(embed=em)

@bot.command()
@commands.is_owner()
async def shutdown(ctx):
    await ctx.send('`shutting down the bot....`')
    await ctx.bot.logout()

bot.run(TOKEN)
