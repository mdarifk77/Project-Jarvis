import speech_recognition as sr
import webbrowser
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id) # 0 = male, 1 = female (depends on system)
    engine.setProperty('rate', 170)  # Speed (default ~200)
    engine.setProperty('volume', 1)  # Volume (0.0 to 1.0)
    engine.say(text)
    engine.runAndWait()
    
def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://www.google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://www.linkedin.com")   
    elif "open instagram" in c.lower():
        webbrowser.open("https://www.intagram.com")   
              
    
        
if __name__ == "__main__":
    speak("initializing jarvis.......")
    
    while True:   
            # listen for the wake word jarvis 
        
            # obtain audio from the microphone
        r = sr.Recognizer()
        
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("listening....")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word =  r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("yes sir") 
            # listen for commands 
                    
            with sr.Microphone() as source:
                print("Jarvis Active....")
                audio = r.listen(source)
                command =  r.recognize_google(audio) 
                
                processCommand(command)
               
        except Exception as e:
            print(" Error; {0}".format(e))    
    