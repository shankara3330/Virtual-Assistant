import speech_recognition as sr
import pyaudio
import pyttsx3 #text to speech converting 
import pywhatkit #accessing the web content
import datetime #inbuild date and time package
import wikipedia #wikipedia package for PY
import pyautogui #use for taking snaps and screen shots
import time
import pyjokes #Jokes package
import random #generating random number
from time import ctime
import webbrowser 
from PIL import Image
import os # for accessing the app on computer like MUSIC VLC
import smtplib # for sending mail

#An virtual Assistant (Ai) that listens to the user audio and converts it to text 
#and send it back to processing action and gets the results in automated way.

#assinging listener
listener = sr.Recognizer()
name = 'Hari'

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id) #chaining to female voice give 1

# py text to speech function
def talk(text):
    engine.say(text)
    engine.runAndWait();

#wishin function as soon as the AI runs
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if(hour >= 0 and hour <12):
        talk(f'Good Morning {name}')   
    elif hour>=12 and hour<18:
        talk(f'Good afternoon {name}')
    else:
        talk(f'Good Evening {name}')
    talk(f'I am all your ears master how may i help you')

#takes the audio command from MIC
def take_command():
    
        with sr.Microphone() as source:
            print('Listneing...') 
            listener.pause_threshold = 1
            voice = listener.listen(source)
        try:
            print("Recognizing...")
            command = listener.recognize_google(voice,language='en-in')
            command = command.lower()
            

        except Exception:
            print('Say the again master')
            return "None"

        return command
        
        
#all actions  for the command or query is operated here
def run_alexa():
     
    command = take_command()
    # print(command)
    if 'adam' in command:
        command = command.replace('adam','')
        print(f'You said:{command}\n')
        #Play songs and video in YOUTUBE
        if ('in youtube') in command:
            song =command.replace('play', '')
            talk('playing'+ song)
            pywhatkit.playonyt(song)
            return
            
        #Search information about someone or something in  WIKIPEIDA
        elif 'who is' in command:
            person = command.replace('who is','')
            info = wikipedia.summary(person,2)
            talk("according to the internet")
            print(info)
            talk(info)
            return

        elif 'tell me about' in command:
            person = command.replace('tell me about','')
            info = wikipedia.summary(person,2)
            talk("according to the internet")
            print(info)
            talk(info)
            return

        elif 'wikipedia' in command:
            person = command.replace('wikipedia','')
            info = wikipedia.summary(person,2)
            talk("according to the internet")
            print(info)
            talk(info)
            return
        
        #For Date
        elif('what is the date' or 'whats the date today') in command:
            todaydate = datetime.datetime.now().strftime('%D')
            todaydate = todaydate.replace('/', '')
            talk('Today date is'+ todaydate)
            print(todaydate)
            return
        
        #For GMAIL
        elif ("open my mail" or "open gmail" or "check my email")in command:
            url="https://mail.google.com/mail/u/0/#inbox"
            webbrowser.get().open(url)
            talk("here Is your gmails sir")
            return
        
        #For a random Joke
        elif('joke' or 'tell me a worst comdey line') in command:
            joke = pyjokes.get_joke()
            print(joke)
            talk(joke)
            return
        
        #For open YOUTUBE
        elif('open youtube') in command:
            url="https://youtube.com"
            webbrowser.get().open(url)
            print("Here is your Youtube sir")
            talk("Here is your Youtube sir")
            return

        #For open GITHUB
        elif('open github') in command:
            url="https://github.com/HariKharaN"
            webbrowser.get().open(url)
            print("Here is your Github sir")
            talk("Here is your Github sir")
            return
        
        #For Openeing Whatsapp
        elif('open whatsapp') in command:
            url="https://web.whatsapp.com/"
            webbrowser.get().open(url)
            talk("Here is your Whatsapp sir")
            return
        
        #For Openeing Linkedin
        elif('open linkedin') in command:
            url="https://www.linkedin.com/in/hari-haran-k-713061201/"
            webbrowser.get().open(url)
            talk("Here is your Linkedin sir")
            return

        #For open any browser
        elif('open google' or 'open chrome' or 'open web browser') in command:
            url="https://google.com"
            webbrowser.get().open(url)
            talk("Here is your browser sir")
            return

        #for searching any price in internet i.e.. BITCOIN, DOGECOIN, or Any stocks in market 
        elif ('price of')in command:
            search_term = command
            url = "https://google.com/search?q=" + search_term
            webbrowser.get().open(url)
            talk("Here is what I found for " + search_term + " on google")
            return
        
        #For searching some terms in Internet
        elif ('search') in command:
            search_term = command.replace('search','');
            url = "https://google.com/search?q=" + search_term
            webbrowser.get().open(url)
            talk("Here is what I found for" + search_term + "on google")
            return
        
        #Showing my timetable
        elif 'show my time table' in command:
            im = Image.open(r"C:\Users\HARIK\OneDrive\Desktop\lockscreen.jpg")
            im.show()
            return
        
        #capturing the screen
        elif ("capture" or "my screen" or "screenshot")in command:
            myScreenshot = pyautogui.screenshot()
            myScreenshot.save('C:\\Users\\HARIK\\OneDrive\\Pictures')
            return

        #for playing music
        elif('play music' or 'play some music') in command:
            music_dir = 'C:\\Users\\HARIK\\Music\\FAVO'
            songs = os.listdir(music_dir)
            song = songs[random.randint(0,len(songs)-1)]
            os.startfile(os.path.join(music_dir,song))
            return
        
        #for checking time
        elif('what is the time' or 'tell me the time') in command:
            strTime = datetime.datetime.now().strftime("%I:%M %p")
            print(f"Sir, the time is {strTime}")                         
            talk(f"Sir, the time is {strTime}")                         
            return
        
        #for checking weather
        elif ('email to' or 'send email') in command:
            try:
                talk("What should i say")
                content = take_command()
                to="vishnupriyaramesh2001@gmail.com"
                pywhatkit.send_mail('hari88529@gmail.com','7305846355Kh',"",content,to)
                talk("Email as been send")

            except Exception as e:
                print(e)
                talk('Sorry master i am not able to send mail')
            
            return
        
        #for cheching weather out
        elif ("weather" or "tell me the weather report" or "whats the condition outside") in command:
            url = "https://www.google.com/search?sxsrf=ACYBGNSQwMLDByBwdVFIUCbQqya-ET7AAA%3A1578847393212&ei=oUwbXtbXDN-C4-EP5u82AE&q=weather&oq=weather&gs_l=psyab.3..35i39i285i70i256j0i67l4j0i131i67j0i131j0i67l2j0.1630.4591..5475...1.2..2.322.1659.9j5j0j1......0....1..gwswiz.....10..0i71j35i39j35i362i39._5eSPD47bv8&ved=0ahUKEwiWrJvwwP7mAhVfwTgGHfsNDxsQ4dUDCAs&uact=5"
            webbrowser.get().open(url)
            talk("Here is what I found for on google for todays weather")
            return

        #For calculating
        if ("plus" or "minus" or "multiply" or "divide" or "power" or "+" or "-" or "*" or "/") in command:
            opr = command.split()[3]
            if opr == '+':
                talk(int(command.split()[0]) + int(command.split()[5]))
            elif opr == '-':
                talk(int(command.split()[0]) - int(command.split()[2]))
            elif opr == 'multiply':
                talk(int(command.split()[0]) * int(command.split()[2]))
            elif opr == 'divide':
                talk(int(command.split()[0]) / int(command.split()[2]))
            elif opr == 'power':
                talk(int(command.split()[0]) ** int(command.split()[2]))
            else:
                talk("Wrong Operator")
            return
    
        elif('Are you single' or 'do you have a boyfriend')in command:
            talk('I already have a boyfreind')
            return

        elif 'goodbye' in command:
            talk("we could continue more sir, but byee")
            exit()
        
        else:
            talk('Say that again please')
            return
    else:
        talk("who are You, thats not even my name")

#starting function of the AI    
wishMe()
while True:
    run_alexa()
    time.sleep(2)  