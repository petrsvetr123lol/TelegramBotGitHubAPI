import telegram.ext
import requests

with open('token.txt', 'r') as f:
    TOKEN= f.read()

def start(update, context):
    update.message.reply_text("Bot is on!")

def help(update, context):
    update.message.reply_text("""
    Following commands are available:
    
    /start ==> start the bot
    /help ==> show help 
    /info ==> show info about bot
    """)

def info(update, context):
    update.message.reply_text("This bot was made using Python by Petr")

def commit(update, context):
    response = requests.get("https://api.github.com/repos/petrsvetr123lol/TestingRepo/commits/main.json")
    update.message.reply_text(response.text)


updater = telegram.ext.Updater(TOKEN, use_context=True)
disp = updater.dispatcher


disp.add_handler(telegram.ext.CommandHandler("start", start))
disp.add_handler(telegram.ext.CommandHandler("help", help))
disp.add_handler(telegram.ext.CommandHandler("info", info))
disp.add_handler(telegram.ext.CommandHandler("commit", commit))
print("Bot is running!")

updater.start_polling()
updater.idle()
