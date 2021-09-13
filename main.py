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
    await bot.send_message(chat_id=message.chat.id, text="♻️ COVID 19 UPDATES BOT ♻️ - @Covid_19_Updates_SL_Bot

ᴘʜᴏᴛᴏ ᴇᴅɪᴛᴏʀ ʟᴋ - @Photo_Editor_LK_Bot

ᴛᴇᴄʜ ᴡɪᴅᴇ ʙᴏᴛ ᴘᴏᴡᴇʀᴅ ʙʏ ʜᴀsɪʏᴀ - @Hasiya_Tech_Bot

HASIYA MUSIC - @Music_Downloder_By_Hasiya_Bot

All Bots Made By - @HASIYA_GEEK
😉 Made BY Hasiya 😉")
    
    
    
   
bot.run() 
