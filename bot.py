import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup , InlineKeyboardButton , ReplyKeyboardMarkup , CallbackQuery
from os import system as cmd
bot = Client(
    "transcribebot",
    api_id=17983098,
    api_hash="ee28199396e0925f1f44d945ac174f64",
    bot_token="5782497998:AAFdx2dX3yeiyDIcoJwPa_ghY2h_dozEh_E"
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
  global user_id
  user_id = message.from_user.id 
  file = message.audio
  global file_path
  file_path = message.download(file_name="./downloads/")
  filename = os.path.basename(file_path)
  head, tail = os.path.split(file_path)
  file, ext = os.path.splitext(tail)
  global result
  result = f"{file}.txt"
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
  cmd(f'''python3 speech.py {langtoken} "{file_path}" "{result}" ''')  
  with open(result, 'rb') as f:
        bot.send_document(user_id, f)
  cmd(f'''unlink {file_path}''')
  cmd(f'''unlink {result}''') 

bot.run()
