import telebot
import subprocess

# Replace with your Telegram Bot API token
bot = telebot.TeleBot('5848326557:AAGatJA3c9m0JJZinxN2mSOsolFdhtyvIDM')

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.reply_to(message, "السلام عليكم . أنا بوت تفريغ الصوتيات")


# Handler for audio messages
@bot.message_handler(content_types=['audio'])
def handle_audio(message):
    bot.reply_to(message, "جاري التفريغ . سيتم إرسال ملف التفريغ بعد الانتهاء إن شاء الله")
    # Download audio file
    audio_file = bot.download_file(bot.get_file(message.audio.file_id).file_path)
    # Rename audio file to "entry"
    with open('entry.mp3', 'wb') as f:
        f.write(audio_file)
    # Execute speech.py script with entry file
    subprocess.call(['python', 'speech.py', 'RK3ETXWBJQSMO262RXPAIXFSG6NH3QRH', 'entry.mp3', 'transcription.txt'])
    # Upload transcription file to user
    with open('transcription.txt', 'rb') as f:
        bot.send_document(message.chat.id, f)

# Start the bot
bot.polling()
