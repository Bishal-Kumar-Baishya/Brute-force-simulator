from flask import Flask, request
import logging

app = Flask(__name__)
logging.basicConfig(
    filename="log.txt",
    format="%(asctime)s - %(message)s",
    level=logging.WARNING
)

CORRECT_USERNAME = 'light'
CORRECT_PASSWORD = 'lelouch'
failed_attempts = {}


@app.route("/login", methods=["POST"])
def login():
    username = request.form['username']
    password = request.form['password']
    if username == CORRECT_USERNAME and password == CORRECT_PASSWORD:
        return "Access granted"
    else:
        failed_attempts[request.remote_addr] = failed_attempts.get(request.remote_addr, 0) + 1
        if failed_attempts[request.remote_addr] >= 5:
            return "Account has been locked for security reasons"
        logging.warning(f"Failed login - IP: {request.remote_addr} - Username: {username} - Password: {password}")
        return "Invalid credentials"
        

if __name__ == "__main__":
    app.run()