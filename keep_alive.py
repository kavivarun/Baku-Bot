from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Hello. I am alive!"

#hosts server
def run():
  app.run(host='0.0.0.0',port=8080)

#command for starting thread
def keep_alive():
    t = Thread(target=run)
    t.start()