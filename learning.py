from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World! <h1>HELLO</h1>"

@app.route("/our_mission")
def our_mission():
    return "<h2>At Greenwood High, we strive to make our students better everyday through continuous learning and support, to make students feel immersed in their subjects and classes</h2>"

@app.route("/admin")
def admin():
    return redirect(url_for("home"))

if __name__  == "__main__":
    app.run()