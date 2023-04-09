from pyrogram import Client, filters
bot = Clinet(
    api_id= ,
    api_hash= ,
    bot_token= 
)
@bot.on_message(filters.command('start') & filters.private)
def command1(bot,message):
    bot.send_message(message.chat.id, " السلام عليكم أنا بوت تفريغ صوتيات , فقط أرسل الصوتية هنا ")
    
@bot.on_message(filters.private & filters.incoming & filters.audio )
def _telegram_file(client, message):
  user_id = message.from_user.id
  sent_message = message.reply_text('🕵️Checking File...', quote=True)
  file = message.audio
  sent_message.edit(Messages.DOWNLOAD_TG_FILE.format(file.file_name, humanbytes(file.file_size), file.mime_type))
  LOGGER.info(f'Download:{user_id}: {file.file_id}')
  try:
    file_path = message.download(file_name=DOWNLOAD_DIRECTORY)
    sent_message.edit(Messages.DOWNLOADED_SUCCESSFULLY.format(os.path.basename(file_path), humanbytes(os.path.getsize(file_path))))
  with open('entry.mp3', 'wb') as f:
      f.write(audio_file)
    # Execute speech.py script with entry file
  subprocess.call(['python', 'speech.py', 'RK3ETXWBJQSMO262RXPAIXFSG6NH3QRH', 'entry.mp3', 'transcription.txt'])
    # Upload transcription file to user
  with open('transcription.txt', 'rb') as f:
      bot.send_document(message.chat.id, f)  
    
    
bot.run()
