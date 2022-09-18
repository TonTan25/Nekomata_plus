
from googletrans import Translator
from tkinter import *
from PIL import Image, ImageTk
import pyttsx3

a_read = pyttsx3.init()

voices = a_read.getProperty('voices')
en_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
jp_id_3 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_jaJP_AyumiM'

root = Tk()
root.title("Transltort Pro Max")
root.geometry("555x681")
logo = PhotoImage(file= 'F:/PROJECT C/AI/images/staruml_logo.png')
root.iconphoto(True,logo)

load = Image.open('F:/PROJECT C/AI/images/bk_1.jpg')
reder = ImageTk.PhotoImage(load)
img = Label(root,image = reder)
img.place(x=0,y=15)

name = Label(root,text = 'TransLator', fg = '#0000FF',bd= 0,bg ='#F1EFFA')
name.config(font = (("Transformers Movie"),30))
name.pack(padx=10)

box_top = Text(root, width=36,height=10,font=(("Times New Roman"), 16))
box_top.pack(pady=20)

box_bot = Text(root, width=36,height=10,font=(("Times New Roman"), 16))
box_bot.pack(pady=50)

button_frame  = Frame(root).pack(side= BOTTOM)
b = ''
def clear():
    #box_top.delete(1.0,END)
    box_bot.delete(1.0,END)
def trans_ja():
    clear()
    input_top = box_top.get(1.0,END)
    #print(input_top)
    translator = Translator()
    a = translator.translate(input_top, dest='ja', src = 'vi')
    b= '日本 : '+ a.text
    box_bot.insert(END,b)
    return b
def trans_en():
    clear()
    input_top = box_top.get(1.0,END)
    #print(input_top)
    translator = Translator()
    a = translator.translate(input_top, dest='en', src = 'vi')
    b= 'En : ' + a.text
    box_bot.insert(END,b)
    return b
def read():
    b = box_bot.get(1.0,END)
    if '日本' in b:
        id = jp_id_3
        a_read.setProperty("voice",id)
        a_read.say(b)
        a_read.runAndWait()
    elif 'En' in b:
        id = en_id
        a_read.setProperty("voice",id)
        a_read.say(b)
        a_read.runAndWait()


clear_button = Button(button_frame,text = 'CLEAR',font=(("Times New Roman"),15,'bold'),bg= '#000FFF',fg = '#000000',command=clear)
clear_button.place(x= 120,y=320)
trans_button = Button(button_frame,text = 'EN',font=(("Times New Roman"),15,'bold'),bg= '#000FFF',fg = '#000000',command=trans_en)
trans_button.place(x= 230,y=320)
trans_button = Button(button_frame,text = 'JA',font=(("Times New Roman"),15,'bold'),bg= '#000FFF',fg = '#000000',command=trans_ja)
trans_button.place(x= 300,y=320)
read_button = Button(button_frame,text = 'READ',font=(("Times New Roman"),15,'bold'),bg= '#000FFF',fg = '#000000',command=read)
read_button.place(x= 370,y=320)


root.mainloop()


