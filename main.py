from flask import Flask, render_template, request

app = Flask('JobScrapper')

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    return render_template("seacrh.html", keyword=keyword)

app.run(debug=True)