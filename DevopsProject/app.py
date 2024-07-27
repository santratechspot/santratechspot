from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def index():
    ip = requests.get('https://api.ipify.org').text
    return f'Your public IP address is: {ip}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
