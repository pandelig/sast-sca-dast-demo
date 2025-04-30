from flask import Flask, request
import subprocess

app = Flask(__name__)
app.config['SECRET_KEY'] = "verysecretkey123" # Hardcoded secret!

@app.route('/')
def index():
    return "Welcome! Try visiting: `/hello?name=World`, `/execute?cmd=ls -la`, `/admin`"

@app.route('/hello')
def hello():
    name = request.args.get('name', 'Guest')
    return f"Hello, {name}!"

@app.route('/execute')
def execute():
    command = request.args.get('cmd', 'ls -l')
    # Insecure command execution!
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return f"<pre>{result.stdout}</pre><pre>{result.stderr}</pre>"

@app.route('/admin')
def admin():
    return f"Admin area - Secret Key: {app.config['SECRET_KEY']}"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
