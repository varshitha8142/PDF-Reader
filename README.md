# PDF-Reader

It reads aloud everything that text is present on that PDF or Image.





**Project description** </br>
pyttsx3 is a text-to-speech conversion library in Python. Unlike alternative libraries, it works offline, and is compatible with both Python 2 and 3.
</br>

**Installation** </br>
pip install pyttsx3
If you recieve errors such as No module named win32com.client, No module named win32, or No module named win32api, you will need to additionally install pypiwin32.</br>

**Usage :** </br>
import pyttsx3
engine = pyttsx3.init()
engine.say("I will speak this text")
engine.runAndWait()
Changing Voice , Rate and Volume :

import pyttsx3
engine = pyttsx3.init() # object creation
</br>
**RATE**</br>
rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', 125)     # setting up new voice rate
</br>


