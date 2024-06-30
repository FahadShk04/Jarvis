from chatterbot import ChatBot
from chatterbot import ChatterBotCorpusTrainer

chatbot =ChatBot('Bot')
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train('ChatterBotCorpusTrainer.english')

while True:
    query = str(input(">> "))
    print(chatbot.get_response(query))
    if "exit " in query:
     break 