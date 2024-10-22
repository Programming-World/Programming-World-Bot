import discord
from discord.ext import commands
from time import perf_counter
bot = commands.Bot(command_prefix="pw! ")


@bot.event
async def on_ready():
    print(f"Connected to the bot\nName and Tag: {bot.user}\nID: {bot.user.id}")
    # await bot.change_presence(activity=discord.Streaming(name="My Stream", url=my_twitch_url))


@bot.event
async def on_message(message):
    await bot.process_commands(message)
    if message.channel.id == 682609211582316616:
        if not message.author.bot:
            if message.content.lower() == "linux":
                await message.author.send("Lovely, you found the first easter egg! To gain your role, simply go in **OWNER**'s dm and type this:\n129142124")
            elif message.content.lower() == "short_code":
                await message.author.send("Lovely, you found the second easter egg! To gain your role, simply go in **OWNER**'s dm and type this:\n19815182031545")
            elif message.content.lower() == "icn":
                await message.author.send("Lovely, you found the third easter egg! To gain your role, simply go in **OWNER**'s dm and type this:\n9314")
            elif message.content.lower() == "682997703101382679":
                await message.author.send("Lovely, you found the fourth easter egg! To gain your role, simply go in **OWNER**'s dm and type this:\n142113251819")
            await message.channel.purge(limit=1)


@bot.event
async def on_message_edit(before, after):
    if before.author.id == bot.user.id:
        return
    if before.content == after.content:  # to avoid any duplicates
        return
    Channel = bot.get_channel(682521280859340802)
    Embed = discord.Embed(title="A message was edited!", color=0xFFA500)
    Embed.add_field(name="Author", value=before.author.mention, inline=False)
    Embed.set_thumbnail(url=before.author.avatar_url)    
    Embed.add_field(name="Message before being edited", value=before.content, inline=False)
    Embed.add_field(name="Message after being edited", value=after.content, inline=False)
    Embed.add_field(name="Channel", value=before.channel.mention, inline=False)
    Embed.set_footer(text="Posted by Programming World#8930")
    await Channel.send(embed=Embed)


@bot.event
async def on_message_delete(ctx):
    if ctx.author.bot:
        return
    Channel = bot.get_channel(682521280859340802)
    Embed = discord.Embed(title="A message was deleted!", color=0xFF0000)
    Embed.add_field(name="Author", value=ctx.author.mention, inline=False)
    Embed.set_thumbnail(url=ctx.author.avatar_url)
    Embed.add_field(name="Message", value=ctx.content, inline=False)
    Embed.add_field(name='Channel', value=ctx.channel.mention, inline=False)
    Embed.set_footer(text="Posted by Programming World#8930")
    await Channel.send(embed=Embed)


@bot.command()
async def Activity(ctx, message, description=" ", link=""):
    if message.lower() == "play":
        await bot.change_presence(activity=discord.Game(name=f"{description}"))
    elif message.lower() == "watch":
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{description}"))
    elif message.lower() == "listen":
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f"{description}"))
    elif message.lower() == "stream":
        if link.startswith("https://"):
            await bot.change_presence(activity=discord.Streaming(name=message, url=link))
        else:
            await ctx.send("Pls enter a **VALID** link")


@bot.command()
async def clear(ctx, amount):
    if amount == "all":
        await ctx.channel.purge()
    else:
        try:
            await ctx.channel.purge(limit=int(amount) + 1) #To remove command usage too!
        except Exception:
            await ctx.send("Pls enter a valid option!\n1. A number\n2. all")

            
@bot.command(aliases=["gr"])
async def get_role(ctx, role=None):
    Role = False
    if role is not None:
        if role.lower() == "announcements":
            Role = ctx.guild.get_role(683802971636760605)
        elif role.lower() == "challenges":
            Role = ctx.guild.get_role(683025080728682557)
        elif role.lower() == "ler":
            Role = ctx.guild.get_role(683025080653316150)
        elif role.lower() == "plotd":
            Role = ctx.guild.get_role(683025080649121857)
    if Role:
        await ctx.author.add_roles(Role)
        await ctx.send("Your role is given!")
    else:
        await ctx.send("Pls choose from these options:\n1. Announcements\n2. Challenges\n3. LER\n4. PLOTD")


@bot.command()
async def ping(ctx):
    start = perf_counter()
    message = await ctx.send("Ping...")
    end = perf_counter()
    duration = (end - start) * 1000
    await message.edit(content=f"Pong! {ctx.author.mention} {duration:.2f}")
    

@bot.command()
async def Ready(ctx):
    await ctx.send("I'm Ready!")

    
@bot.command(aliases=["rr"])
async def remove_role(ctx, role=None):
    Role = False
    if role is not None:
        if role.lower() == "announcements":
            Role = ctx.guild.get_role(683802971636760605)
        elif role.lower() == "challenges":
            Role = ctx.guild.get_role(683025080728682557)
        elif role.lower() == "ler":
            Role = ctx.guild.get_role(683025080653316150)
        elif role.lower() == "plotd":
            Role = ctx.guild.get_role(683025080649121857)
    if Role:
        await ctx.author.remove_roles(Role)
        await ctx.send("Your role is removed!")
    else:
        await ctx.send("Pls choose from these options:\n1. Announcements\n2. Challenges\n3. LER\n4. PLOTD")


@bot.command(name="user-info", aliases=['ui'])
async def userinfo(ctx, member: discord.Member = None):
    member = member or ctx.author
    embed = discord.Embed(title=member.name, description=member.mention, color=0x008000)
    embed.add_field(name="Created at", value=member.created_at, inline=False)
    embed.add_field(name="ID", value=member.id, inline=False)
    embed.add_field(name='Join Date', value=member.joined_at, inline=False)
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text="Posted by Programming World#8930")
    await ctx.send(embed=embed)

bot.run("NjgyMzI1MzY3MTYzNDUzNDQ4.XlzCmQ.KbftbJV2THngb8S6BRbqYDoqxIE")
