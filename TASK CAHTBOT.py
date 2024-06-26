import nltk
import random
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses
patterns_responses = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today?",]
    ],
    [
        r"what is your name?",
        ["My name is Chatbot and I'm a chatbot.",]
    ],
    [
        r"how are you?",
        ["I'm doing good\nHow about You ?",]
    ],
    [
        r"i am great",
        ["Awesome! good to hear that",]
    ],
    [
        r"sorry (.*)",
        ["It's alright", "It's OK, never mind",]
    ],
    [
        r"i'm (.*) doing good",
        ["Nice to hear that", "Alright :)",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
    [
        r"what's your age?",
        ["I'm a computer program, I don't have an age",]
    ],
    [
        r"where do you live?",
        ['I am a bot and I live in your computer',]
    ],
    [
        r"quit",
        ["Bye, take care. See you soon :) ", "It was nice talking to you. See you soon :)"]
    ],
]

# Create a Chatbot
def chatbot():
    print("Hi, I'm Chatbot and I'm here to help you. Type 'quit' to end the conversation.")
    chat = Chat(patterns_responses, reflections)
    chat.converse()

if __name__ == "__main__":
    nltk.download('punkt')
    nltk.download('averaged_perceptron_tagger')
    chatbot()
