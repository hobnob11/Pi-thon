from flask import Flask, render_template, request
import RPi.GPIO as GPIO

app = Flask(__name__,template_folder="www")
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(5,GPIO.OUT)

State = 0

def SwitchState(Stateu):
    global State
    State = Stateu
    GPIO.output(5,State)

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

@app.route('/Input/<Statuu>')
def Input(Statuu):
    global State
    if(Statuu=="1"):
        SwitchState(1)
    if(Statuu=="0"):
        SwitchState(0)
    return str(State) + "   " + str(Statuu)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=80)

