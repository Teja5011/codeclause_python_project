import pyttsx3


class SpeakingAssistant:
    def __init__(self):
        self.engine = pyttsx3.init()

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()


if __name__ == "__main__":
    assistant = SpeakingAssistant()
    assistant.speak("Hello! I am your speaking assistant.")

    while True:
        user_input = input("You: ")

        if "hello" in user_input.lower():
            assistant.speak("Hello! How can I assist you?")
        elif "how are you" in user_input.lower():
            assistant.speak("I'm just a program, but I'm here to help!")
        elif "goodbye" in user_input.lower():
            assistant.speak("Goodbye!")
            break
        else:
            assistant.speak("I'm sorry, I don't have a response for that.")
