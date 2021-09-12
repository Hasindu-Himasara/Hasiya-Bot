from pyrogram import Client, filters

API_ID = 7407598 
API_HASH = '6e6622a5e352ee0c86cc558ca1c17de3'
BOT_TOKEN = '1935913054:AAFMHhHsp6PIys3LTWPPa9Re7IRNse2HKNs'

bot = Client(
    'Hasiya-Bot',
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@bot.on_message(filters.command(commands=['start']))
async def start(client, filters):
    bot.send_message(chat_id=message.chat.id, text="Hi, How are you? I'm Hasindu's bot.\n Send me some messages.....")
    
@bot.on_message(filters.command(commands=['help']))
async def start(client, filters):
    bot.send_message(chat_id=message.chat.id, text="Just send me some messages and enjoy")

bot.run()
