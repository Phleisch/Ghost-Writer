import os
from pydub import AudioSegment
from gtts import gTTS
from rap_god import getLyrics


def textToRap():
	sounds = []
	texttospeech = []
	for i in range(0,7):
		lyr = getLyrics()
		generated = {'lyrics' : lyr}
		tts = gTTS(text="".join(lyr), lang='en', slow=False)
		sounds.append(tts)
		name = "vocals"
		name = name+str(i)+".mp3"
		tts.save(name)
		texttospeech.append((AudioSegment.from_mp3(name) + 5))
		os.remove(name)
	instrumental = (AudioSegment.from_mp3("ultimate.mp3") - 10)
	songv1 = instrumental.overlay(texttospeech[0][:37250],position=16750)
	songv2 = songv1.overlay(texttospeech[1][:36750],position=54860)
	songv3 = songv2.overlay(texttospeech[2][:37500],position=92500)
	#songv4 = songv3.overlay(texttospeech[3][:17250],position=130500)
	#songv5 = songv4.overlay(texttospeech[4][:29000].fade_out(3000),position=148300)
	#songv5.export("rap.mp3", format="mp3")
	songv4 = songv3.overlay(texttospeech[3][:3600],position=130500)
	songv5 = songv4.overlay(texttospeech[4][:9150],position=134500)
	songv6 = songv5.overlay(texttospeech[5][:3750],position=144250)
	songv7 = songv6.overlay(texttospeech[6][:28500].fade_out(3000),position=148300)
	songv7.export("rap.mp3", format="mp3")

if __name__ == '__main__':
	textToRap()
