from openai import OpenAI
import pyttsx3
import speech_recognition as sr
import time
import sys
from datetime import datetime

r = sr.Recognizer()


def SpeakText(command):
    # Initialize the engine
    engine = pyttsx3.init()
    newVoiceRate = 130
    engine.setProperty('rate', newVoiceRate)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(command)
    engine.runAndWait()


# Your OpenAI API key
client = OpenAI(api_key="YOUR-API-KEY")

SpeakText("Hi, My name is leo")
time.sleep(1)
while True:
    with sr.Microphone() as source2:
        # wait for a second to let the recognizer
        # adjust the energy threshold based on
        # the surrounding noise level
        r.adjust_for_ambient_noise(source2, duration=0.2)

        # listens for the user's input
        audio2 = r.listen(source2)

        try:
            # Recognize speech using Google Speech Recognition
            content = r.recognize_google(audio2)
            content = content.lower()

            # Check if the wake word is detected
            if "hey leo" in content:
                # Speak acknowledgement
                SpeakText("Yes, how can I assist you?")

                # Now proceed with OpenAI completion
                audio2 = r.listen(source2)  # Listen for the user's input after wake word
                content = r.recognize_google(audio2).lower()  # Recognize the user's input

                session = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[{
                        "role": "user",
                        "content": "Summarize the content below in 100 words: " + content
                    }]
                )

                response = session.choices[0].message.content
                print(response)
                SpeakText(response)
                response = ""
                time.sleep(1)

            if "exit" in content:
                SpeakText("Bye Bye, See you next time")
                sys.exit()
            if "what is the time" in content:
                now = datetime.now()
                current_time = now.strftime("%I:%M %p")
                SpeakText("It's " + current_time)
        except sr.UnknownValueError:
            print("")
