import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Please speak something...")
    audio = recognizer.listen(source)

try:
    text = recognizer.recognize_google(audio)
    print("You said: " + text)
except sr.RequestError:
    print("Service unavailable.")
except sr.UnknownValueError:
    print("Sorry, something went wrong.")