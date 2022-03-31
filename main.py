import telegram.ext
import requests
import json


with open('token.txt', 'r') as f:
    TOKEN = f.read()


def start(update, context):
    update.message.reply_text("Bot is on!")


def help(update, context):
    update.message.reply_text("""
    Commits are sent in real time.
    Following commands are available:
    
    /start ==> start the bot
    /help ==> show help 
    /info ==> show info about bot
    /commits ==> show latest commit 

    """)


def info(update, context):
    update.message.reply_text("This bot was made using Python by Petr")


def commits(update, context):
    response_API = requests.get('https://api.github.com/repos/petrsvetr123lol/TestingRepo/commits/main')
    data = response_API.text
    parse_json = json.loads(data)
    latest_commit = parse_json['html_url']
    message = parse_json['commit']['message']
    message_convert = json.dumps(message)
    latest_commit_convert = json.dumps(latest_commit)
    update.message.reply_text(message_convert + latest_commit_convert)


updater = telegram.ext.Updater(TOKEN, use_context=True)
disp = updater.dispatcher

disp.add_handler(telegram.ext.CommandHandler("start", start))
disp.add_handler(telegram.ext.CommandHandler("help", help))
disp.add_handler(telegram.ext.CommandHandler("info", info))
disp.add_handler(telegram.ext.CommandHandler("commits", commits))
print("Bot is running!")

updater.start_polling()
updater.idle()
