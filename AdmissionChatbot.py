class AdmissionChatbot:
    def __init__(self):
        self.context = {}
        self.admission_responses = {
            "admission procedure": "The admission procedure involves submitting an online application, providing transcripts, letters of recommendation, and a personal statement.",
            "requirements": "Admission requirements include a completed application form, high school transcripts, standardized test scores (SAT/ACT), letters of recommendation, and a personal statement.",
            "deadlines": "The application deadlines are November 1st for Early Decision and January 1st for Regular Decision.",
            "tuition fees": "The tuition fees for the upcoming academic year are $20,000 per semester.",
            "scholarships": "We offer a variety of scholarships based on academic merit, financial need, and extracurricular involvement. Please visit our scholarships page for more details."
        }
        self.default_response = "I'm sorry, I didn't understand that. Can you please rephrase your question?"
        self.farewell_message = "Goodbye! If you have more questions later, feel free to ask!"

    def greet(self):
        greeting = "Hello! How can I assist you with your college admission queries today?"
        self.context["greeting"] = greeting
        print(f"Chatbot: {greeting}")

    def farewell(self):
        print(f"Chatbot: {self.farewell_message}")

    def respond(self, user_input):
        user_input_lower = user_input.lower()
        response = self.admission_responses.get(user_input_lower, self.default_response)
        self.context[user_input] = response
        return response

    def ask_admission_questions(self):
        questions = [
            "Which institute you went to previously?",
            "Do you hold any acheivements at the national level academically?",
            "What sports do you play, if so what are your acheivements in that field?"
        ]
        answers = {}
        for question in questions:
            print(f"Chatbot: {question}")
            user_response = input("You: ")
            answers[question] = user_response
            self.context[question] = user_response
        return answers

    def handle_question(self, user_input):
        user_input_lower = user_input.lower()
        response = self.admission_responses.get(user_input_lower, self.default_response)
        self.context[user_input] = response
        return response

    def remember_context(self):
        return self.context

    def handle_interaction(self):
        self.greet()
        while True:
            user_input = input("You: ")
            if user_input.lower() == "bye":
                self.farewell()
                break
            response = self.handle_question(user_input)
            print(f"Chatbot: {response}")
            self.context[user_input] = response

        print("Chatbot: I have a few questions for you!")
        answers = self.ask_admission_questions()
        print("Chatbot: Thanks for sharing! Here's what I learned about you:")
        for question, answer in answers.items():
            print(f"{question} - {answer}")

        print("Chatbot: If you have any more questions, feel free to ask!")

# Running the chatbot
chatbot = AdmissionChatbot()
chatbot.handle_interaction()
