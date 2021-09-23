from pyrogram import Client, filters

API_ID = 7407598 
API_HASH = '6e6622a5e352ee0c86cc558ca1c17de3'
BOT_TOKEN = '1993601562:AAGQDgbhPdHh5HkGzW4TLVC4gBJaJiTGmC8'

bot = Client("Hasiya Bot",
             api_hash=API_HASH,
             api_id=API_ID,
             bot_token=BOT_TOKEN)

@bot.on_message(filters.command(commands=['hasiya']))
async def welcome(client, message):
    await bot.send_message(chat_id=message.chat.id, text="Hi...")
    
@bot.on_message(filters.command(commands=['help']))
async def help(client, message):
    await bot.send_message(chat_id=message.chat.id, text="Just send me some messages and enjoy")
    
@bot.on_message(filters.command(commands=['bot']))
async def help(client, message):
    await bot.send_message(chat_id=message.chat.id, text="Online 😎")
    
    
@bot.on_message(filters.command(commands=['You Tube']))
async def help(client, message):
    await bot.send_message(chat_id=message.chat.id, text="Gaming Hasiya You Tube Channel Link.\n https://www.youtube.com/c/GamingHasiyaYouTube")
    
    
@bot.on_message(filters.command(commands=['start']))
async def help(client, message):
    await bot.send_message(chat_id=message.chat.id, text="💫 Hi i am Hasindu Helper\n🔥 Bot made by Hasindu Himasara\n ♻️ 24 Hour Active\n Contact By @Hasindu_Himasara\n  අපගේTelegram Account එකක් පාළනයෙන් ගිලිහී ගොස් ඇත./nඑම නිසා මෙම Telegram Account එකට මැසේජ් දමිය හැක.")
    
    
@bot.on_message(filters.command(commands=['About']))
async def help(client, message):
    await bot.send_message(chat_id=message.chat.id, text="👨‍💻 Hasiya Helper 👨‍💻 - I am Hasindu's Helper Bot\n🇱🇰 Bot Made By Hasindu Himasara 🇱🇰")
    
    
bot.run() 
