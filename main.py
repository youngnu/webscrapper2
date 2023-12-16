from flask import Flask, render_template, request
from extractors.indeed import extract_indeed
from extractors.wwr import extract_wwr
from extractors.wanted import extract_wanted


app = Flask('JobScrapper')

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    indeed = extract_indeed(keyword)
    wwr = extract_wwr(keyword)
    wanted = extract_wanted(keyword)
    jobs  = indeed + wwr + wanted
    return render_template("seacrh.html", keyword=keyword, jobs = jobs)

app.run(debug=True)