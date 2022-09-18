import pyttsx3


nekomata_speak = pyttsx3.init()

voices = nekomata_speak.getProperty('voices')

for voice in voices:
    print("Voice:")
    print(" - ID: %s" % voice.id)
    print(" Name: %s" % voice.name)
    print(" Languages: %s" % voice.languages)
    print(" Gender: %s" % voice.gender)
    print(" Age: %s" % voice.age)



jp_id_1 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_jaJP_SayakaM'
jp_id_2 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_JA-JP_HARUKA_11.0'
jp_id_3 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_jaJP_AyumiM'
vn_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_viVN_An'
def speaks(nekomata_brain):
    nekomata_speak.setProperty("voice",jp_id_3)
    nekomata_speak.say(nekomata_brain)
    nekomata_speak.runAndWait()

if __name__ == "__main__":
    nekomata_brain = input('Hãy viết : ')
    speaks(nekomata_brain)