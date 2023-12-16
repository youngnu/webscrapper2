from flask import Flask, render_template, request, redirect
from extractors.indeed import extract_indeed
from extractors.wwr import extract_wwr
from extractors.wanted import extract_wanted


app = Flask('JobScrapper')

db={}

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    if keyword == None:
        return redirect("/")
    if keyword in db:
        jobs = db[keyword]
    else:
        indeed = extract_indeed(keyword)
        wwr = extract_wwr(keyword)
        wanted = extract_wanted(keyword)
        jobs  = indeed + wwr + wanted
        db[keyword] = jobs
    return render_template("seacrh.html", keyword=keyword, jobs = jobs)

app.run(debug=True)