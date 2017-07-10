from flask import Flask, render_template
import winamp
from subprocess import call

w = winamp.winamp()


page_info = {}
page_info['business_name'] = u"Llama MC"
page_info['desciption'] = u"Music stream controller for AMS-Cluster"
page_info['about'] = u"Lets see where the llama runs now"
page_info['phone'] = u"(660) 541-1026"
page_info['phone_link'] = u"+16605411026"
page_info['address'] = u"Saint Joseph MO"
page_info['email'] = u"jaredhaer@gmail.com"
page_info['facebook'] = u"https://www.facebook.com/jared.haer/"
page_info['twitter'] = u"https://twitter.com/jared216"
page_info['now_playing']=u"None"


app = Flask(__name__)
app.debug = True


@app.route("/")
def index():
    page_info['now_playing']=w.getCurrentTrackName()
    return render_template("index.html",page_info=page_info)

@app.route("/next")
def next():
    w.next()
    page_info['now_playing']=w.getCurrentTrackName()
    return render_template("index.html",page_info=page_info)

@app.route("/prev")
def prev():
    w.prev()
    page_info['now_playing']=w.getCurrentTrackName()
    return render_template("index.html",page_info=page_info)

@app.route("/stop")
def stop():
    w.stop()
    page_info['now_playing']=w.getCurrentTrackName()
    return render_template("index.html",page_info=page_info)

@app.route("/play")
def play():
    w.play()
    page_info['now_playing']=w.getCurrentTrackName()
    return render_template("index.html",page_info=page_info)

@app.route("/mode/<music_mode>")
def musicMode(music_mode):
    call('c:\scr\music-stream-controller\mmsc.bat '+music_mode)
    page_info['now_playing']=w.getCurrentTrackName()
    return render_template("index.html",page_info=page_info)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=15432)
