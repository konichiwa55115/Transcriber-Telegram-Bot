import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup , InlineKeyboardButton , ReplyKeyboardMarkup , CallbackQuery
import subprocess
bot = Client(
    "transcribebot",
    api_id="**************",
    api_hash="*****************",
    bot_token="*****************"
)

#Fill vars with your own id , hash and token 

CHOOSE_UR_LANG = " Choose Your Language ! "
CHOOSE_UR_LANG_BUTTONS = [
    [InlineKeyboardButton("AR",callback_data="AR")],
     [InlineKeyboardButton("EN",callback_data="EN")],
     [InlineKeyboardButton("TR",callback_data="TR")],
     [InlineKeyboardButton("FR",callback_data="FR")],
     [InlineKeyboardButton("JA",callback_data="JA")],
     [InlineKeyboardButton("GE",callback_data="GE")]
]



@bot.on_message(filters.command('start') & filters.private)
def command1(bot,message):
    bot.send_message(message.chat.id, " Hi there , I'm a simple Telegram bot to transcribe audios/videos , just send/forward any media ",disable_web_page_preview=True)

    
@bot.on_message(filters.private & filters.incoming & filters.audio | filters.voice | filters.video | filters.document )
def _telegram_file(bot, message):
  try: 
    with open("myfile.txt", 'r') as fh:
      
            sent_message = message.reply_text(" There's a Transcription Process running right now ! \n\n Plz, send media after a while !" , quote=True)
            return
  except FileNotFoundError: 
    pass  
    f = open("myfile.txt", "x")

  global user_id
  user_id = message.from_user.id 
  file = message.audio
  global file_path
  file_path = message.download(file_name="./downloads/")
  filename = os.path.basename(file_path)
  head, tail = os.path.split(file_path)
  file, ext = os.path.splitext(tail)
  global mp3file
  mp3file= file+".mp3"
  global result
  result = file+".txt"
  message.reply(
             text = CHOOSE_UR_LANG,
             reply_markup = InlineKeyboardMarkup(CHOOSE_UR_LANG_BUTTONS)

        )
@bot.on_callback_query()
def callback_query(CLIENT,CallbackQuery):
  global langtoken
  if CallbackQuery.data == "AR":
      langtoken = "RK3ETXWBJQSMO262RXPAIXFSG6NH3QRH"
  elif CallbackQuery.data == "EN":
      langtoken = "2OVHUDKLF33Z44DOOX7GBAWEL5GOXI3Z"
  elif CallbackQuery.data == "TR":
      langtoken = "25LMC6WPQBFURJTCECAU3O3BIWIV4PGT"
  elif CallbackQuery.data == "FR" :
      langtoken = "AMORHRXGFFALYGUR23MVHVWJKHJIH53T"
  elif CallbackQuery.data == "GE":
      langtoken = "UEK2TR23J5ECLC6L6BI5YNHN5MBC4Q6U"
  elif CallbackQuery.data == "JA":
      langtoken = "BCDCJOEWUAGWQZTHX4QGSXGWLO5CWV5Z" 
  CallbackQuery.edit_message_text(
      
      "Transcribing ....."
  )   
  subprocess.call(['ffmpeg', '-i',file_path,'-q:a','0','-map','a',mp3file,'-y' ])
  subprocess.call(['python','speech.py',langtoken,mp3file,result])
  with open(result, 'rb') as f:
        bot.send_document(user_id, f)
        subprocess.call(['unlink',"myfile.txt"])  
        subprocess.call(['unlink',mp3file])  
        subprocess.call(['unlink',result])  

bot.run()
