from gtts import gTTS
import pyttsx3

def runGtts(txt):
	tts = gTTS(text=txt, lang='en')
	tts.save("test.mp3")

def runPtts(txt):
	engine = pyttsx3.init()
	engine.say(txt)
	engine.runAndWait()


# engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# for voice in voices:
#    print(voice.id)
#    engine.setProperty('voice', voice.id)
#    engine.say('The quick brown fox jumped over the lazy dog.')
# engine.runAndWait()

txt = 'Brianna is a beautiful girl'
genSpeechFile(txt)

