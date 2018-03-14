import os
from pydub import AudioSegment
from gtts import gTTS
from god_rap import get_lyrics

def text_to_rap():
	result = []
	song = (AudioSegment.from_mp3("instrumentals/ultimate.mp3") - 10)
	offset = 16750
	for i in range(0,5):
		lyr = get_lyrics()
		for line in lyr:
			tts = gTTS(text=line, lang='en', slow=False)
			tts.save("vocals.mp3")
			bar = (AudioSegment.from_mp3("vocals.mp3") + 5)
			if i == 0 and (offset + len(bar)) <= 54860:
				song = song.overlay(bar,position=offset)
				offset += len(bar)
				result.append(line)
			elif i == 0:
				offset = 54860
				break
			elif i == 1 and (offset + len(bar)) <= 92500:
				song = song.overlay(bar,position=offset)
				offset += len(bar)
				result.append(line)
			elif i == 1:
				offset = 92500
				break
			elif i == 2 and (offset + len(bar)) <= 130500:
				song = song.overlay(bar,position=offset)
				offset += len(bar)
				result.append(line)
			elif i == 2:
				offset = 130500
				break
			elif i == 3 and (offset + len(bar)) <= 148300:
				song = song.overlay(bar,position=offset)
				offset += len(bar)
				result.append(line)
			elif i == 3:
				offset = 148300
				break
			elif i == 4 and offset + len(bar) <= 179800:
				song = song.overlay(bar,position=offset)
				offset += len(bar)
				result.append(line)
		result[-1] += "\n"
	os.remove("vocals.mp3")
	song.export("static/ultimate_rap.mp3", format="mp3")
	return result

if __name__ == '__main__':
	final_song = text_to_rap()
	for i in range(len(final_song)):
		print(final_song[i])
