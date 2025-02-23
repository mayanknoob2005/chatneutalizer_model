#sending message to neutralized message to telegram
import requests
import sys
import importlib

sys.path.append("/Users/filter") #path where the folder is saved


chatneutalizer_token = "" #token(api key) which you get from telegram 
chatneutalizer = "" #from chatneutalizer_chatid.py

while True:
    
    model = importlib.import_module("model")  # Dynamically reload the module
    importlib.reload(model)  # Ensure fresh import each time
    ans = model.ans  # Get the latest value of ans

    if ans == "@exit":
        break

    url = f"https://api.telegram.org/bot{chatneutalizer_token}/sendMessage"
    payload = {"chat_id": chatneutalizer, "text": ans}

    response = requests.post(url, data=payload)
    print(response.text)
    temp=importlib.import_module("replacement") 
    importlib.reload(temp)