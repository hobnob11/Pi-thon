from flask import Flask, render_template

app = Flask(__name__,template_folder="www")

@app.route('/')
def index():
    return render_template("index.html")
@app.route('/Cake')
def Output():
    return "Output goes here"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=8000)