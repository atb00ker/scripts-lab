from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

updater = Updater(token='YOUR_TOKEN_HERE')
dispatcher = updater.dispatcher

def start(bot, update):
	update.message.reply_text("Hi! I am ATB00ker Bot! Currently under construction! Use /help to see what all i can do presently! \ud83d\ude04")

def help(bot, update):
	update.message.reply_text("Click on the links to use them! \n/Developer to meet the developer. \ud83d\ude09\n/StudyMaterial for amity syllabus\n/Projects to see my work.")

def StudyMaterial(bot, update):
	keyboard = [[InlineKeyboardButton("First Year", url='https://drive.google.com/drive/folders/0B-SmzjWLoGhCRDQ5amdPWUY5N2s'),InlineKeyboardButton("Second Year", url='https://www.google.co.in/')],[InlineKeyboardButton("Third Year", url='https://www.google.co.in/'),InlineKeyboardButton("Fourth Year", url='https://www.google.co.in/')]]
	reply_markup = InlineKeyboardMarkup(keyboard)
	update.message.reply_text('If you have any useful Study Material; Please send it to me @ ajay39in@gmail.com\nThanks! \ud83d\ude03 \nPlease choose:', reply_markup = reply_markup)

def Developer(bot, update):
	update.message.reply_text("Hi! I am Ajay Tripathi! Find me on:\nFacebook: https://www.facebook.com/ajay39in \nTelegram: @ATB00ker\nGitHub: https://github.com/ATB00ker\nGmail: ajay39in@gmail.com\nHotmail: ajay39in@hotmail.com\n/Projects to see my work")

def Projects(bot, update):
	update.message.reply_text("Hi! Here is a link to my GitHub Profile: https://github.com/ATB00ker\nMy work include:\nI. C++: I know C++ and can projects on the same, a sample of my work is available on Github here: https://github.com/ATB00ker/Class12thSampleProject\n\nII. Web development: I have worked on HTML, CSS, JavaScript, JQuery, Bootstrap, KUTE and many more; Some of my work include:\n\n 1.Exposure Website: https://github.com/ATB00ker/Exposure.github.io\n 2.InfiCON Website: https://github.com/ATB00ker/InfiCON.github.io\n 3.Presentation Creation Tool: https://github.com/ATB00ker/PresentationCreationTool\n\nIII. Python: I can develop applications on python and this bot is developed on python.")

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('Developer', Developer))
updater.dispatcher.add_handler(CommandHandler('StudyMaterial', StudyMaterial))
updater.dispatcher.add_handler(CommandHandler('Projects', Projects))

# Start the Bot
updater.start_polling()
# Run the bot until the user presses Ctrl-C or the process receives SIGINT, SIGTERM or SIGABRT
updater.idle()
