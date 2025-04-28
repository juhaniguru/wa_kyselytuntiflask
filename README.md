# NÄIN KÄYNNISTÄT PALVELIMEN

Huom! Jos käytät macia, korvaa python -> python3

## LUO VIRTUALENV



python -m venv .venv

Tämä komento suorittaa python modulen nimeltä venv. Sen tarkoitus on luoda virtualenvivronment ja annat parametrillä sille nimeksi .venv

## AKTIVOI VIRTUALENV

windows: .venv\Scripts\activate
mac: source .venv/bin/activate

## ASENNA RIIPPUVUUDET

python -m pip install -r requirements.txt

Tämä komento sourittaa pip-moduulin. Sille annetaan käskyksi asentaa requirements.txt-tiedosoon listatut kaikki riippuvuudet

## LAITA PALVELIN PÄÄLLE

python main.py
