#doing words replacemnt into dictonary

from dic_combine import final_dict

# Input from the user
user_input = input("Enter a sentence (type @exit :to exit): ")

# Splitting the sentence into words
words = user_input.split()

# List to store the updated words
updated_words = []
contain=False #no  bad word
# Checking if each word is in the final_dict
for word in words:
    if word in final_dict:
        # Replacing the word with its corresponding value from final_dict
        updated_words.append(f"({' , '.join(map(str, final_dict[word]))})")
        contain=True
    else:
        # If not found, just keep the word
        updated_words.append(word)
        
# Joining the updated words to form the final sentence
updated_sentence = ' '.join(updated_words)




# Printing the final output
#print("Updated sentence:", updated_sentence)