from flask import Flask, render_template, request
from datetime import date, datetime

app = Flask(__name__)

def dagar_kvar(fodelsedatum):
    idag = date.today()
    datum = datetime.strptime(fodelsedatum, "%Y-%m-%d").date()

    nasta_fodelsedag = date(idag.year, datum.month, datum.day)

    if nasta_fodelsedag < idag:
        nasta_fodelsedag = date(idag.year + 1, datum.month, datum.day)

    skillnad = nasta_fodelsedag - idag
    return skillnad.days

@app.route("/")
def start():
    return render_template("index.html")

@app.route("/resultat", methods=["POST"])
def resultat():
    namn = request.form["namn"]
    fodelsedatum = request.form["fodelsedatum"]

    antal_dagar = dagar_kvar(fodelsedatum)

    return render_template("resultat.html", namn=namn, antal_dagar=antal_dagar)

if __name__ == "__main__":
    app.run(debug=True)