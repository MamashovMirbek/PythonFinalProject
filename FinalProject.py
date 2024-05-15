import webbrowser # Importing for Google searching
import speech_recognition as sr # Importing for speech recognition

recognizer = sr.Recognizer() # Initializing the recognizer

with sr.Microphone() as source: # Using the microphone as the audio source
    print('Listening...') # Hint for the user for speaking

    audio = recognizer.listen(source) # Listening for speech and converting it to text

try: # tries the lines below
    your_speech = recognizer.recognize_google(audio) # Recognizing speech using Google Speech Recognition
    print('You said: "' + your_speech + '"') # Printing the speech

    if your_speech != '': # Means if your speech is not empty or has a result
        url = 'https://www.google.com/search?q=' + '+'.join(your_speech.split()) # Adding 'https...' and changing spaces to '+' for web browsing url
        webbrowser.open_new(url) # Opening the web browser and searching for your speech

except sr.UnknownValueError: # Means if 'try:' is not defined then this line will work
    print("Sorry, I didn't catch that.") # Means if line 19 is true then it prints

except sr.RequestError: # Means if line 19 didn't work then this line will work
    print("Could not request results. Please check your internet connection.") # Means if line 22 is true then it prints
