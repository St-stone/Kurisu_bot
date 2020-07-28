import discord,json,random,time,sys,os,asyncio,math
from discord.ext import commands
from datetime import datetime
from discord.ext import commands
from discord.utils import get
from keep_alive import keep_alive
bot = commands.Bot(command_prefix='!')


@bot.event  #登入成功
async def on_ready():
  print('Logged in as')
  print(bot.user.name)
  print(bot.user.id)
  print('------')
  mydict = {'sec': "0"}
  file = "wait.json"
  with open(file, 'w', encoding='utf-8') as f:
    json.dump(mydict, f)
  
@bot.command()  #註冊
async def 註冊(message,name:str):
  filename = 'data.json'
  with open(filename, 'r', encoding='utf-8') as file:
    data = json.load(file)
    if (str(message.author.id) in str(data)):
      await message.channel.send('<@' + str(message.author.id) +'> 您已經註冊過了')
    else:
      if (str(name) in str(data)):
        await message.channel.send("這暱稱已經有人使用了")
        return
      strid = message.author.id
      data[strid] = [name,strid,0,0] 
      #[使用者名稱,id,積分,違規]
      file = 'data.json'
      with open(file, 'w', encoding='utf-8') as f:
        json.dump(data, f)
      filename = 'Nameid.json'
      with open(filename, 'r', encoding='utf-8') as file:
        Nameid = json.load(file)
      Nameid[name] = strid
      file = 'Nameid.json'
      with open(file, 'w', encoding='utf-8') as f:
        json.dump(Nameid, f)

      filename = 'number.json'
      with open(filename, 'r', encoding='utf-8') as file:
        number = json.load(file)
      ALL = str(number["all"])
      
      ID = message.author.id
      number["all"] = int(ALL)+1
      AA = int(ALL)+1
      AA = str(AA)
      number[AA] = [str(name),int(ID)]
      
      file = 'number.json'
      with open(file, 'w', encoding='utf-8') as f:
        json.dump(number, f)

      await message.channel.send('<@' + str(message.author.id) +'> 註冊成功')
  channel = bot.get_channel(727903243341922445)
  with open("data.json", 'r', encoding='utf-8') as file:
    data = json.load(file)
  await channel.send("```data.json:\n"+str(data)+"```")
  with open("number.json", 'r', encoding='utf-8') as file:
    data = json.load(file)
  await channel.send("```number.json:\n"+str(data)+"```")
  with open("Nameid.json", encoding='utf-8') as file:
    data = json.load(file)
  await channel.send("```Nameid.json:\n"+str(data)+"```")

@bot.command()  
async def 資訊總覽(message):
  filename = 'data.json'
  with open(filename, 'r', encoding='utf-8') as file:
    data = json.load(file)
    if (str(message.author.id) in str(data)):
      strid = str(message.author.id)
      name = data[strid][0]
      userid = data[strid][1]
      point = data[strid][2]
      Irregularities = data[strid][3]
      embed = discord.Embed(title=str(name)+"帳號資訊",description="當前賽季：2020夏(7~9月)",color=750000)
      embed.add_field(name="玩家ID", value=userid, inline=False)
      embed.add_field(name="玩家積分", value=point)
      if(int(Irregularities) >= 3):
        mood = "禁賽中"
      else:
        mood = "可進行遊戲"
      embed.add_field(name="目前狀態", value=mood)
      await message.channel.send(embed=embed)
    else:
      return
  channel = bot.get_channel(727903243341922445)
  with open("data.json", 'r', encoding='utf-8') as file:
    data = json.load(file)
  await channel.send("```data.json:\n"+str(data)+"```")
  with open("number.json", 'r', encoding='utf-8') as file:
    data = json.load(file)
  await channel.send("```number.json:\n"+str(data)+"```")
  with open("Nameid.json", encoding='utf-8') as file:
    data = json.load(file)
  await channel.send("```Nameid.json:\n"+str(data)+"```")

@bot.command()  
async def 玩家資訊(message,userid:int):
  u = str(message.channel.id)
  if (str(message.author.id) == "550907252970749952"or str(message.author.id) == "544552665204654080" or str(message.author.id) == "480747560793931778"or str(message.author.id) == "352066968750260245"or str(message.author.id) == "511246631073611808"  or str(message.author.id) == "597692502346301452"):
    pass
  elif (u == '695838524813082624'):
    pass
  else:
    return
  filename = 'data.json'
  with open(filename, 'r', encoding='utf-8') as file:
    data = json.load(file)
    if (str(userid) in str(data)):
      strid = str(userid)
      name = data[strid][0]
      userid = data[strid][1]
      point = data[strid][2]
      Irregularities = data[strid][3]
      embed = discord.Embed(title=str(name)+"帳號資訊(管理員預覽模式)",description="當前賽季：2020夏(7~9月)",color=750000)
      embed.add_field(name="玩家ID", value=userid, inline=False)
      embed.add_field(name="玩家積分", value=point)
      if(int(Irregularities) >= 3):
        mood = "禁賽中"
      else:
        mood = "可進行遊戲"
      embed.add_field(name="目前狀態", value=mood)
      embed.add_field(name="警告次數(管理員模式)", value=Irregularities)
      await message.channel.send(embed=embed)
    else:
      return

@bot.command()  
async def 查詢玩家(message,name:str):
  u = str(message.channel.id)
  if (u != '695838524813082624'):
    return
  filename = 'Nameid.json'
  with open(filename, 'r', encoding='utf-8') as file:
    Nameid = json.load(file)
  if(name in str(Nameid)):
    a = Nameid[name]
    await message.channel.send(a)
  else:
    await message.channel.send("查詢不到該玩家")
  
@bot.command()  
async def 查詢(message):
  filename = 'Nameid.json'
  with open(filename, 'r', encoding='utf-8') as file:
    Nameid = json.load(file)
  await message.channel.send(Nameid)

@bot.event
async def on_reaction_add(reaction,user):
  channel = str(reaction.message.channel.id)
  if(channel == "695838524813082624" or channel == '707975877127962664'):
    pass
  else:
    return
  if(str(user.id)=="599961707607228418"):
    return
  #🇦🇧🇨🇩🇪🇫🇬🇭🇮🇯🇰
  Number = ""
  print(reaction)
  if(str(reaction) == "🇦"):
    Number = "0"
  if(str(reaction) == "🇧"):
    Number = "1"
  if(str(reaction) == "🇨"):
    Number = "2"
  if(str(reaction) == "🇩"):
    Number = "3"
  if(str(reaction) == "🇪"):
    Number = "4"
  if(str(reaction) == "🇫"):
    Number = "5"
  if(str(reaction) == "🇬"):
    Number = "6"
  if(str(reaction) == "🇭"):
    Number = "7"
  if(str(reaction) == "🇮"):
    Number = "8"
  if(str(reaction) == "🇯"):
    Number = "9"
  if(str(reaction) == "🇰"):
    Number = "10"
  filename = 'reaction.json'
  with open(filename, 'r', encoding='utf-8') as file:
    data = json.load(file)
  msgID= str(reaction.message.id)
  data[msgID] = Number
  with open(filename, 'w', encoding='utf-8') as f:
    json.dump(data, f)

  

@bot.command()  #我的資訊,message,action:str,add:int,userid:int,reason:str
async def 管理(message):
  u = str(message.channel.id)
  if (u == '695838524813082624' or u == '707975877127962664'):
    pass
  else:
    return
  filename = 'data.json'
  with open(filename, 'r', encoding='utf-8') as file:
    data = json.load(file)
    #🇦🇧🇨🇩🇪🇫🇬🇭🇮🇯🇰🇱🇲🇳🇴🇵🇶🇷🇸🇹🇺🇻🇼🇽🇾🇿
    zero = "🇦"
    one = "🇧"
    two = "🇨"
    three = "🇩"
    four = "🇪"
    five = "🇫"
    six = "🇬"
    seven = "🇭"
    eight = "🇮"
    nine = "🇯"
    ten = "🇰"

    #action
    embed = discord.Embed(title="管理模式",description="請選擇要進行的動作：",color=750000)
    embed.add_field(name="取消",value=zero)
    embed.add_field(name="增加積分",value=one)
    embed.add_field(name="扣除積分",value=two)
    embed.add_field(name="警告",value=three)
    embed.add_field(name="撤銷警告",value=four)
    msg1 = await message.channel.send(embed=embed)
    await msg1.add_reaction(zero)
    await msg1.add_reaction(one)
    await msg1.add_reaction(two)
    await msg1.add_reaction(three)
    await msg1.add_reaction(four)
    await asyncio.sleep(1)
    switch = "F"
    while(switch == "F"):
      filename = 'reaction.json'
      with open(filename, 'r', encoding='utf-8') as file:
        answer = json.load(file)
      if(str(msg1.id) in str(answer)):
        switch = "T"
        ans1 = answer[str(msg1.id)]
        del answer[str(msg1.id)]
        await msg1.delete()
        with open(filename, 'w', encoding='utf-8') as f:
          json.dump(answer, f)
      else:
        await asyncio.sleep(1)
    print(ans1)
    if(str(ans1) == "0"):
      await message.channel.send("取消成功")
      return
    elif(str(ans1) == "1"):
      action = "增加積分"
    elif(str(ans1) == "2"):
      action = "扣除積分"
    elif(str(ans1) == "3"):
      action = "警告"
    elif(str(ans1) == "4"):
      action = "撤銷警告"

    #add  
    embed = discord.Embed(title="管理模式",description="請選擇要增加/扣除的數字",color=750000)
    embed.add_field(name="取消",value=zero)
    embed.add_field(name="1",value=one)
    embed.add_field(name="2",value=two)
    embed.add_field(name="3",value=three)
    embed.add_field(name="4",value=four)
    embed.add_field(name="5",value=five)
    embed.add_field(name="6",value=six)
    embed.add_field(name="7",value=seven)
    embed.add_field(name="8",value=eight)
    embed.add_field(name="9",value=nine)
    embed.add_field(name="10",value=ten)
    msg2 = await message.channel.send(embed=embed)
    await msg2.add_reaction(zero)
    await msg2.add_reaction(one)
    await msg2.add_reaction(two)
    await msg2.add_reaction(three)
    await msg2.add_reaction(four)
    await msg2.add_reaction(five)
    await msg2.add_reaction(six)
    await msg2.add_reaction(seven)
    await msg2.add_reaction(eight)
    await msg2.add_reaction(nine)
    await msg2.add_reaction(ten)
    await asyncio.sleep(1)
    switch = "F"
    while(switch == "F"):
      filename = 'reaction.json'
      with open(filename, 'r', encoding='utf-8') as file:
        answer = json.load(file)
      if(str(msg2.id) in str(answer)):
        switch = "T"
        ans2 = answer[str(msg2.id)]
        del answer[str(msg2.id)]
        await msg2.delete()
        with open(filename, 'w', encoding='utf-8') as f:
          json.dump(answer, f)
      else:
        await asyncio.sleep(1)
    print(ans2)
    if(str(ans2) == "0"):
      await message.channel.send("取消成功")
      return
    else:
      add = int(ans2)

  #userid
    embed = discord.Embed(title="管理模式",description="請選擇玩家(頁數)",color=750000)
    filename = 'number.json'
    with open(filename, 'r', encoding='utf-8') as file:
      pagedata = json.load(file)
    pages = pagedata["all"]
    page = math.ceil(pages/10)
    embed.add_field(name="取消",value=zero)
    a=0
    while(a != page):
      v = pagedata["data"][a]
      embed.add_field(name=(a+1),value=v)
      a = a+1
    msg3 = await message.channel.send(embed=embed)
    await msg3.add_reaction(zero)
    a=0
    while(a != page):
      v = pagedata["data"][a]
      await msg3.add_reaction(v)
      a = a+1
    await asyncio.sleep(1)
    switch = "F"
    while(switch == "F"):
      filename = 'reaction.json'
      with open(filename, 'r', encoding='utf-8') as file:
        answer = json.load(file)
      if(str(msg3.id) in str(answer)):
        switch = "T"
        ans3 = answer[str(msg3.id)]
        del answer[str(msg3.id)]
        await msg3.delete()
        with open(filename, 'w', encoding='utf-8') as f:
          json.dump(answer, f)
      else:
        await asyncio.sleep(1)
    print(ans3)
    if(str(ans3) == "0"):
      await message.channel.send("取消成功")
      return
    else:
      page = int(ans3)
    
    embed = discord.Embed(title="管理模式",description="請選擇玩家",color=750000)
    filename = 'number.json'
    with open(filename, 'r', encoding='utf-8') as file:
      pagedata = json.load(file)
    pages = pagedata["all"]
    allpage = math.ceil(pages/10)
    embed.add_field(name="取消",value=zero)
    a=0
    if(allpage == page):
      ALL = pagedata["all"]
      ALL = ALL-(page-1)*10 
      print(ALL)
      while(a != ALL):
        people = str((page-1)*10+a+1)
        Name = pagedata[people][0]
        v = pagedata["data"][a]
        embed.add_field(name=Name,value=v)
        a = a+1
    else:
      ALL = 10
      while(a != ALL):
        people = str((page-1)*10+a+1)
        Name = pagedata[people][0]
        v = pagedata["data"][a]
        embed.add_field(name=Name,value=v)
        a = a+1
    msg4 = await message.channel.send(embed=embed)

    a=0
    await msg4.add_reaction(zero)
    if(allpage == page):
      ALL = pagedata["all"]
      ALL = ALL-((page-1)*10)
      while(a != ALL):
        v = pagedata["data"][a]
        await msg4.add_reaction(v)
        a = a+1
    else:
      ALL = 10
      while(a != ALL):
        v = pagedata["data"][a]
        await msg4.add_reaction(v)
        a = a+1
    await asyncio.sleep(1)
    switch = "F"
    while(switch == "F"):
      filename = 'reaction.json'
      with open(filename, 'r', encoding='utf-8') as file:
        answer = json.load(file)
      if(str(msg4.id) in str(answer)):
        switch = "T"
        ans4 = answer[str(msg4.id)]
        del answer[str(msg4.id)]
        await msg4.delete()
        with open(filename, 'w', encoding='utf-8') as f:
          json.dump(answer, f)
      else:
        await asyncio.sleep(1)
    print(ans4)
    if(str(ans4) == "0"):
      await message.channel.send("取消成功")
      return
    elif(int(ans4) <= 10):
      who = str((page-1)*10+int(ans4))
      userid = pagedata[who][1]

    #reason
    filename = 'reason.json'
    with open(filename, 'r', encoding='utf-8') as file:
      reasondata = json.load(file)
    UserName = str(message.author.name)
    embed = discord.Embed(title="管理模式",description="請選擇理由("+str(UserName)+")",color=750000)
    ID=str(message.author.id)
    embed.add_field(name="取消",value=zero)
    a=0
    while(a != 10):
      v = pagedata["data"][a]
      r=reasondata[ID][a]
      if(r == ""):
        r ="未設定"
      embed.add_field(name=r,value=v)
      a = a+1
    msg5 = await message.channel.send(embed=embed)
    await msg5.add_reaction(zero)
    await msg5.add_reaction(one)
    await msg5.add_reaction(two)
    await msg5.add_reaction(three)
    await msg5.add_reaction(four)
    await msg5.add_reaction(five)
    await msg5.add_reaction(six)
    await msg5.add_reaction(seven)
    await msg5.add_reaction(eight)
    await msg5.add_reaction(nine)
    await msg5.add_reaction(ten)
    await asyncio.sleep(1)
    switch = "F"
    while(switch == "F"):
      filename = 'reaction.json'
      with open(filename, 'r', encoding='utf-8') as file:
        answer = json.load(file)
      if(str(msg5.id) in str(answer)):
        switch = "T"
        ans5 = answer[str(msg5.id)]
        del answer[str(msg5.id)]
        await msg5.delete()
        with open(filename, 'w', encoding='utf-8') as f:
          json.dump(answer, f)
      else:
        await asyncio.sleep(1)
    print(ans5)
    if(str(ans5) == "0"):
      await message.channel.send("取消成功")
      return
    else:
      reason = reasondata[ID][int(ans5)-1]



    filename = 'data.json'
    with open(filename, 'r', encoding='utf-8') as file:
      data = json.load(file)
      
    if (str(userid) in str(data)):
      strid = str(userid)
      name = data[strid][0]
      userid = data[strid][1]
      point = data[strid][2]
      Irregularities = data[strid][3]
      channel = bot.get_channel(695834999613816873)

      if(action == "增加積分"):
        newpoint = int(point)+int(add)
        data[strid][2] = newpoint
        await channel.send("管理員`"+str(message.author.name)+"`以「"+reason+"」為理由，給予了玩家`"+name+"`"+str(add)+"積分")
      
      if(action == "扣除積分"):
        newpoint = int(point)-int(add)
        data[strid][2] = newpoint
        await channel.send("管理員`"+str(message.author.name)+"`以「"+reason+"」為理由，扣除了玩家`"+name+"`"+str(add)+"積分")
      
      if(action == "警告"):
        newIrregularities = int(Irregularities)+int(add)
        data[strid][3] = newIrregularities
        await channel.send("管理員`"+str(message.author.name)+"`以「"+reason+"」為理由，記了玩家`"+name+"`"+str(add)+"次警告")
        if(newIrregularities >= 3 and Irregularities < 3):
          banchannel = bot.get_channel(695941034613538856)
          await banchannel.send("ban <@"+str(userid)+">")
      
      if(action == "撤銷警告"):
        newIrregularities = int(Irregularities)-int(add)
        data[strid][3] = newIrregularities
        await channel.send("管理員`"+str(message.author.name)+"`以「"+reason+"」為理由，撤銷了玩家`"+name+"`"+str(add)+"次警告")
        if(newIrregularities < 3 and Irregularities >= 3):
          banchannel = bot.get_channel(695941034613538856)
          await banchannel.send("unban <@"+str(userid)+">")
      print(add)
      file = 'data.json'
      with open(file, 'w', encoding='utf-8') as f:
        json.dump(data, f)
      await message.channel.send("成功")


      
    else:
      return
  channel = bot.get_channel(727903243341922445)
  with open("data.json", 'r', encoding='utf-8') as file:
    data = json.load(file)
  await channel.send("```data.json:\n"+str(data)+"```")
  with open("number.json", 'r', encoding='utf-8') as file:
    data = json.load(file)
  await channel.send("```number.json:\n"+str(data)+"```")
  with open("Nameid.json", encoding='utf-8') as file:
    data = json.load(file)
  await channel.send("```Nameid.json:\n"+str(data)+"```")

@bot.command()
async def 抽籤(message, a: int, b: int, c: str):
    d = c
    while (str(d) in c):
        d = (random.randint(a, b))
    await message.channel.send(d)

@bot.command()
async def 設定理由(message,a:int,b:str):
  filename = 'reason.json'
  with open(filename, 'r', encoding='utf-8') as file:
    data = json.load(file)
  ID = str(message.author.id)
  data[ID][a-1] = b
  with open(filename, 'w', encoding='utf-8') as f:
    json.dump(data, f)
  await message.channel.send("成功")


@bot.command()
async def explosion(message, a: int):
  await asyncio.sleep(a)
  await message.channel.send('<@' + str(message.author.id) +'>')
  await message.channel.send("我が名はめぐみん。")
  await asyncio.sleep(2)
  await message.channel.send("紅魔族随一の魔法の使い手にして、爆裂魔法を操りし者。")
  await asyncio.sleep(4)
  await message.channel.send("我が力、見るがいい！")
  await asyncio.sleep(2)
  await message.channel.send("エクスプロージョン！")

@bot.command()
async def data(message):
  if( message.author.id == 550907252970749952):
    filename = 'data.json'
    with open(filename, 'r', encoding='utf-8') as file:
      data = json.load(file)
    await message.channel.send(data)
    
keep_alive()
bot.run(os.getenv('NjkwNTUyNzk5ODg4NjcwNzQx.XnTFaQ.RZwtz3tD-EW0dv09O_P5dY5nORY'))
