import speech_recognition as sr 

nekomata_listen = sr.Recognizer()
with sr.Microphone() as mic:
	print('hay noi voi toi ... ')
	audio_data = nekomata_listen.record(mic, duration=5)
	print('toi dang nghe ...')
	try:
		txt = nekomata_listen.recognize_google(audio_data, language="vi")
	except:
		txt = 'toi khong hieu ban noi gi'
	print(txt)
	