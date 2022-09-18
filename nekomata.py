import webbrowser as wb
import speech_recognition as sr
from datetime import  datetime
from googletrans import Translator
import googletrans
import wikipedia
import pyttsx3


nekomata_speak = pyttsx3.init()

voices = nekomata_speak.getProperty('voices')
nekomata_listen = sr.Recognizer()
now = datetime.now()
txt = ""
nekomata_brain = ""
url = ""
vn_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_viVN_An'
jp_id_3 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_jaJP_AyumiM'

def speak_ja(nekomata_brain):
    nekomata_speak.setProperty("voice",jp_id_3)
    nekomata_speak.say(nekomata_brain)
    nekomata_speak.runAndWait()

def speak_vn(nekomata_brain):
    nekomata_speak.setProperty("voice",vn_id)
    nekomata_speak.say(nekomata_brain)
    nekomata_speak.runAndWait()
    
def micro(txt):
    with sr.Microphone() as mic:
        print('Hãy nói với tôi  ... ')
        audio_data = nekomata_listen.record(mic, duration=5)
        #print('toi dang nghe ...')
        try:
            txt = nekomata_listen.recognize_google(audio_data, language="vi")
        except:
            txt = 'Tôi đang không hiểu bạn nói gì cả !'+'\nbạn có thể nói lại được không.'
            txt = str(input('bạn có thể nhập : '))
        print(txt)
    return txt

def welcome():
    Hours = datetime.now().hour
    if Hours >= 6 and Hours <11:
        nekomata_brain = "Chào buổi sáng bạn hiền !"
    elif Hours >= 11 and Hours <12:
        nekomata_brain = "buổi trưa tốt lành"
    elif Hours >= 13 and Hours <18:
        nekomata_brain = "Chào buồi chiều nhé."
    elif Hours >=18 and Hours <24:
        nekomata_brain = "Buổi tối tốt lành."
    if Hours >= 0 and Hours <6:
        nekomata_brain = "Bình minh mới tốt lành."
    print(nekomata_brain)
    speak_vn(nekomata_brain)

def open_file(url):
    print("bạn hãy nhập đường đẫn")
    a = str(input("ổ đĩa : "))
    b = str(input("thư mục : "))
    c = str(input("thư mục : "))
    d = str(input("thư mục : "))
    url = f'{a}/{b}/{c}/{d}'
    print("đường dẫn : " + url)
    return url

def trans(nekomata_brain):
    translator = Translator()
    a = str(input("Nhập văn bản :"))
    nekomata_brain = translator.translate(a, dest='ja', src = 'vi').text
    return nekomata_brain

if __name__ == "__main__":
    welcome()
    while True:
        text = micro(txt)
        if text == "":
            nekomata_brain = "bạn vui lòng nói lại được không !"      
        elif "đọc văn bản" in text:
            nekomata_brain = str(input("bạn hãy nhập vào đây: "))
        elif "Xin chào" in text :
            nekomata_brain = "chào bạn. bẹn khẻo hông !"
        elif "ngày bao nhiêu" in text :
            nekomata_brain = now.strftime("hôm nay là ngày %d tháng %m năm %Y")
        elif "mấy giờ" in text :
            nekomata_brain = now.strftime("%H:%M:%S")
        elif "mở thư mục" in text:
            speak_vn(" Vui lòng nhập đường dẫn thay nói .")
            if url != "":
                url=""
                url= open_file(url)
                wb.open(url)
        elif "Mở nhạc" in text:
            speak_vn(" nhạc của bạn đây.")
            url = "F:/OTHER FILE/Paimon hehe 'te nandayo-.mp4"
            print("đường dẫn : " + url)
            wb.open(url)
        elif "dịch văn bản" in text:
            nekomata_brain = trans(nekomata_brain)
            speak_ja(nekomata_brain)
        elif "Wiki" in text:
            while True:
                print("bạn muốn tìm gì trên Wiki nào :")
                text = micro(txt)
                if text :
                    if "ngừng tìm kiếm"in text:
                        break
                    else:
                        wikipedia.set_lang("vi")
                        nekomata_brain = wikipedia.summary(text, sentences=2)
                        print(nekomata_brain)
                        speak_vn(nekomata_brain)
                    nekomata_brain = "Đã ngường tìm kiếm trên Wiki."
        elif "Google" in text:
            speak_vn("bạn tìm kiếm gì trên Google : ")
            search = micro(txt)
            url = f"https://www.google.com.vn/search?q={search}"
            wb.get().open(url)
            nekomata_brain = f'Google {search} của bạn đây'
        elif "YouTube" in text:
            speak_vn("bạn tìm kiếm gì trên Youtube : ")
            search = micro(txt)
            url = f"https://www.youtube.com/search?q={search}"
            wb.get().open(url)
            nekomata_brain = f'Youtube {search} của bạn đây'
        elif "Goodbye" in text :
            nekomata_brain = " chao bẹn nhé "
            speak_vn(nekomata_brain)
            break
        print(nekomata_brain)
        speak_vn(nekomata_brain)
        #speak(nekomata_brain)