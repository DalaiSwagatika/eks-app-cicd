from flask import Flask
import requests
app = Flask(__name__)
 
@app.route('/')
def hello():
    try:
        r = requests.get('http://app1-service:5000')
        return f"Hello from App2. Reached App1: {r.text}"
    except:
        return "App1 not reachable"
 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
