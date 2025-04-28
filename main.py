
from flask import Flask, render_template, request, redirect, url_for

# luodaan flask serveri tässä
# annetaan sille nimeksi skriptin nimi __name__-muuttuja on oletuksena python skriptillä ja sen arvo on skriptin nimi
app = Flask(__name__)

# kun flask-serveri on luotu
# siihen voidaan kiinnittää routeja, joita se kuuntelee
@app.route("/")
# index on funktio, joka suoritetaan kun mennään yo. routeen /
# indeksiä sanotaan siksi routehandleriksi
def index():
    return render_template('index.html')



if __name__ == '__main__':
    # palvelin lähtee päälle osoitteessa http://localhost:6000
    # kun kirjoitat terminaaliin python main.py
    app.run(debug=True, port=5005)
