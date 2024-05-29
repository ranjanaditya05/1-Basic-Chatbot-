class SimpleChatbot:
    def __init__(self):
        self.context = {}
        self.jokes = [
            "Why was the math book sad? Because it had too many problems.",
            "Why did the golfer bring an extra pair of pants? In case he got a hole in one!",
            "Why was the computer cold? It left its Windows open.",
            "What do you call cheese that isn't yours? Nacho cheese!",
            "Why did the tomato turn red? Because it saw the salad dressing!",
        ]
        self.current_joke_index = 0

    def greet(self):
        print("Chatbot: Hi there! I'm your friendly chatbot. How can I assist you today?")

    def farewell(self):
        print("Chatbot: It was nice talking to you. Have a great day!")

    def tell_joke(self):
        joke = self.jokes[self.current_joke_index]
        self.current_joke_index = (self.current_joke_index + 1) % len(self.jokes)
        return joke

    def handle_question(self, user_input):
        responses = {
                  "how do you work": "I work by processing your inputs and responding based on pre-defined rules and data.",
            "what's your purpose": "My purpose is to assist you with your queries and provide useful information.",
            "can you tell me a joke": "Sure! Why don't scientists trust atoms? Because they make up everything!",
            "what's the time": "I'm not able to check the current time. Please check your device for the time.",
            "can you learn": "I can't learn on my own, but my developers can update my programming to make me smarter.",
            "what's your favorite food": "As a chatbot, I don't eat, but I hear pizza is quite popular!",
            "tell me a joke": self.tell_joke,
            "one more": self.tell_joke,
            "bye": self.farewell
           
        }
        normalized_input = user_input.strip().lower()
        return responses.get(normalized_input, "Sorry, I didn't understand that. Could you please rephrase?")

    def remember_context(self, user_input, response):
        self.context[user_input] = response

    def ask_questions(self):
        questions = [
            "What's your favorite color?",
            "What's your favorite food?",
            "Where are you from?",
            "What's your favorite hobby?",
            "Do you have any pets?"
        ]
        answers = {}
        for question in questions:
            print(f"Chatbot: {question}")
            user_response = input("You: ")
            answers[question] = user_response
            self.remember_context(question, user_response)
        return answers

    def handle_interaction(self):
        self.greet()
        while True:
            user_input = input("You: ")
            if user_input.lower() == "bye":
                self.farewell()
                break
            response = self.handle_question(user_input)
            if callable(response):
                response = response()
            print(f"Chatbot: {response}")
            self.remember_context(user_input, response)
        
        print("Chatbot: I have a few questions for you!")
        answers = self.ask_questions()
        print("Chatbot: Thanks for sharing! Here's what I learned about you:")
        for question, answer in answers.items():
            print(f"{question} - {answer}")
        
        print("Chatbot: If you have any more questions, feel free to ask!")

chatbot = SimpleChatbot()
chatbot.handle_interaction()