from flask import Flask

app = Flask('JobScrapper')

@app.route("/")
def hello():
    return "<h1>Hello World</h1>"

app.run(debug=True)