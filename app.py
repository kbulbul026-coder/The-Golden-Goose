from flask import Flask, render_template, send_file

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download')
def download_file():
    path = 'static/file.pdf'
    return send_file(path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
