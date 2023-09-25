echo "Cloning Repo...."
git clone https://github.com/konichiwa55115/Transcriber-Telegram-Bot /kony
cd /kony
pip3 install -r requirements.txt
echo "Starting Bot...."
python3 bot.py
