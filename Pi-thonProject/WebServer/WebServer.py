from flask import Flask, render_template, request
import RPi.GPIO as GPIO

app = Flask(__name__,template_folder="www")
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(5,GPIO.OUT)

State = 0
Allowed = ["Public"]
Requests = []

def SwitchState(A):
    global State
    State = A
    GPIO.output(5,State)

def CheckIfAllowed(A):
    global Allowed
    try:
        index = Allowed.index(A)
    except ValueError:
        return -1
    else:
        return index
def CheckIfRequested(A):
    global Requested
    try:
        index = Requested.index(A)
    except ValueError:
        return False
    else:
        return True

@app.route('/')
def index():
    #if the incomming request is on the local network
    if(str(request.remote_addr)[:10] == "192.168.1."):
        return render_template("admin.html",Allowed = Allowed,Requested = Requested)
    else:
        return render_template("index.html")

@app.route('/ADMIN/<NewID>')
def ADMIN(NewID):
    global Allowed
    if(str(request.remote_addr)[:10] == "192.168.1."):
        if(CheckIfAllowed(NewID)!=-1):
            Allowed.remove(NewID)
        else:
            Allowed.append(NewID)
        return render_template("admin.html",Allowed = Allowed)

@app.route('/Output')
def Output():
    global State
    return str(State) + " :D"

@app.route('/Input/Public/<Input>')
def PublicInput(Input):
    if(CheckIfAllowed("Public")!=-1):
        if(Input=="1"):
            SwitchState(1)
        if(Input=="0"):
            SwitchState(0)
        return str(State) + "   " + str(Input)
    else:
        return "Access Denied"

@app.route('/Input/<Id>/<Input>')
def Input(Id,Input):
    global State
    if(CheckIfAllowed(str(request.remote_addr) + str(Id))!=-1):
        if(Input=="1"):
            SwitchState(1)
        if(Input=="0"):
            SwitchState(0)
        return str(State) + "   " + str(Input)
    else:
        global Requests
        if(CheckIfRequested(str(request.remote_addr) + str(Id))==False):
            Requests.append(str(request.remote_addr) + str(Id))
        return "Access Denied"

@app.route('/Input/<Input>')
def Input2(Input):
    global State
    global Requests
    if(CheckIfAllowed(request.remote_addr)!=-1):
        if(Input=="1"):
            SwitchState(1)
        if(Input=="0"):
            SwitchState(0)
        return str(State) + "   " + str(Input)
    else:
        if(CheckIfRequested(str(request.remote_addr))==False):
            Requests.append(str(request.remote_addr))
        return "Access Denied"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=80)

