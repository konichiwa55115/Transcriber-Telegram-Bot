import os
from pyrogram import Client, filters
import subprocess
bot = Client(
    "myfirs",
    api_id=17983098,
    api_hash="ee28199396e0925f1f44d945ac174f64",
    bot_token="5782497998:AAEf0sdg9W84-8AhODyR9KrDGjmWGlkipvs"
)
@bot.on_message(filters.command('start') & filters.private)
def command1(bot,message):
    bot.send_message(message.chat.id, " السلام عليكم أنا بوت تفريغ صوتيات , فقط أرسل الصوتية هنا\n\n  لبقية البوتات هنا \n\n https://t.me/ibnAlQyyim/1120 ",disable_web_page_preview=True)
@bot.on_message(filters.command('clear') & filters.private)
def command1(bot,message):
    bot.send_message(message.chat.id, " تم الإخلاء ",disable_web_page_preview=True)
    subprocess.call(['rm','-r',"./downloads/"])   
    
@bot.on_message(filters.private & filters.incoming & filters.audio )
def _telegram_file(client, message):
  if os.path.isdir("./downloads/") :
        sent_message = message.reply_text('هناك عملية يتم الآن . أرسل الصوتية  بعد مدة من فضلك', quote=True)
        return
  else :
        pass
  user_id = message.from_user.id 
  sent_message = message.reply_text('جار التفريغ ', quote=True)
  file = message.audio
  file_path = message.download(file_name="./downloads/")
  head, tail = os.path.split(file_path)

    # Execute speech.py script with entry file
  subprocess.call(['python3', 'speech.py', 'RK3ETXWBJQSMO262RXPAIXFSG6NH3QRH', file_path, tail+".txt"])
    # Upload transcription file to user
  with open(tail+".txt", 'rb') as f:
        bot.send_document(message.chat.id, f)
  subprocess.call(['rm', tail+".txt" ])  
  subprocess.call(['rm', "-r",head ])
 
@bot.on_message(filters.private & filters.incoming & filters.voice )
def _telegram_file(client, message):


  if os.path.isdir("./downloads/") :
        sent_message = message.reply_text('هناك عملية يتم الآن . أرسل الصوتية  بعد مدة من فضلك', quote=True)
        return
  else :
        pass
  user_id = message.from_user.id 
  sent_message = message.reply_text('جار التفريغ ', quote=True)
  file = message.audio
  file_path = message.download(file_name="./downloads/")
  head, tail = os.path.split(file_path)

    # Execute speech.py script with entry file
  subprocess.call(['python3', 'speech.py', 'RK3ETXWBJQSMO262RXPAIXFSG6NH3QRH', file_path, tail+".txt"])
    # Upload transcription file to user
  with open(tail+".txt", 'rb') as f:
        bot.send_document(message.chat.id, f)
  subprocess.call(['rm', tail+".txt" ])  
  subprocess.call(['rm', "-r",head ])

bot.run()
