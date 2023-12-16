from flask import Flask, render_template

app = Flask('JobScrapper')

@app.route("/")
def hello():
    return render_template("home.html", name="YoungBeom")

app.run(debug=True)