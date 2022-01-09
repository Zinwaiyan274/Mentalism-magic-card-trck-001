import CardList as cl
print(cl.computer_picky())
keyword = cl.keyword

import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak Anything :")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
    except:
        print("Sorry could not recognize what you said")

text = str(text).lower()
# print(text)

if text in keyword:
    print(f"voilà! keyword is >>>{keyword}<<<< and you said >>>>{text}<<<<<")
else:
    print(f"Damm you said>>{text}<<")

# ___________________Not done yet_____________________
