#to get the chat id of sender (chatneutralized account)
import requests

bot_token = ""  # Your Bot's Token which you get when create a bot on telegram

url = f"https://api.telegram.org/bot{bot_token}/getUpdates"

response = requests.get(url)
data = response.json()

# Check if the response contains messages
if data["ok"] and data["result"]:
    # Iterate over all updates and filter for group chat
    for update in data["result"]:
        if "message" in update:
            chat = update["message"]["chat"]
            # Check if it's a group (negative chat_id) 
            if chat["type"] == "group" or chat["type"] == "supergroup":
                chat_id = chat["id"]
                print(f"Group Chat ID: {chat_id}")  
                #this will gave some chatid's for "chatneutalizer" of tele_sender.py
else:
    print("No updates found.")
    
