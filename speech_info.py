import speech_recognition as sr
r = sr.Recognizer()
def spoke():
	with sr.Microphone() as source:
		audio = r.listen(source,phrase_time_limit=3)
		try:
			r.adjust_for_ambient_noise(source,duration=0.5)
			text = r.recognize_google(audio,language='id-ID')
			return text
		except:
			try:
				r.adjust_for_ambient_noise(source,duration=0.5,language='id-ID')
				text = r.recognize_bing(audio)
				return text
			except:
				try:
					r.adjust_for_ambient_noise(source,duration=0.5,language='id-ID')
					text = r.recognize_sphinx(audio)
					return text
				except: pass
