import googletrans
from googletrans import Translator
import pyttsx3


nekomata_speak = pyttsx3.init()

voices = nekomata_speak.getProperty('voices')
jp_id_3 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_jaJP_AyumiM'

def speaks(nekomata_brain):
    nekomata_speak.setProperty("voice",jp_id_3)
    nekomata_speak.say(nekomata_brain)
    nekomata_speak.runAndWait()

def trans(nekomata_brain):
    translator = Translator()
    nekomata_brain = translator.translate(nekomata_brain, dest='ja', src = 'vi').text
    return nekomata_brain

if __name__ == '__main__':
    nekomata_brain = str(input("Nhập văn bản :"))
    nekomata_brain = trans(nekomata_brain)
    print(nekomata_brain)
    speaks(nekomata_brain)