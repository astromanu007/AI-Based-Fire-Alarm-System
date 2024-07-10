from flask import Flask, render_template

app = Flask(__name__)

status = "Conditions Normal"

@app.route('/')
def index():
    return render_template('index.html', status=status)

@app.route('/fire_detected')
def fire_detected():
    global status
    status = "Fire Detected!"
    return render_template('index.html', status=status)

@app.route('/conditions_normal')
def conditions_normal():
    global status
    status = "Conditions Normal"
    return render_template('index.html', status=status)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
