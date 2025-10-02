
from flask import Flask, render_template_string, send_file

app = Flask(__name__)

@app.route('/')
def index():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()
    return render_template_string(html)

@app.route('/kursverlauf.png')
def diagramm():
    return send_file('kursverlauf.png', mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
