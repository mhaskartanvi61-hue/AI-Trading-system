from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "AI Trading System Running"

@app.route("/auth")
def auth():
    token = request.args.get("request_token")
    return f"Request Token: {token}"

app.run(host="0.0.0.0", port=10000)
