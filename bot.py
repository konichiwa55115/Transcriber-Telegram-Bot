from pyrogram import Client, filters
bot = Clinet(
    api_id= ,
    api_hash= ,
    bot_token= 
)
@bot.on_message(filters.command('start') & filters.private)
def command1(bot,message):
    bot.send_message(message.chat.id, " السلام عليكم أنا بوت تفريغ صوتيات , فقط أرسل الصوتية هنا ")
bot.run()
