from openai import OpenAI
import pyttsx3
import speech_recognition as sr
import time

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
client = OpenAI(api_key="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")

SpeakText("Hi, My name is bobert")
time.sleep(1)
while True:
    with sr.Microphone() as source2:
        # wait for a second to let the recognizer
        # adjust the energy threshold based on
        # the surrounding noise level
        SpeakText("Listening....")
        r.adjust_for_ambient_noise(source2, duration=0.2)

        # listens for the user's input
        audio2 = r.listen(source2)

        content = r.recognize_google(audio2)
        content = content.lower()
    # Create a new session
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