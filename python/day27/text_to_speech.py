from gtts import gTTS

test = input("Enter the text you want to convert to speech: ")
audio = gTTS(text=test, lang='en')

audio.save("output.mp3")
print("Audio file saved as output.mp3")