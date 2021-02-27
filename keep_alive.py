
from flask import Flask
from threading import Thread

###################################
#this is to keep the bot alive using uptime bot while in repl.it
#goto to uptime bot and set your monitors there
app = Flask('')
@app.route('/')

def home():
    return"discord.py is alive! yaay!"
def run():
    app.run(host ='0.0.0.0', port = 8080)


def keep_alive():
   t = Thread(target = run)
   t.start()