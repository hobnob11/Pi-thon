﻿from flask import Flask, render_template
import RPi.GPIO as GPIO

app = Flask(__name__,template_folder="www")
GPIO.setmode(GPIO.BCM)
GPIO.setup(5,GPIO.OUT)

State = False

def SwitchState(Stateu):
    global State
    State = Stateu
    GPIO.output(5,State)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/Output')
def Output():
    global State
    return str(State) + " :D"

@app.route('/Input/<Statuu>')
def Input(Statuu):
    global State
    if(Statuu=="true"):
        SwitchState(True)
    if(Statuu=="false"):
        SwitchState(False)
    return str(State) + "   " + str(Statuu)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=80)