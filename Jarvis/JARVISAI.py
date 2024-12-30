import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
print(voices[0].id)
engine.setProperty("voice",voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning")

    elif hour>=12 and hour<18:
        speak("dood afternoon")

    else:
        speak("good evening")

    speak("i am jarvis sir,please tell me how many i help you")

def takecommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query =r.recognize_google(audio,language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        '''print(e)'''
        print("say that agian please...")
        return "none"
    return query

def sentEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com')
    server.ehlo()
    server.starttls()
    server.login('popsqldatabase1122@gmail.com','Ppopsql1122')
    server.sendmail('popsqldatabase1122@gamil.com',to,content)
    server.close()



if __name__ == "__main__":
    wishme()
    while True:
        query = takecommand().lower()
        if 'wikipedia'in query:
            speak('Searching wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            print(results)
            speak(results)

        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "open google" in query:
            webbrowser.open("google.com")

        elif "open stackoverflow" in query:
            webbrowser.open("stackoverflow.com")


        elif "play music" in query:
            music_dir = "C:\\Users\\Lenovo\\Music\\New folder"
            songs = os.listdir(music_dir)
            print("songs")
            os.startfile(os.path.join(music_dir,songs[0]))

        elif "the time"in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir,the time is{strTime}")



        elif "open code" in query:
            codePath = "C:\\Users\\Lenovo\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe"
            os.startfile(codePath)

        elif"email to vaibhav" in query:
            try:
                speak("what should i say?")
                content = takecommand()
                to = 'vaibhavguptaa1122@gmail.com'
                sentEmail(to,content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("soory, i am not able to sent this email")










