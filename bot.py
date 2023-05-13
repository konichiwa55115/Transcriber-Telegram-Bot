import os
from pyrogram import Client, filters
import subprocess
bot = Client(
    "myfirs",
    api_id=17983098,
    api_hash="ee28199396e0925f1f44d945ac174f64",
    bot_token="5998058674:AAGcy7rA5u_x87r8Nr1soEI_42y7k_WRcq8"
)
@bot.on_message(filters.command('start') & filters.private)
def command1(bot,message):
    bot.send_message(message.chat.id, " السلام عليكم أنا بوت تفريغ صوتيات , فقط أرسل الصوتية هنا\n\n  لبقية البوتات هنا \n\n https://t.me/ibnAlQyyim/1120 ",disable_web_page_preview=True)
@bot.on_message(filters.command('clear') & filters.private)
def command1(bot,message):
    bot.send_message(message.chat.id, " تم الإخلاء ",disable_web_page_preview=True)
    subprocess.call(['unlink','transcription.txt'])   
    
@bot.on_message(filters.private & filters.incoming & filters.audio )
def _telegram_file(client, message):
  try: 
    with open(' ~/trans5115text/transcription.txt', 'r') as fh:
        if os.stat(' ~/trans5115text/transcription.txt').st_size == 0: 
            pass
        else:
            sent_message = message.reply_text('هناك تفريغ يتم الآن . أرسل الصوتية بعد مدة من فضلك', quote=True)
            return
  except FileNotFoundError: 
    pass  
  user_id = message.from_user.id 
  sent_message = message.reply_text('جار التفريغ', quote=True)
  file = message.audio
  file_path = message.download(file_name="entry")

    # Execute speech.py script with entry file
  subprocess.call(['python3', 'speech.py', 'RK3ETXWBJQSMO262RXPAIXFSG6NH3QRH', "./downloads/entry" , 'transcription.txt'])
    # Upload transcription file to user
  with open('transcription.txt', 'rb') as f:
        bot.send_document(message.chat.id, f)
  subprocess.call(['unlink','transcription.txt'])   
 
@bot.on_message(filters.private & filters.incoming & filters.voice )

def _telegram_file(client, message):
  try: 
    with open(' ~/trans5115text/transcription.txt', 'r') as fh:
        if os.stat(' ~/trans5115text/transcription.txt').st_size == 0: 
            pass
        else:
            sent_message = message.reply_text('هناك تفريغ يتم الآن . أرسل الصوتية بعد مدة من فضلك', quote=True)
            return
  except FileNotFoundError: 
    pass  
  user_id = message.from_user.id
  sent_message = message.reply_text('جار التفريغ', quote=True)
  file = message.voice
  file_path = message.download(file_name="entry")

    # Execute speech.py script with entry file
  subprocess.call(['python3', 'speech.py', 'RK3ETXWBJQSMO262RXPAIXFSG6NH3QRH', "./downloads/entry" , 'transcription.txt'])
    # Upload transcription file to user
  with open('transcription.txt', 'rb') as f:
        bot.send_document(message.chat.id, f)
  subprocess.call(['unlink','transcription.txt'])      

bot.run()
