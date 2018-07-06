import os
import json
from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "coffee_secret"

@app.route("/")
def index():
    return render_template("index.html")
print("this works!")

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)