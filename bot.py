from pyrogram import Client, filters
bot = Client(
    "myfirs",
    api_id=17983098,
    api_hash="ee28199396e0925f1f44d945ac174f64",
    bot_token="5714654934:AAFm0UBvzuU1X-Adg7QThWCzpoKBww9SNXE"
)
@bot.on_message(filters.command('start') & filters.private)
def command1(bot,message):
    bot.send_message(message.chat.id, " السلام عليكم أنا بوت تفريغ صوتيات , فقط أرسل الصوتية هنا ")
    
@bot.on_message(filters.private & filters.incoming & filters.audio )
def _telegram_file(client, message):
  user_id = message.from_user.id
  sent_message = message.reply_text('🕵️Checking File...', quote=True)
  file = message.audio
  LOGGER.info(f'Download:{user_id}: {file.file_id}')
  file_path = message.download(file_name=DOWNLOAD_DIRECTORY)

bot.run()
