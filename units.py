from chatterbot import ChatBot




bot=ChatBot("units",logic_adapters=["chatterbot.logic.UnitConversion"])


while True:
    user_text= input("Type the unit conversion that you want to solve:")
    chatbot_response=str(bot.get_response(user_text))
    print(chatbot_response)