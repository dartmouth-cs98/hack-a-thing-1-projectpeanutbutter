import speech_recognition as sr
import requests

# r = sr.Recognizer()
# mic = sr.Microphone()

# with mic as source:
#     r.adjust_for_ambient_noise(source, duration=0.5)
#     print("Say something!")
#     audio = r.listen(source)
    

# text = r.recognize_google(audio)
text = """if you get burned by the fire we throw water at you if you fall into the lake we throw fire at you there is no such thing as canadian-american because Canada is in North America come to think of it if we you were both born in South America than your American to"""
r = requests.post("http://bark.phon.ioc.ee/punctuator?text=" + text)

print(r.text)