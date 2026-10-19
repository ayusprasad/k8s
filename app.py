import os
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    message = ""
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        if name:
            message = f'Hello {name}, welcome to the Kubernetes test application!!!'
    return render_template('index.html', message=message)


@app.get('/health')
def health():
    return {"status": "healthy"}, 200


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    host = os.environ.get("HOST", "0.0.0.0")
    debug = os.environ.get("FLASK_DEBUG") == "1"
    app.run(host=host, port=port, debug=debug)
