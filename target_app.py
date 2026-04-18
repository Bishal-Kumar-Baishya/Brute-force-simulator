from flask import Flask, request

app = Flask(__name__)

CORRECT_USERNAME = 'light'
CORRECT_PASSWORD = 'lelouch'

@app.route("/login", methods=["POST"])
def login():
    username = request.form['username']
    password = request.form['password']
    if username == CORRECT_USERNAME and password == CORRECT_PASSWORD:
        return "Access granted"
    else:
        return "Invalid credentials"
        

if __name__ == "__main__":
    app.run()