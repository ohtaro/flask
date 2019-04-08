from flask import Flask
from ddtrace import tracer

tracer.configure(
    hostname='10.8.1.26',
    port=8126,
)

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello world'

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=80)
