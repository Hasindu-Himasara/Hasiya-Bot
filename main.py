from pyrogram import Client, filters

API_ID = 7407598 
API_HASH = '6e6622a5e352ee0c86cc558ca1c17de3'
BOT_TOKEN = '1993601562:AAGQDgbhPdHh5HkGzW4TLVC4gBJaJiTGmC8'

bot = Client("Hasiya Bot",
             api_hash=API_HASH,
             api_id=API_ID,
             bot_token=BOT_TOKEN)

@bot.on_message(filters.command(commands=['start']))
async def welcome(client, message):
    await bot.send_message(chat_id=message.chat.id, text="Hi, How are you? I'm Hasindu's bot.\n Send me some messages.....")
    
@bot.on_message(filters.command(commands=['help']))
async def help(client, filters):
    await bot.send_message(chat_id=message.chat.id, text="Just send me some messages and enjoy")
    
    @bot.on_message(filters.command(commands=['hasiya']))
async def start(client, filters):
    await bot.send_message(chat_id=message.chat.id, text="I Am Hasiya's Bot")
    
bot.run() 
