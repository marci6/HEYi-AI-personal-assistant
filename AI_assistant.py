import speech_recognition as sr
import pyttsx3 # text to speech conversion library
import datetime
import wikipedia
import webbrowser
import time
import subprocess
from ecapture import ecapture as ec
import wolframalpha


print('Loading your Heyi')

engine=pyttsx3.init('sapi5')
engine.setProperty('rate', 140)     # setting up new voice rate
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[0].id')

chrome_path='C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

def speak(text):
    engine.say(text) # converts text to speech
    engine.runAndWait() # Blocks while processing all currently queued commands

def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello, Good Morning")
        print("Hello, Good Morning")
    elif hour>=12 and hour<18:
        speak("Hello, Good Afternoon")
        print("Hello, Good Afternoon")
    else:
        speak("Hello, Good Evening")
        print("Hello, Good Evening")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            return -1
        return statement

#speak("Loading your Heyi")
wishMe()


if __name__=='__main__':

    fail_counter=0
    while True:
        
        speak("How can i help you?")
        statement = takeCommand()
        while statement==-1:
            fail_counter+=1
            if fail_counter>1:
                speak('Closing Heyi')
                break
            speak("Repeat")
            statement = takeCommand()
            
        if fail_counter<2:
            fail_counter=0
            statement.lower()
            
        if statement==0:
            continue
        # conclude session
        if "good bye" in statement or "ok bye" in statement or "stop" in statement:
            speak('Good bye')
            print('Good bye')
            break
        # search on wikipedia
        if 'wikipedia' in statement:
            speak('What should I be looking for ?')
            quest = takeCommand().lower()
            results = wikipedia.summary(quest, sentences=1)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        # open Youtube
        elif 'open youtube' in statement:
            webbrowser.get(chrome_path).open_new_tab("https://www.youtube.com")
            speak("youtube is open now")
            time.sleep(5)
        # open Google
        elif 'open google' in statement:
            webbrowser.get(chrome_path).open_new_tab("https://www.google.com")
            speak("Google chrome is open now")
            time.sleep(5)
        # open Gmail
        elif 'open gmail' in statement:
            webbrowser.get(chrome_path).open_new_tab("https://mail.google.com/mail/u/0/?tab=wm&ogbl#inbox")
            speak("Google Mail open now")
            time.sleep(5)

        elif 'who are you' in statement or 'what can you do' in statement:
            speak('I am G-one version 1 point O your persoanl assistant. I am programmed to minor tasks like'
                  'opening youtube,google chrome,gmail and stackoverflow ,predict time,take a photo,search wikipedia,' 
                  'get top headline news from times of india and you can ask me computational or geographical questions too!')


        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was built by Marcello Chiesa")
            print("I was built by Marcello Chiesa")

        elif "open stackoverflow" in statement:
            webbrowser.open_new_tab("https://stackoverflow.com/login")
            speak("Here is stackoverflow")
        # Open NY Times
        elif 'news' in statement:
            news = webbrowser.get(chrome_path).open_new_tab("https://www.nytimes.com/international/?action=click&region=Editions&pgtype=Homepage")
            speak('Here are some headlines from the New York Times, Happy reading')
            time.sleep(6)
        # take a photo
        elif "camera" in statement or "take a photo" in statement or "take a picture" in statement:
            ec.capture(0,"robo camera","img.jpg")
        # search on Google
        elif 'search'  in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(5)
        # ask WolframAlpha
        elif 'ask' in statement or 'question' in statement:
            speak('I can answer to computational and geographical questions and what question do you want to ask now')
            question=takeCommand()
            app_id="P442WJ-7Y4EY5VPHX"
            client = wolframalpha.Client(app_id)
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)

        # shutdown PC
        elif "log off" in statement or "sign out" in statement:
            speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])
        
        elif 'timer' in statement:
            words=statement.split()
            for word in words:
                if word=='seconds':
                    l=1
                if word=='minutes':
                    l=60
            n=int(words[-2])
            t=l*n
            while t: 
                print(n,' seconds remaining')
                time.sleep(1) 
                t -= 1
            speak('Timer concluded')
            
            # check time
        elif 'time' in statement:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

time.sleep(3)