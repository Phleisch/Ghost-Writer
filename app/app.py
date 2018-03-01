#Import Flask class and specific functions for our purposes
from flask import Flask, render_template, send_file
#AudioSegment / pydub edits mp3 files and gives us the ability to overlay. MAKE SURE YOU HAVE FFMPEG
from pydub import AudioSegment
#Library for our lyrics to be turned into vocals, via text-to-speech
from gtts import gTTS
#Markov has the methods to generate lyrics - any input file can be used. Default is "raps_all"
from markov_gen_one import getLyrics

#Create an instance of this class. "__name__" is default for a single module
app = Flask(__name__)

#Tells us what URL will trigger flask. If we had route('/landing'), then the URL http://127.0.01.1/landing would trigger flask
@app.route('/')
#def index() is the code bound to the above URL. So when we go to http://127.0.01.1/ - index() is run
def index():
    #Make sure AudioSegment has access to FFMPEG or we will not be able to manipulate mp3 files
    AudioSegment.ffmpeg = "c:/ffmpeg"
    #Generate lyrics using our Markov chain
    lyr = getLyrics()
    generated = {'lyrics' : lyr}
    #Verbalize lyrics, save as an mp3
    tts = gTTS(text="    ".join(lyr), lang='en')
    tts.save("rap.mp3")
    #Overlay lyric verbalization onto an instrumental. Default instrumental is "Ultimate" by Denzel Curry
    sound1 = AudioSegment.from_mp3("rap.mp3")
    sound2 = AudioSegment.from_mp3("instrumentals/ultimate.mp3")
    output = sound2.overlay(sound1,position=20000)
    output.export("static/mixed_sounds.mp3", format="mp3")
    #Give Flask a webpage to display. Generated is a list of lyrics we created. For each line of lyrics, a paragraph is created in the webpage
    return render_template('index.html', title="Home",generated=generated)