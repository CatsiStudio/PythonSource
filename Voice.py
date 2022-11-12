import pyttsx3
 
engine = pyttsx3.init()
while True:
    voiceinput = input('')
    engine.say (voiceinput)
    engine.runAndWait()
