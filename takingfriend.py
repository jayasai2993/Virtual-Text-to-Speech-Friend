import pyttsx3
vtf = pyttsx3.init()

""" RATE"""
rate = vtf.getProperty('rate')   # getting details of current speaking rate
#print (rate)                        #printing current voice rate
vtf.setProperty('rate', 160)     # setting up new voice rate
def vtf_speak(text):
    print('speaking.....')
    vtf.say(txt)
    vtf.runAndWait()

txt="hello friend , i am your virtual friend ,enter bye to exit"
print("enter bye to exit")
vtf_speak(txt)

while txt != "bye":
    txt = input(" what should i say :")
    txt =txt.lower()
    if txt != 'bye':
        vtf_speak(txt)
    else:
        vtf_speak('see you again friend ,that was a nice talking talking you')
input()