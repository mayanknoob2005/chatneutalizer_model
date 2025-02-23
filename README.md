# chatneutalizer_model

# Setup Guide

## Setting Up the Files

1) **Save the Folder and File**  
   - Store the folder and file in an offline location (not connected to OneDrive, Google Drive, etc.).

2) **Install Python (if not installed)**  
   - If Python is not installed, install it first.

3) **Install Required Libraries**  
   - Run the following command to install the necessary libraries:  
     ```sh
     pip install requests groq
     ```

4) **Create a Groq Cloud Account**  
   - Sign up on [Groq Cloud](https://console.groq.com) to obtain the API key for the model.

5) **Install and Set Up Telegram**  
   - Install Telegram and log in.

6) **Create a Telegram Bot**  
   - Use [BotFather](https://t.me/botfather) to create a Telegram bot and obtain its API key.

7) **Run the Script**  
   - Execute `tele_sender.py`.

8) **Enter API Key**  
   - A dialog box will pop up. Enter the API key to send messages.

9) **Send Messages**  
   - Successfully send messages. Continue sending new messages or type `@exit` to terminate the program.

---

## Getting API Key from Groq Cloud

1) **Create an Account**  
   - Sign up on [Groq Cloud](https://console.groq.com).

2) **Obtain API Key**  
   - The API key is available on the left side above the "Documentation" section.

3) **Select a Model**  
   - Go to **Documentation -> Model** and select the model.  
   - We are using:  
     ```python
     model="llama3-70b-8192"
     ```

---

## Creating the Bot and Getting API Key & Chat ID

1) **Create a Telegram Bot**  
   - Visit [BotFather](https://t.me/botfather) to create a bot and obtain the API key.

2) **Set Bot Name**  
   - Enter a name for your bot (e.g., `chatneutralized`).

3) **Add Bot to Group**  
   - Add the bot to the group where you want to send messages and make it an admin.

4) **Get Chat ID**  
   - Add the API key to `chatneutralizer_chatid.py` to retrieve the chat ID for `chatneutralizer` in `tele_sender.py`.

5) **Identify the Correct Chat ID**  
   - You will receive multiple chat IDs (group chat IDs have a negative sign).  
   - Use all retrieved chat IDs in `chatneutralizer` of `tele_sender.py`, and test which one works.

---

