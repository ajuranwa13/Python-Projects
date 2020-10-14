# make your own assistant to do work by just listening your voice
import pyttsx3  # pip install pyttsx3
import datetime 
import speech_recognition as sr # pip install speechRecognition
import wikipedia
import webbrowser
import os

# creates a obj of pyttsx3
engine = pyttsx3.init()
# get voice by get fun
voices = engine.getProperty('voices')
# it selects male voice by [0] and female by [1]
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>0 and hour<12:
        speak('Good Morning')
    elif hour>=12 and hour<18:
        speak('Good Afternoon')
    else:
        speak('Good Evening')
    speak('I am Max and how may i help you today?')

   

def takeCommand():
    # it recogonises the input audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....>>>")
        # will provide gape between to words
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing..>>>')
        query = r.recognize_google(audio,language='en-in')
        print("User Said : {}".format(query))
    
    except Exception as e:
        # print(e)
        print('Say that again please...')
        return 'None'
    return query

if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()
        # logic to execute tasks bt query
        if 'wikipedia' in query:
            speak('Searching wikipedia')
            # will replace wikipedia by space in query
            query = query.replace('wikipedia','')
            # set no of sentences to take from wikipedia in results 
            results = wikipedia.summary(query,sentences=2)
            speak('According to wikipedia')
            # print(results)
            speak(results)

        # say thank you for quiting the program
        elif 'thank you' in query:
            speak('Always happy to help you')
            quit()

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'open google' in query:
            webbrowser.open('google.com')

        elif 'open hackerrank' in query:
            webbrowser.open('hackerrank.com')

        elif 'play music' in query:
            # here you have to copy your music dir path in music_dir
            music_dir = 'G:\\personal things\\songs\\Ajay music\\Punjabi'
            # store song list in songs
            songs = os.listdir(music_dir)
            # print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime('%H:%M:%S')
            speak('sir, the time is {0}'.format(strTime))

        elif 'open code' in query:
            codepath = "C:\Users\hp\AppData\Local\Programs\Microsoft VS Code\Code.exe"
            os.startfile(codepath)

        # and many more elif you can add  for more app to open by your assistant
