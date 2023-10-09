import speech_recognition as sr

r = sr.Recognizer() 

with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    print('Speak Anything : ')
    while 1:
    
    	audio = r.listen(source)

    	try:
        	text = r.recognize_google(audio)
        	print('You said: {}'.format(text))
    	except:
        	print('Sorry could not hear')
