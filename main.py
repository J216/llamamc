from flask import Flask, render_template
import winamp
from subprocess import call

w = winamp.winamp()

app = Flask(__name__)
app.debug = True

main_nav="""
<p>
    <a href="/next">next</a> || <a href="/prev">prev</a>
</p> 
<p>
    <a href="/stop">stop</a> || <a href="/play">play</a><br><br>
</p>
<p>
    MUSIC MODES
</p>
<p>
    <a href="/mode/ton">Type O Negative</a>
    <br><a href="/mode/deep-sleep">Deep Sleep</a>
    <br><a href="/mode/night">Night</a>
    <br><a href="/mode/evening-cooldown">Evening Cooldown</a>
    <br><a href="/mode/evening">Evening</a>
    <br><a href="/mode/workday">Workday</a>
    <br><a href="/mode/morning">Morning</a>
</p></body></html>
"""


@app.route("/")
def index():
    return '<html><head><title>Llama MC</title></head><body><h1><br><br>'+w.getCurrentTrackName()+'</h1><br>'+main_nav

@app.route("/next")
def next():
    w.next()
    return '<html><head><title>Llama MC - Next</title></head><body><h1>'+w.getCurrentTrackName() + '<br><a href="/">home</a></h1></body></html>'

@app.route("/prev")
def prev():
    w.prev()
    return '<html><head><title>Llama MC - Previous</title></head><body><h1>'+w.getCurrentTrackName()+ '<br><a href="/">home</a></h1></body></html>'

@app.route("/stop")
def stop():
    w.stop()
    return '<html><head><title>Llama MC - Stop</title></head><body><h1>'+'Stopped'+ '<br><a href="/">home</a></h1></body></html>'

@app.route("/play")
def play():
    w.play()
    return '<html><head><title>Llama MC - Play</title></head><body><h1>'+w.getCurrentTrackName()+ '<br><a href="/">home</a></h1></body></html>'

@app.route("/mode/<music_mode>")
def musicMode(music_mode):
    call('c:\scr\music-stream-controller\mmsc.bat '+music_mode)
    return '<html><head><title>Llama MC - '+music_mode+' Mode</title></head><body><h1>Mode set to: '+music_mode+'<br>'+w.getCurrentTrackName()+ '<br><a href="/">home</a></h1></body></html>'

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=15432)
