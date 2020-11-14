import speech_recognition as sr
from translate import Translator

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Listening: ")
    audio = r.listen(source)

try:
    print("You said ---> " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("We can't catch your voice,please try again..")
except sr.RequestError as e:
    print("We can't receive the results,please try again; {0}".format(e))

çevirmen = Translator(to_lang = "tr")
yazı = çevirmen.translate(r.recognize_google(audio))
print(r.recognize_google(audio),"----->",yazı)

                            




























