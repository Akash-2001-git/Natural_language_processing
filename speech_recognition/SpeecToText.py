import speech_recognition as sp

# initialize the recognition
rec = sp.Recognizer()

# my device index   
my_micro = sp.Microphone(device_index=1)

with my_micro as source:
    print("Say something ...")
    audio = rec.listen(source) # get voice input from your micro

    to_text = rec.recognize_google(audio) # convert audio to text


print(to_text) # print speech recorded from microphone
f = open("text_detected.txt", "a+")
f.write(to_text)
f.close()