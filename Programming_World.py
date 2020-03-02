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
                await ctx.author.send("Lovely, you found the third easter egg! To gain your role, simply go in **OWNER**'s dm and type this:\n9314")
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
    await Channel.send(f'{before.author} just edited "{before.content}" to "{after.content}" in {before.channel.mention}')


@bot.event
async def on_message_delete(ctx):
    if ctx.author.bot:
        return
    Channel = bot.get_channel(682521280859340802)
    await Channel.send(f"<@{ctx.author.id}>'s message is just deleted \"{ctx.content}\" in <#{ctx.channel.id}>")


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
    embed.set_footer(text="Created By Nice Boy#3542")
    await ctx.send(embed=embed)


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


bot.run("NjgzMjk4NDUxMDMwNTQwMzI5.Xlw01A.ByZwq-1ZBip8yZIH5E0dRybCBfQ")
