import sys
import pyttsx3

tts = pyttsx3.init()

while True:
    text = input('>')
    if text.upper()[0] == 'Q' or text.upper()== 'EXIT':
        tts.say('Quiting..')
        print("Quiting...")
        sys.exit()
    tts.say(text)
    tts.runAndWait()


