import pyttsx3

myfile= open("hello.txt")
info=myfile.readlines()
myfile.close()

engine= pyttsx3.init()
engine.say(info)
engine.runAndWait()