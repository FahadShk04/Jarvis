import pyttsx3 #for audio
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser #for youtube 
import os #for music
import smtplib #for email
import pyaudio
import pyjokes
# import requests
# from bs4 import BeautifulSouppip 
import pywikihow #for how to do mode
from pywikihow import search_wikihow #for how to do mode

engine= pyttsx3.init('sapi5') #for voice
voices=engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)



def speak(audio): # it is used for speaking
   engine.say(audio)
   engine.runAndWait()

def wishme():
   hour=int(datetime.datetime.now().hour)
   if hour>=4 and hour<12:
      speak("Good Morning!")

   elif hour>=12 and hour<18:
      speak("Good Afternoon!")
    
   else:
      speak("Good Evening!")

   speak("I am Jarvis Sir. Created By Fahad With The Help Of Python Programming Language. Please tell me How may I help You")

def takeCommand(): #it taking audio and microphones and converting it into string and returning it
   
   #It takes command input from the user and return string output

 r=sr.Recognizer()
 with sr.Microphone() as source:
    print("Listening...")
    r.pause_threshold = 1 #it is used for when i take a gap of 1 second beofre giving command it will not get complete
    audio=r.listen(source) #it came from speak recognition
                            
   
 try:
    print("Recognizing...")
    query=r.recognize_google(audio,language='en-in')
    print(f"user said:{query}\n") #here we are recognizing audio which is typed

 except Exception as e:
    # print(e) if uh Want that uh dont to see the error in console then dont write (it is exception)
    print("Say that Again Please...")   
    return "None"
 return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587) #587 port num
    server.ehlo()
    server.starttls()
    server.login('fahadshk04@gmail.com', 'password')
    server.sendmail('receiver@gmail.com',to, content)
    server.close()
    
if __name__=="__main__":
   wishme()
   # while True:
   if 1:
      query= takeCommand().lower() #lower will help you to convert case in lower
    
   #logic for executing tasks based on query 
   if 'wikipedia' in query:
      speak("Searching Wikipedia...")
      query = query.replace("wikipedia", "")
      results = wikipedia.summary(query, sentences=2)  #it will return 2 sentences  from wikipedia
      speak("According to Wikipedia")
      speak(results)
      print(results)

   elif 'open youtube' in query:
      speak("Opening Youtube Sir!")
      webbrowser.open("youtube.com")

   elif 'open google' in query:
      speak("Opening google Sir!")
      webbrowser.open("google.com")
    
   elif 'open stackoverflow' in query:
      speak("Opening stackoverflow Sir!")
      webbrowser.open("stackoverflow.com")

   elif 'open chrome' in query:
      speak("Opening Chrome Sir!")
      webbrowser.open("Chrome.com")

   #elif 'play music' in query:
      #music_dir='D:\\Non Critical\\sings\\Favorite songs2
      #songs = os.listdir(music_dir)
      #print(songs)
      #os.startfile(os.path.join(music_dir, songs[0])) #to open file for songs

   elif 'the time' in query:
      strTime = datetime.datetime.now().strftime("%H:%M:%S")
      speak(f"Sir,The Time is {strTime}")
      print(strTime)

#    elif 'open code' in query:
#       codepath = __path__
#       os.startfile(codepath)
   elif 'email to fahad' in query:
    try:
         speak("What Should I say?")
         content = takeCommand()
         to = "fahadshk04@gmail.com"
         sendEmail(to, content)
         speak("Email has been sent!")
    except Exception as e:
       print(e)
       speak("Sorry Fahad Bhai. I am Not able To send this email")   

   elif "hello" in query:
      speak("Hi there!")
   elif "goodbye" in query:
      speak("GoodBye Have a great Day!")

   elif 'who am i' in query:
      speak("I am not Sure But i think you are Fahad Shaikh sorry if i don't recognize your voice")

   # elif 'activate how to do mode' in query:
   #    speak("How to do Mode is Activated. Please tell me what you want to know?")
   #    how=takeCommand() #how is a command name
   #    max_result=1 #dont increase more then 1
   #    how_to = search_wikihow(how, max_result) #it is a function tht takes query max_result = 10 and then lang
   #    assert len(how_to)==1 #used for assertion if how to level is equal to max_result then only it will run otherwise error
   #    how_to[0].print() #we take the length of 0th position and print it.
   #    speak(how_to[0].summary) #we summary the length of the 0th position
   elif'tell me a joke' in  query:
      speak(pyjokes.get_jokes())

   elif 'activate how to do mode' in query:
      speak("How to do Mode is Activated. Please tell me what you want to know?")
      while True:
         how=takeCommand()
         try:
            if "exit" in how or "close" in how:
               speak("okay sir,how to do mode is closed")
               break
            else:
               max_result=1 #dont increase more then 1
               how_to = search_wikihow(how, max_result) #it is a function tht takes query max_result = 10 and then lang
               assert len(how_to)==1 #used for assertion if how to level is equal to max_result then only it will run otherwise error
               how_to[0].print() #we take the length of 0th position and print it.
               speak(how_to[0].summary) #we summary the length of the 0th position
         except Exception as e:
            speak("sorry sir,i am not able to find this")
   else:
      speak("Sorry But there is no such query like this!")
      print(speak)