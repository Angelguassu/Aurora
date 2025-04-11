from flask import Flask, render_template, request, redirect, session
from urllib.parse import urlparse

app = Flask(__name__)

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)
