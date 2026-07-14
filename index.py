from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer,ChatterBotCorpusTrainer
from flask import Flask, render_template,request
import requests

app = Flask(__name__)

bot=ChatBot("chatbot",read_only=False,
            logic_adapters=[
                {
                    "import_path": "chatterbot.logic.BestMatch",
                    "default_response":"sorry I don't have an answer",
                    "maximum_similarity_threshold":0.90
                }
            ])

# trainer=ChatterBotCorpusTrainer(bot)
# trainer.train("chatterbot.corpus.english")

@app.route("/")
def main():
    return  render_template("index.html")
 
# while True:
#     user_response = input("User: ")
#     print("Chatbot: " + str(bot.get_response(user_response)))


@app.route("/get")
def get_chatbot_response():
    userText=request.args.get('userMessage')
    rawData = requests.get("https://api.openweathermap.org/data/2.5/weather?q=" + userText + "&appid=dcad530dad7ee160e3d0752fffbddeac&units=metric")
    result = rawData.json()
    return result
    




if __name__ == "__main__":
        app.run(debug=True)

