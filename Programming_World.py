import discord
from discord.ext import commands
from time import perf_counter
bot = commands.Bot(command_prefix="pw! ")


@bot.event
async def on_ready():
    print(f"Connected to the bot\nName and Tag: {bot.user}\nID: {bot.user.id}")
    # await bot.change_presence(activity=discord.Streaming(name="My Stream", url=my_twitch_url))


@bot.event
async def on_message_edit(before, after):
    if before.author.id == bot.user.id:
        return
    if before.content == after.content:  # to avoid any duplicates
        return
    Channel = bot.get_channel(682521280859340802)
    await Channel.send(f'{before.author} just edited "{before.content}" to "{after.content}" in {before.channel.mention}')


@bot.event
async def on_message_delete(ctx):
    if ctx.author.bot:
        return
    Channel = bot.get_channel(682521280859340802)
    await Channel.send(f"{ctx.author} just deleted \"{ctx.content}\" in <#{ctx.channel.id}>")


@bot.command()
async def stream(ctx, what, link):
    try:
        await bot.change_presence(activity=discord.Streaming(name=what, url=link))
        await ctx.send(f"Successfully changed streaming status to **{stream}**")
    except Exception as e:
        await ctx.send(f"error: {e}")
        return


@bot.command()
async def Activity(ctx, message, *args):
    content = " ".join(args)
    if message.lower() == "play":
        await bot.change_presence(activity=discord.Game(name=f"{content}"))
    elif message.lower() == "watch":
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{content}"))
    elif message.lower() == "listen":
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f"{content}"))
    elif message.lower() == "stream":
        await ctx.send("Pls send your url:")


@bot.command()
async def Ready(ctx):
    await ctx.send("I'm Ready!")


@bot.command()
async def Ping(ctx):
    start = perf_counter()
    message = await ctx.send("Ping...")
    end = perf_counter()
    duration = (end - start) * 1000
    await message.edit(content=f"Pong! {ctx.author.mention} {duration:.2f}")


@bot.command(aliases=['u', 'ui'])
async def userinfo(ctx, member: discord.Member = None):
    member = member or ctx.author
    embed = discord.Embed(title=member.name, description=member.mention, color=0x008000)
    embed.add_field(name="Created at", value=member.created_at, inline=False)
    embed.add_field(name="ID", value=member.id, inline=False)
    embed.add_field(name='Join Date', value=member.joined_at, inline=False)
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text="Created By Mad#2430")
    await ctx.send(embed=embed)

                  
@bot.command(name="682997703101382679")
async def _682997703101382679(ctx):
    await ctx.channel.purge(limit=1)
    await ctx.author.send("Send this in **OWNER**'s dm:\n142113251819")

bot.run("NjgyMzI1MzY3MTYzNDUzNDQ4.XldncQ.DfYV_ZmWKzbKOqokl8A3RU2xk2o")
