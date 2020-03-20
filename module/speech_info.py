import speech_recognition as sr
import pyttsx3
r = sr.Recognizer()
def speech_recognize(lang):
	with sr.Microphone() as source:
		audio = r.listen(source,phrase_time_limit=3)
		try:
			r.adjust_for_ambient_noise(source)
			text = r.recognize_google(audio,language=lang)
			return text
		except:
			try:
				r.adjust_for_ambient_noise(source,language=lang)
				text = r.recognize_bing(audio)
				return text
			except:
				try:
					r.adjust_for_ambient_noise(source,language=lang)
					text = r.recognize_sphinx(audio)
					return text
				except: pass

def text_to_speech(text):
	engine = pyttsx3.init()
	engine.setProperty('voice','Indonesian')
	engine.say(text)
	print('\n'+str(text))
	engine.runAndWait()
