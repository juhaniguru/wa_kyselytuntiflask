
from flask import Flask, render_template, request, redirect, url_for, jsonify

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


@app.route('/api/v1/users')
def get_users():
    # flaskilla ei ole pakko käyttää html:ää vastausten content-typenä
    # sillä voi lähettää dataa esim. myös json-formaatissa
    # pythonin dict-tietotyyppi sopii jsonin lähetykseen hyvin, koska muoto jsonissa ja dictionaryssa on sama
    """

    {'avain': 'arvo', 'avain2': 1, 'bands': ['Gorgoroth', 'Torture Killer', 'Dimmu Borgir', 'Cradle Of Filth', 'Behemoth', 'Immortal', 'Watain']}

    :return:
    """
    # jsonify-funktio muuttaa http-responsen tyypin application/jsoniksi => content-type: application/json
    # jotta selain ymmärtää vastauksen olevan html:n sijasta jsonia
    return jsonify([
        {'id': 1, 'username': 'Juhani', 'role:': 'normal-user'},
    ])



if __name__ == '__main__':
    # palvelin lähtee päälle osoitteessa http://localhost:6000
    # kun kirjoitat terminaaliin python main.py
    app.run(debug=True, port=5005)
