from pyrogram import Client, filters

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

API_ID = 7407598 
API_HASH = '6e6622a5e352ee0c86cc558ca1c17de3'
BOT_TOKEN = '2022969489:AAGKy72Yka8Ut1jSlnj34YKgqdNImTrob8o'

bot = Client("Hasiya Bot",
             api_hash=API_HASH,
             api_id=API_ID,
             bot_token=BOT_TOKEN)

@bot.on_message(filters.command(commands=['hasiya']))
async def welcome(client, message):
    await bot.send_message(chat_id=message.chat.id, text="Hi...")
    
@bot.on_message(filters.command(commands=['wh']))
async def help(client, message):
    await bot.send_message(chat_id=message.chat.id, text="Just send me some messages and enjoy")
    
@bot.on_message(filters.command(commands=['bot']))
async def help(client, message):
    await bot.send_message(chat_id=message.chat.id, text="Online 😎")
    
    
@bot.on_message(filters.command(commands=['You Tube']))
async def help(client, message):
    await bot.send_message(chat_id=message.chat.id, text="Gaming Hasiya You Tube Channel Link.\n https://www.youtube.com/c/GamingHasiyaYouTube")
   
  
@bot.on_message(filters.command(commands=['yt']))
async def help(client, message):
    await bot.send_message(chat_id=message.chat.id, text="🤗 Hi I am HASINDU'S ASSISTANT BOT 🌐 Tech Wide Group :- https://t.me/TECH_WIDE_GROUP")

    
@bot.on_message(filters.command(commands=['About']))
async def help(client, message):
    await bot.send_message(chat_id=message.chat.id, text="👨‍💻 Hasiya Helper 👨‍💻 - I am Hasindu's Helper Bot\n🇱🇰 Bot Made By Hasindu Himasara 🇱🇰")
    
@bot.on_message(filters.command(commands=['start']))
async def help(client, message):    
    await message.reply_photo(photo='https://telegra.ph/file/f3454e8977521dc89dede.jpg',caption='🤗 Hi I am Hasiya LK Bot\n🌐 Tech Wide Group :- https://t.me/TECH_WIDE_GROUP\n🔰 Tech Wide Channel :- https://t.me/TECH_WIDE_OFFICIAL\nStay Safe',reply_markup=keyboard) 

keyboard = InlineKeyboardMarkup( 
             [ 
                           [InlineKeyboardButton( text="TECH WIDE", url="https://t.me/TECH_WIDE_GROUP")
                           ] 
            ] 
)


@bot.on_message(filters.command(commands=['help']))
async def help(client, message):    
    await message.reply_photo(photo='https://telegra.ph/file/283b6a1bcefa6af1919f3.jpg',caption='I am Online ✅',reply_markup=keyboard) 

keyboard = InlineKeyboardMarkup( 
             [ 
                           [InlineKeyboardButton( text="TECH WIDE", url="https://t.me/TECH_WIDE_GROUP")
                           ] 
            ] 
)



bot.run() 
