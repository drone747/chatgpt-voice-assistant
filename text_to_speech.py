import pyttsx3

def SpeakText(command):
    # Initialize the engine
    engine = pyttsx3.init()
    newVoiceRate = 130
    engine.setProperty('rate', newVoiceRate)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(command)
    engine.runAndWait()

SpeakText("hello my name is andy")