from flask import Flask
from ddtrace import tracer

app = Flask(__name__)

@app.route('/')
def index():
    return 'aiueo'

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=80)
