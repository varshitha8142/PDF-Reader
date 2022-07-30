import pyttsx3 
import PyPDF2
from gtts import gTTS                            
import os


# Read the PDF file binary mode
pdf_file = open('2.pdf', 'rb')
read_pdf = PyPDF2.PdfFileReader(pdf_file, strict=False)
#pdf_fil = open("C:/Users/varshi/Desktop/PROJECTS/PYTHON/text.txt", "r")
#myText = pdf_fil.read().replace("\n", " ")
language = 'en'
#output = gTTS(text=myText, lang=language, slow=False)



#Find the number of pages in the PDF document
number_of_pages = read_pdf.getNumPages()
# init function to get an engine instance for the speech synthesis  
engine = pyttsx3.init()
for i in range(0, number_of_pages ):
    # Read the PDF page 
    page = read_pdf.getPage(i)
    
    # Extract the text of the PDF page 
    page_content = page.extractText()
    speaker = pyttsx3.init()
    voices = speaker.getProperty('voices')
    if(voices==0):
#changing index, changes voices, 1 for male
        speaker.setProperty('voice', voices[int(input())].id)
    elif(voices==1):
        speaker.setProperty('voice', voices[int(input())].id)
#changing index, changes voices, (except 1) for female
    else:
        speaker.setProperty('voice', voices[int(input())].id)
    
    # set the audio speed and volume
    newrate=200
    engine.setProperty('rate', newrate)
    newvolume=500
    engine.setProperty('volume', newvolume)
        
    # say method on the engine that passing input text to be spoken 
    engine.say(page_content) 
    
    # run and wait method to processes the voice commands.  
    engine.runAndWait()

    #pdf_fil.close()
    #os.system("aravindvarshit.mp3")
'''
import pyttsx3, PyPDF2

pdfReader = PyPDF2.PdfFileReader(open('C:/Users/varshi/Desktop/PROJECTS/PYTHON/2.pdf', 'rb'))

speaker = pyttsx3.init()

for page_num in range(pdfReader.numPages):
    text =  pdfReader.getPage(page_num).extractText()
    speaker.say(text)
    speaker.runAndWait()
speaker.stop()
engine.save_to_file(text, 'audio.mp3')
engine.runAndWait()
















#import pyttsx3
import pyttsx3 as tts
import PyPDF2
from tkinter.filedialog import *
#from gtts import gTTSAPI

#import os 

engine=tts.init()
voices=engine.getProperty('voices')
for voice in voices:
    engine.setProperty('voice',voice.id)
    rate=engine.getProperty('rate')
    engine.setProperty('rate',rate-1)
    

    pdf = askopenfilename()
    pdfreader=PyPDF2.PdfFileReader(pdf)
    pages=pdfreader.numPages
#output = gTTSAPI(text=pdfreader, lang="en")
    a=int(input("enter which page you want"))
    for i in range(a,pages):
        page=pdfreader.getPage(i)
        text=page.extractText()
        #player=pyttsx3.init()
        #player.say(text)
        engine.say(text)
        engine.runAndWait()
        
....................................................................................................................................................................................

import PyPDF2 
import pyttsx3 
  
# path of the PDF file 
path = open('C:/Users/varshi/Desktop/PROJECTS/PYTHON/2.pdf','rb')  
# creating a PdfFileReader object 
pdfReader = PyPDF2.PdfFileReader(path) 
  
# the page with which you want to start 
# this will read the page of 25th page. 
from_page = pdfReader.getPage(1) 
  
# extracting the text from the PDF 
text = from_page.extractText() 
  
# reading the text 
speak = pyttsx3.init() 
speak.say(text) 
speak.runAndWait()
'''  

    


'''

#....................................................................................................................................................................................

from tkinter import Tk
from tkinter.filedialog import askopenfilename
import pdftotext
from gtts import gTTS

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filelocation = askopenfilename() # open the dialog GUI

with open(filelocation, "rb") as f:  # open the file in reading (rb) mode and call it f
    pdf = pdftotext.PDF(f)  # store a text version of the pdf file f in pdf variable

string_of_text = ''
for text in pdf:
    string_of_text += text

final_file = gTTS(text=string_of_text, lang='en')  # store file in variable
final_file.save("2.mp3") 
'''
