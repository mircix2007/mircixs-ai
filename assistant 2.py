import os
import pyttsx3
import speech_recognition as sr
import webbrowser
from datetime import datetime
import wikipedia
import pyautogui


# this method is for taking the commands
# and recognizing the command from the
# speech_Recognition module we will use
# the recongizer method for recognizing
from self import self


def takeCommand():
    r = sr.Recognizer()

    # from the speech_Recognition module
    # we will use the Microphone module
    # for listening the command
    with sr.Microphone() as source:
        print('Listening')

        # seconds of non-speaking audio before
        # a phrase is considered complete
        r.pause_threshold = 0.7
        audio = r.listen(source)

        # Now we will be using the try and catch
        # method so that if sound is recognized
        # it is good else we will have exception
        # handling
        try:
            print("Recognizing")

            # for Listening the command in indian
            # english we can also use 'hi-In'
            # for hindi recognizing
            Query = r.recognize_google(audio, language='en-in')
            print(Query)

        except Exception as e:
            print(e)
            print("Say that again sir")
            return "None"

        return Query


def speak(audio):
    engine = pyttsx3.init()
    # getter method(gets the current value
    # of engine property)
    voices = engine.getProperty('voices')

    # setter method .[0]=male voice and
    # [1]=female voice in set Property.
    engine.setProperty('voice', voices[1].id)

    # Method for the speaking of the the assistant
    engine.say(audio)

    # Blocks while processing all the currently
    # queued commands
    engine.runAndWait()


def tellDay():
    # This function is for telling the
    # day of the week
    day = datetime.datetime.today().weekday() + 1

    # this line tells us about the number
    # that will help us in telling the day
    Day_dict = {1: 'Monday', 2: 'Tuesday',
                3: 'Wednesday', 4: 'Thursday',
                5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}

    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
        speak("The day is " + day_of_the_week)

def findphone():
    webbrowser.open("https://www.icloud.com")
    pyautogui.moveTo(883, 668, duration = 5)
    pyautogui.leftClick(883,668)
    pyautogui. leftclick(955, 623)
    pyautogui. leftclick(1098, 571)
    pyautogui.leftclick(1094,613)
    pyautogui.leftclick(1277,829)
    pyautogui.moveTo(954, 636, duration, = 2)|
    pyautogui. leftclick(954, 636)
    pyautogui.leftclick(948,664)
    pyautogui.leftclick(951,695)
    pyautogui.moveTo(969, 119, duration = 2)
    pyautogui.leftclick(969,119)
    pyautogui. leftClick(955, 280)
    pyautogui.leftClick(64,337)

def tellTime():
    now = datetime.now()

    current_time = now.strftime("%H hours %M minutes and %S seconds")

    speak("Current Time is :" + current_time)

def Hello():
    # This function is for when the assistant
    # is called it will say hello and then
    # take query
    speak("Hello sir I am your desktop assistant. Tell me how may I help you")

def playstarcraft():
    os.startfile(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Battle.net\Battle.net.lnk")
    pyautogui.moveTo(841, 696, duration = 2)
    pyautogui.click(841, 696)


def music():
    os.startfile(r"C:\Users\MIRCIX\OneDrive\Desktop\shortcuts for assistant\iTunes.exe.lnk")
    pyautogui.moveTo(1821, 178, duration = 2)
    pyautogui.leftClick(1821, 178)

def enjoysilence():
    os.startfile(r"C:\Users\MIRCIX\OneDrive\Desktop\shortcuts for assistant\iTunes.exe.lnk")
    pyautogui.moveTo(266, 429, duration = 2)
    pyautogui.click(1821, 178)


def Take_query():
    # calling the Hello function for
    # making it more interactive
    Hello()

    # This loop is infinite as it will take
    # our queries continuously until and unless
    # we do not say bye to exit or terminate
    # the program
    while (True):

        # taking the query and making it into
        # lower case so that most of the times
        # query matches and we get the perfect
        # output
        query = takeCommand().lower()
        if "Open geeksforgeeks" in query:
            speak("Opening GeeksforGeeks ")

            # in the open method we just to give the link
            # of the website and it automatically open
            # it in your default browser
            webbrowser.open("www.geeksforgeeks.com")
            continue

        if "open brave" in query:
            speak("Opening Brave ")
            webbrowser.open("www.google.com")
            print("brave")
            continue

        if "day" in query:
            tellDay()
            continue

        if "time" in query:
            tellTime()
            continue

        # this will exit and terminate the program
        if "bye" in query:
            exit()

        if "wikipedia" in query:

            # if any one wants to have a information
            # from wikipedia
            speak("Checking the wikipedia ")
            query = query.replace("wikipedia", "")

            # it will give the summary of 4 lines from
            # wikipedia we can increase and decrease
            # it also.
            result = wikipedia.summary(query, sentences=4)
            speak("According to wikipedia")
            speak(result)

        if "tell me your name" in query:
            speak("I am Marvin. Your desktop Assistant")

        if "play music" in query:
            music()
            continue

        if "play enjoy the silence" in query:
            enjoysilence()
            continue

        if "go to sleep" in query:
            os.startfile(r"C:\Users\MIRCIX\OneDrive\Desktop\shortcuts for assistant\sleep command.bat")

        if "play starcraft" in query:
            playstarcraft()

        if "find my phone" in query:
            findphone()








if __name__ == '__main__':
    # main method for executing
    # the functions
    Take_query()
