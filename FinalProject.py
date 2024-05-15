import webbrowser
import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print('Listening...')

    audio = recognizer.listen(source)

try: # tries the lines below
    your_speech = recognizer.recognize_google(audio)
    print('You said: "' + your_speech + '"')

    if your_speech != '':
        url = 'https://www.google.com/search?q=' + '+'.join(your_speech.split())
        webbrowser.open_new(url)

except sr.UnknownValueError:
    print("Sorry, I didn't catch that.")

except sr.RequestError:
    print("Could not request results. Please check your internet connection.")
