import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup , InlineKeyboardButton , ReplyKeyboardMarkup , CallbackQuery
import subprocess
bot = Client(
    "myfirs",
    api_id=17983098,
    api_hash="ee28199396e0925f1f44d945ac174f64",
    bot_token="5848326557:AAGHzvPErt9hr6NFYn7TNDOaXQiVXvR213c"
)
CHOOSE_UR_LANG = " اختر لغة المقطع من فضلك "
CHOOSE_UR_LANG_BUTTONS = [
    [InlineKeyboardButton("العربية",callback_data="العربية")],
     [InlineKeyboardButton("الإنجليزية",callback_data="الإنجليزية")],
     [InlineKeyboardButton("التركية",callback_data="التركية")],
     [InlineKeyboardButton("الفرنسية",callback_data="الفرنسية")],
     [InlineKeyboardButton("اليابانية",callback_data="اليابانية")],
     [InlineKeyboardButton("الألمانية",callback_data="الألمانية")]
]



@bot.on_message(filters.command('start') & filters.private)
def command1(bot,message):
    bot.send_message(message.chat.id, " السلام عليكم أنا بوت تفريغ صوتيات , فقط أرسل الصوتية هنا\n\n  لبقية البوتات هنا \n\n https://t.me/ibnAlQyyim/1120 ",disable_web_page_preview=True)

    
@bot.on_message(filters.private & filters.incoming & filters.audio | filters.voice | filters.video | filters.document )
def _telegram_file(bot, message):
  try: 
    with open("myfile.txt", 'r') as fh:
      
            sent_message = message.reply_text('هناك عملية يتم الآن . أرسل الفيديو بعد مدة من فضلك', quote=True)
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
  if CallbackQuery.data == "العربية":
      langtoken = "RK3ETXWBJQSMO262RXPAIXFSG6NH3QRH"
  elif CallbackQuery.data == "الإنجليزية":
      langtoken = "2OVHUDKLF33Z44DOOX7GBAWEL5GOXI3Z"
  elif CallbackQuery.data == "التركية":
      langtoken = "25LMC6WPQBFURJTCECAU3O3BIWIV4PGT"
  elif CallbackQuery.data == "الفرنسية" :
      langtoken = "AMORHRXGFFALYGUR23MVHVWJKHJIH53T"
  elif CallbackQuery.data == "الألمانية":
      langtoken = "UEK2TR23J5ECLC6L6BI5YNHN5MBC4Q6U"
  elif CallbackQuery.data == "اليابانية":
      langtoken = "BCDCJOEWUAGWQZTHX4QGSXGWLO5CWV5Z" 
  subprocess.call(['ffmpeg', '-i',file_path,'-q:a','0','-map','a',mp3file,'-y' ])
  subprocess.call(['python','speech.py',langtoken,mp3file,result])
  with open(result, 'rb') as f:
        bot.send_document(user_id, f)
        subprocess.call(['unlink',"myfile.txt"])  


bot.run()
