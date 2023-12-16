from flask import Flask, render_template, request, redirect, send_file
from extractors.indeed import extract_indeed
from extractors.wwr import extract_wwr
from extractors.wanted import extract_wanted
from file import save_to_file

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

@app.route("/export")
def export():
    keyword = request.args.get("keyword")
    if keyword == None:
        return redirect("/")
    if keyword not in db:
        return redirect(f"/search?keyword={keyword}")
    save_to_file(keyword, db[keyword])
    return send_file(f"{keyword}.csv", as_attachment=True)

app.run(debug=True)