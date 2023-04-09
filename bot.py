import telebot
import subprocess

# Replace with your Telegram Bot API token
bot = telebot.TeleBot('5848326557:AAFWQc5chBlpdqNvjJHyUTTOksahsV7zMVg')

# Handler for audio messages
@bot.message_handler(content_types=['audio'])
def handle_audio(message):
    # Download audio file
    audio_file = bot.download_file(bot.get_file(message.audio.file_id).file_path)
    # Rename audio file to "entry"
    with open('entry.ogg', 'wb') as f:
        f.write(audio_file)
    # Execute speech.py script with entry file
    subprocess.call(['python', 'speech.py', 'RK3ETXWBJQSMO262RXPAIXFSG6NH3QRH', 'entry.ogg', 'transcription.txt'])
    # Upload transcription file to user
    with open('transcription.txt', 'rb') as f:
        bot.send_document(message.chat.id, f)

# Start the bot
bot.polling()
