from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

bot = ChatBot('Buddy')
bot = ChatBot(
    'Buddy',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3'
)

bot = ChatBot(
    'Buddy',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3'
)

# Inport ListTrainer
from chatterbot.trainers import ListTrainer

trainer1 = ChatterBotCorpusTrainer(bot)

# Train based on the english corpus
trainer1.train("chatterbot.corpus.english")

# Train based on english greetings corpus
trainer1.train("chatterbot.corpus.english.greetings")

# Train based on the english conversations corpus
trainer1.train("chatterbot.corpus.english.conversations")

trainer = ListTrainer(bot)

trainer.train([
'My name is Nirvantika',
'Hi',
'Hello',
'I need your assistance regarding my order',
'Please, Provide me with your order id',
'I have a complaint.',
'Please elaborate, your concern',
'How long it will take to receive an order ?',
'An order takes 3-5 Business days to get delivered.',
'Okay Thanks',
'No Problem! Have a Good Day!'
])

response = bot.get_response('I have a complaint.')

print("Bot Response:", response)

name=input("Enter Your Name: ")
print("Welcome to the Bot Service! Let me know how can I help you?")
while True:
    request=input(name+':')
    if request=='Bye' or request =='bye':
        print('Bot: Bye')
        break
    else:
        response=bot.get_response(request)
        print('Bot:',response)