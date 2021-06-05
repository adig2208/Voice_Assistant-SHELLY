import pyttsx3
import wikipedia
import datetime
import webbrowser
import os
import smtplib
import time
import speech_recognition as sr
from playsound import playsound

global n
n = "Shelly"
def begin():
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    rate = engine.getProperty('rate')   
    engine.setProperty('rate', 180)
    def run(text):
        engine.say(text)
        engine.runAndWait()
    run("Initializing...")
    run("Installing all drivers")
    run("Checking all connections with the core processors")
    run("Backing up all databases")
    run("Taking control in...")
    run("3")
    run("2")
    run("1")

def speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    rate = engine.getProperty('rate')   
    engine.setProperty('rate', 170)
    engine.say(text)
    engine.runAndWait()

r=sr.Recognizer()
def entry():
    while(1):
        try:
            with sr.Microphone() as source2:
                print("Listening...")
                r.adjust_for_ambient_noise(source2, duration=0.2) 
                audio =r.listen(source2)
                print("Reconizing...")
                global text
                text = r.recognize_google(audio , language='en-in')
                text = text.lower()
                x = datetime.datetime.now().hour
                if x < 12:
                    speak(f"Good morning {text}.")
                    break
                elif x > 12 and x < 16:
                    speak(f"Good afternoon {text} .")
                    break
                else:
                    speak(f"Good evening {text} .")
                    break
                
        except sr.RequestError as e: 
            print("Could not request results; {0}".format(e)) 
              
        except sr.UnknownValueError: 
            speak("Say that again") 

def takeCommand():
    while(1):
        try:
            with sr.Microphone() as source:
                print("Listening...")
                r.adjust_for_ambient_noise(source, duration=0.2) 
                audio2 =r.listen(source)
                print("Recognizing...")
                query = r.recognize_google(audio2 , language='en-in')
                query = query.lower()
                print(f"user said: {query}")
                break
        except sr.UnknownValueError:
            speak("Say that again") 
    return query

def emailRequest():
	while(1):
		try:
			with sr.Microphone() as source7:
				print("Listening...")
				r.adjust_for_ambient_noise(source7 , duration=0.2)
				audio7 = r.listen(source7)
				print('Recognizing...')
				queryy = r.recognize_google(audio7 , language='en-in')
				queryy = queryy.lower()
				queryy = queryy.replace(" ", "")
				print(f"user said: {queryy}")
				break
		except sr.UnknownValueError:
			speak("say that again")
	return queryy

def weather():
    import requests
    from pprint import pprint
    def weather_data(querry):
        res=requests.get('http://api.openweathermap.org/data/2.5/weather?'+querry+'&APPID=your API id&units=metric');
        return res.json();
    def print_weather(result,city):
        print("{}'s temperature: {}°C ".format(city,result['main']['temp']))
        speak("{}'s temperature: {}°C ".format(city,result['main']['temp']))
        print("Wind speed: {} m/s".format(result['wind']['speed']))
        speak("Wind speed: {} metres per second".format(result['wind']['speed']))
        print("Description: {}".format(result['weather'][0]['description']))
        speak("Description: {}".format(result['weather'][0]['description']))
        print("Weather: {}".format(result['weather'][0]['main']))
        speak("Weather: {}".format(result['weather'][0]['main']))
    def main():
        try:
            with sr.Microphone() as source3:
                speak("Which place's weather report do you need?")
                print("Listening...")
                r.adjust_for_ambient_noise(source3, duration=0.2) 
                audio3 =r.listen(source3)
                print("Reconizing...")
                city = r.recognize_google(audio3 , language='en-in')
                city = city.lower()
        except Exception as e:
            speak("say that again")        
        try:
            querry='q='+city;
            w_data=weather_data(querry);
            print_weather(w_data, city)
            print()
        except:
            print('City name not found...')
    if __name__=='__main__':
        main()

def sendEmail(to,content):
	server = smtplib.SMTP('smtp.gmail.com' , 587)
	server.ehlo()
	server.starttls()
	server.login("mail" , 'password')
	server.sendmail("mail",to,content)
	server.close()

def activate():
    begin()
    playsound("D:\\projects\\Voice_assistant\\sound2.mp3")
    speak("Hello Humans")
    speak(f"I am {n}")
    speak("What should I call you?")
    entry()
    speak("How may I help you?")

activate()
query = takeCommand() 
while 'nothing' not in query.lower() and 'bye' not in query.lower():
    if 'wikipedia' in query.lower():
        speak("Searching Wikipedia... Give me a sec")
        query = query.replace("wikipedia","")
        result = wikipedia.summary(query, sentences = 2)
        print(result)
        speak(f"{result}")
    elif 'youtube' in query.lower():
        speak("Opening Youtube...")
        url ="youtube.com"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)
    elif 'instagram' in query.lower():
        speak("Opening instagram...")
        url ="instagram.com"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)
    elif 'facebook' in query.lower():
        speak("Opening facebook...")
        url ="facebook.com"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)
    elif 'twitter' in query.lower():
        speak("Opening twitter...")
        url ="twitter.com"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)
    elif 'weather' in query.lower():
        weather()
    elif 'sublime' in query.lower():
        sublime_dir='C:/Program Files/Sublime Text 3/sublime_text.exe'
        speak("opening sublime ")
        os.startfile(sublime_dir)
    elif 'visual studo' in query.lower():
        vs_dir='C:/Users/adity/AppData/Local/Programs/Microsoft VS Code/Code.exe'
        speak("opening visual studio code")
        os.startfile(vs_dir) 
    elif 'google' in query.lower():
        speak("Opening google...")
        url ="google.com"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)
    elif 'gmail' in query.lower():
        speak("opening gmail")
        url ="gmail.com"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)
    elif 'time' in query.lower():
        y = datetime.datetime.now().hour
        z = datetime.datetime.now().minute 
        if y>12:
            speak(f"The time is {y-12} {z} p m")
        elif y<12:
            speak(f"The time is {y} {z} a m")
    elif 'euro school' in query.lower():
    	speak("Opening Argus....")
    	url = "https://euro.learnindialearn.in/login"
    	chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    	webbrowser.get(chrome_path).open(url)
    elif 'spotify' in query.lower() or 'music' in query.lower():
    	speak("Opening spotify...")
    	songs_dir = 'C:\\Users\\adity\\AppData\\Roaming\\Spotify\\Spotify.exe'
    	os.startfile(songs_dir)
    elif 'date' in query.lower():
    	import datetime
    	d1=datetime.datetime.now()
    	d1= d1.strftime("%B %d %Y")
    	speak(f"Today's date is {d1}")
    elif 'day' in query.lower():
    	d2=datetime.datetime.now().strftime("%A")
    	speak(f"Today's day is {d2}")
    elif 'mail' in query.lower():
    	speak("What shoud I send?")
    	content = takeCommand()
    	speak("who should i send to this mail to?")
    	to = emailRequest()
    	print(f"{to}")
    	speak("is this the correct email id?")
    	reply = takeCommand()
    	if 'yes' in reply.lower():
    		sendEmail(to,content)
    		speak("Mail has been sent successfully")
    	elif 'no' in reply.lower():
    		speak("okay you will have to repeat this process.")
    elif 'year' in query.lower():
    	d3= datetime.datetime.now().strftime("%Y")
    	speak(f"The year is {d3}")
    elif 'your name' in query.lower():
    	speak("My name is Shelly")
    elif 'bored' in query.lower():
    	speak("okay let's play my favourite game ")
    	speak("I bet you can't beat my highscore ")
    	speak("ps my high score is 5000")
    	url = "https://chromedino.com/"
    	chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    	webbrowser.get(chrome_path).open(url)
    elif 'notepad' in query.lower():
    	import subprocess
    	subprocess.Popen('C:\\Windows\\System32\\notepad.exe')
    elif 'paint' in query.lower():
    	import subprocess
    	subprocess.Popen('C:\\Windows\\System32\\mspaint.exe')
    elif 'meet' in query.lower():
        speak("opening meet...")
        url = 'https://meet.google.com/utz-ekev-fee?pli=1&authuser=1'
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)
    elif 'udemy' in query.lower():
        url = 'udemy.com'
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        speak("opening udemy...")
        webbrowser.get(chrome_path).open(url)
    elif 'coursera' in query.lower():
        url = 'https://www.coursera.org/programs/ves-institute-of-technology-on-coursera-jvo5a'
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        speak("opening coursera...")
        webbrowser.get(chrome_path).open(url)
    elif 'wait' in query.lower():
    	speak("Just press b and enter if you need me.")
    	p= input()
    	if p == "b":
    		time.sleep(5)
    speak(f"what more do you need {text}?")
    query= takeCommand()       
else:
	t=datetime.datetime.now().hour
	if t > 5 and t < 21:
		speak(f"okay bye {text} ")
		speak("have a nice day")
		SystemExit() 
	else:
		speak(f"okay bye {text} ")
		speak("Good Night")
		SystemExit()


    


