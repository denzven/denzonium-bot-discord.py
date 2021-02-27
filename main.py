#welcome fellow botdev/coder, hope you are fine and find my python module helpfull
#this is a part of my denzonium bot if you want to invite it to your server 
# https://dsc.gg/denzonium_bot
# goto to this link and invite :)



#######################################
#this imports all the nenecessary modules and stuff thats necessary...
import discord
import os
import alexflipnote
from discord.ext import commands
import random
from keep_alive import keep_alive
import wikipedia
from youtube import GetYoutubeVideo
from discord_slash import SlashCommand, SlashContext
import asyncio



###################################
#this sets all the variable and values required
defaults = os.listdir()
description = 'description'
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix= '+', description=description, intents=intents)
alex_api = alexflipnote.Client(os.getenv("apitoken"))
cogs = ["on_message"]
slash = SlashCommand(bot)

#####################################
#bot event... basically tells you the bot has started 
#and shows affirimation to the console
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    print("The bot is ready!")
    for cog in cogs:
        try:
            bot.load_extension(cog)
            print(f"{cog} was loaded.")
        except Exception as e:
            print(e)


######################################
#all the bot commands.. 👇
###################################
#sets prefix (of ONLY discord.py module)
@bot.command("prefix", help="Set Prefix")
async def setprefix(ctx, *p):
  bot.command_prefix = p
  await ctx.send(f"Prefix of discord .py module set as {p} successfully!")
  pass


#################################
#ping of discord.py module
@bot.command()
async def ping(ctx):
    """ping of the module"""
    await ctx.send(f'ping of discord.py module----> {round(bot.latency*1000)}ms')

"""
###############################
#command error.. (ONLY of discord.py module)
@bot.event
async def on_command_error(ctx,error):
    errorlst = ["pls try again the command","encountered an error pls try again","couldn't find that command","sorry command request couldnt be processed","pls try again","pls check if the command is correct or not","error"]
    error = (random.choice(errorlst))
    await ctx.send(error)

	#this is commented out before it was a bit interfering to other modules
"""

##################################
#roll dice NdN format
@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)


########################################
#8ball
@bot.command(aliases=["8ball"])
async def _8ball(ctx, *,question):
    """8ball gives opinion about the said question"""
    responses=[ 'As I see it, yes.',
  'Ask again later.',
  'Better not tell you now.',
  'Cannot predict now.',
  'Concentrate and ask again.',
  'Don’t count on it.',
  'It is certain.',
  'It is decidedly so.',
  'Most likely.',
  'My reply is no.',
  'My sources say no.',
  'Outlook not so good.',
  'Outlook good.',
  'Reply hazy, try again.',
  'Signs point to yes.',
  'Very doubtful.',
  'Without a doubt.',
  'Yes.',
  'Yes – definitely.',
  'You may rely on it.']
    await ctx.send (f'{random.choice(responses)}')

###################################
#spam command (limit of messages is 69{nice} and can spam mentions too!)

@bot.command()
async def spam(ctx, content: str, times: int):
    """you know what spam means lol."""
    if times >= 69:
        await ctx.send("too many messages!! try something lower... the limit is 69!") 
    else:
        for i in range(times):
            await ctx.send(content)
'''
@bot.command()
async def spam(ctx, content: str, times: int):
    """you know what spam means lol."""
    a = 1
    if times >= 69:
        await ctx.send("too many messages!! try something lower... the limit is 69!") 
    else:
        while a<=times:
            await ctx.send(content)
            asyncnio.sleep(0.1)
            a = a+1
'''



###############################################
#alexflipnote api with result as strings
#you must have a alexflpinote api key to work
@bot.command()#cat
async def cat(ctx):
    """gives you a cute cat image!"""
    catimg = await alex_api.cats()
    await ctx.send(catimg)
    
@bot.command()#fml
async def fml(ctx):
    """gives you an incident that fvked mah life forever""" 
    fmlimg = await alex_api.fml()
    await ctx.send(fmlimg)

@bot.command()#dog
async def dog(ctx):
    """shows you a image of a cute doggo"""
    dogimg = await alex_api.dogs()
    await ctx.send(dogimg)

@bot.command()#poorly_photoshopped_sadcat
async def sadcat(ctx):
    """ image of a sad cat UwU"""
    sadcatimg = await alex_api.sadcat()
    await ctx.send(sadcatimg)
@bot.command()
async def birb(ctx):
    """gives a birb image"""
    birbimg = await alex_api.birb()
    await ctx.send(birbimg)


#####################################################
#alexflipnote api with images as result
#must hav a alexflipnote api key for this
@bot.command()
async def achievement(ctx, text: str, icon = None): 
    """shows an minecraft achachievement card"""
    image = await alex_api.achievement(text=text, icon=icon)
    image_bytes = await image.read()
    file = discord.File(image_bytes, "achievement.png")
    await ctx.send(f"Rendered by {ctx.author}", file=file)


######################################################
#ronibot
class MyHelpCommand(commands.MinimalHelpCommand):
    async def send_pages(self):
        destination = self.get_destination()
        e = discord.Embed(color=discord.Color.blurple(), description='')
        for page in self.paginator.pages:
            e.description += page
        await destination.send(embed=e)
		
bot.help_command = MyHelpCommand()

#######################################
#wiki
@bot.command("wiki", help="Fetch the summary from wikipedia page")
async def wiki(ctx, *query):
  search = ''.join(query)
  search = search.strip()
  try :
    results = wikipedia.summary(search, sentences=2)
    await ctx.send(f"Results for {search}!")
    await ctx.send(results)
    await ctx.send(f"Wikipedia page url {wikipedia.page(search).url}")
  except Exception as e:
    await ctx.send("Specify please!")
    print(e)
  pass


#########################################
#yt
@bot.command("yt", help="Returns the link of a youtubvideo")
async def youtube(ctx, *query):
  result = GetYoutubeVideo(' '.join(query))
  await ctx.send(f"Link https://www.youtube.com/watch\?v={result}")
  pass


#######################################
#calculate
@bot.command(aliases=("calc", "c"), help="Calculate")
async def calculate(ctx, operation,a:float, b:float):
  op = "".join(operation).lower()
  result = 0.0
  if op == "add" or op == "sum" or op=="+":
    result = a+b
    pass
  elif op=="mult" or op=="*" or op=="x":
    result = a*b
    pass
  elif op=="div" or op=="/" or op=="by":
    result = a/b
    pass
  elif op=="sub" or op=="-" or op=="minus":
    result = a-b
    pass
  await ctx.send(f"Heres your answer {ctx.author.name}")
  await ctx.send(result)
  pass


###########################################
#kick
@bot.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    try:
        await member.kick(reason=reason)
        await ctx.send(f'User {member} has kicked by {ctx.author.name}.')
    except Exception as e:
        await ctx.send("No member found with that name!")
        print(e)
    pass

############################################################
#bm it sends a dm to remenber a thing
@bot.command("bm", help="Send something to yourself fomemory")
async def bookmark(ctx, *message):
    await ctx.message.author.send("Remember this:" + f"{message}")


#############################################
#info of mentioned member 
@bot.command("info", help="Get info of a certaimember")
async def info(ctx, member:discord.Member=None):
    joined = member.created_at.strftime("%b %d, %Y")
    member_id = member.id
    pfp = member.avatar_url
    embed = discord.Embed(title=f"{member}", description=f'Name: {member.name}\n User Id{member_id}\n Joined at: {joined}')
    embed.set_image(url=pfp)
    await ctx.send(embed=embed)
    pass




@slash.slash(name="test", description = "test" , guild_ids= [756596083458703530])
async def _test(ctx: SlashContext):
    await ctx.send(content="test")



########################################################
keep_alive()
bot.run(os.getenv("BOTTOKEN"))
#######################################################