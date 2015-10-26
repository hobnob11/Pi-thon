﻿from flask import Flask, render_template, request
import RPi.GPIO as GPIO

app = Flask(__name__,template_folder="www")
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(5,GPIO.OUT)

State = 0
Allowed = ["Public"]

def SwitchState(A):
    global State
    State = A
    GPIO.output(5,State)

def CheckIfAllowed(A):
    global Allowed
    try:
        index = Allowed.index(A)
    except ValueError:
        return False
    else:
        return True



@app.route('/')
def index():
    #if the incomming request is on the local network
    if(str(request.remote_addr)[:10] == "192.168.1."):
        return render_template("admin.html")
    else:
        return render_template("index.html")

@app.route('/Output')
def Output():
    global State
    return str(State) + " :D"

@app.route('/Input/<Id>/<Input>')
def Input(Id,Input):
    global State
    print(str(CheckIfAllowed(Id)))
    if(Input=="1"):
        SwitchState(1)
    if(Input=="0"):
        SwitchState(0)
    return str(State) + "   " + str(Input)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=80)

