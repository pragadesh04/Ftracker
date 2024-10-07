from flask import Flask, session, render_template, request, url_for, redirect, flash

app = Flask(__name__)

@app.route('/signin')
def log():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

if __name__ == "__main__":
    app.run(debug=True)