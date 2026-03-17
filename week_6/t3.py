import re


class Chatbot:

    def __init__(self, name):

        self.name = name

        self.response_rules = {
            "hello": "Hello! Nice to meet you.",
            "hi": "Hi there!",
            "hey": "Hey! How can I help?",
            "good morning": "Good morning! Hope you have a great day.",
            "good evening": "Good evening!",

            "bye": "Goodbye! Have a nice day.",
            "goodbye": "See you later!",
            "see you": "Take care!",

            "fast": "FAST University is known for its strong CS programs.",
            "fast university": "FAST is one of the top CS universities in Pakistan.",
            "fast peshawar": "FAST Peshawar campus offers excellent computing programs.",

            "peshawar": "Peshawar is one of the oldest cities in South Asia.",
            "peshawar food": "Chapli Kabab from Peshawar is famous!",
            "peshawar weather": "Peshawar usually has warm weather.",

            "ai": "Artificial Intelligence is transforming many industries.",
            "machine learning": "Machine learning allows systems to learn from data.",
            "deep learning": "Deep learning uses neural networks with many layers.",

            "tell joke": "Why do programmers prefer dark mode? Because light attracts bugs!",
            "joke": "Why did the computer get cold? It forgot to close Windows.",
            "funny": "Debugging: removing the needles from the haystack.",

            "you are good": "Thank you! I appreciate it.",
            "good bot": "Thanks! I'm trying my best.",
            "smart": "Thanks! I'm always learning.",

            "you are bad": "I'm sorry if I disappointed you.",
            "stupid": "I'm still learning, please be patient with me.",
            "idiot": "Let's keep things friendly..",

            "how are you": "I'm doing great! thanks for asking.",
            "what is your name": "I am your friendly chatbot.",
            "help": "You can ask me about FAST, AI, Peshawar, or ask for a joke!"
        }

        self.conversation_history = []
        self.sentiment_score = 0

        self.positive_words = ["good", "great", "nice", "awesome", "thanks", "smart"]
        self.negative_words = ["bad", "stupid", "idiot", "hate", "terrible", "awful"]
#text preprocessing - convert to lowercase, remove punctuation, split into words

    def preprocess(self, text):

        words = re.findall(r'\w+', text.lower())

        words = list(map(lambda w: w.strip(), words))

        return words

#check sentiment of user input by counting positive and negative words, and update sentiment score

    def update_sentiment(self, words):

        positive = len(list(filter(lambda w: w in self.positive_words, words)))
        negative = len(list(filter(lambda w: w in self.negative_words, words)))

        self.sentiment_score += positive
        self.sentiment_score -= negative

#rule matching 

    def find_best_match(self, text):

        matches = []

        for keyword in self.response_rules:

            if keyword in text:
                matches.append(keyword)

        if not matches:
            return None

        # pick most specific rule (longest keyword)
        best_match = max(matches, key=lambda k: len(k))

        return best_match


#response function

    def respond(self, user_input):

        words = self.preprocess(user_input)

        self.update_sentiment(words)

        rule = self.find_best_match(user_input.lower())

        if rule:
            response = self.response_rules[rule]
        else:
            response = self.learn(user_input)

        if self.sentiment_score < -3:
            response += "\nYou seem upset. Here's something to cheer you up: 😊 Life gets better!"

        self.conversation_history.append(("User", user_input))
        self.conversation_history.append((self.name, response))

        return response

#learning mode - when no rule matches, ask user to teach the bot a new response for that input

    def learn(self, user_input):

        print("I don't know how to respond to that.")

        answer = input("What should I reply next time? ")

        keyword = input("Enter a keyword for this rule: ")

        self.response_rules[keyword.lower()] = answer

        return "Thanks! I learned something new."

#history saving

    def save_history(self, filename="chat_history.txt"):

        with open(filename, "w") as f:

            for speaker, message in self.conversation_history:
                f.write(f"{speaker}: {message}\n")

        print("Conversation saved.")




def main():

    bot = Chatbot("FAST-Bot")

    user_name = input("Hello! What is your name? ")
    print(f"\nWelcome, {user_name} ,I'm {bot.name}.")
    print("You can ask me about FAST, AI, Peshawar, or ask for a joke!")
    print("Type 'exit' to quit.\n")

    while True:

        user_input = input("You: ")

        if user_input.lower() == "exit":
            bot.save_history()
            break

        response = bot.respond(user_input)

        print("Bot:", response)


main()