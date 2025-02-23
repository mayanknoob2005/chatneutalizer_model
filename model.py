# finine tunning the sentence using llm model

import os
from groq import Groq
from replacement import updated_sentence, contain
import tkinter as tk

# Initialize the Groq client with the API key
client = Groq(api_key="")

user_input = updated_sentence

# Define the prompt for fine tune 
prompt = """
You are an expert in natural language processing. 
Your task is to refine and restructure sentences that contain word replacements in brackets, ensuring the result is fluent and natural in English.

try to match sense of neutral and offensive sentence like

For example, given the sentence:
this is (['nonsense', 'rubbish', 'balderdash', 'problem', 'difficulty'] , ['easy work']) work

Your goal is to choose the most appropriate word or phrase to create a grammatically correct and meaningful sentence from the provided options in the dictionary  . 
rest the things to be remain as it is .
If multiple words or phrases are provided, select the one that best fits the what shif have you done in the workcontext. 
Ensure that any offensive language is replaced with neutral alternatives that do not alter the intended meaning.

Provide the answer by putting two line breaks before the refined sentence, 
followed by the refined sentence  then no new line after answer.

If the sentence doesn't require any refinement, output the sentence as is, but ensure it is grammatically correct. 

You are an (['idiot', 'fool', 'inconsiderate person', 'unintelligent person']) and behave like an (['arrogant person']).
answer should be 
You are an idiot and behave like an arrogant person


the last line of your response will contain only the refined senetnce nothing else

"""


# Ensure user input is always combined with the prompt
content = f"{user_input}\n\n{prompt}"

# Create a chat completion request with user input + prompt
chat_completion = client.chat.completions.create(
    messages=[{"role": "user", "content": content}],
    model="llama3-70b-8192",
)

# AI's response
ai = chat_completion.choices[0].message.content


def last_line(sentence):
    lines = sentence.splitlines()  # Split sentence into lines
    return lines[-1]


if contain:  # contains bad word
    ans = last_line(ai)
else:  # no bad word
    ans = user_input



# def print_in_box(ans):
#     length = len(ans)
#     print("-" * (length + 2))
#     print(" " + ans + " ")
#     print("-" * (length + 2))

# Example usage
#print_in_box(ans)