from datetime import date
from flask import render_template
from app import app

cards = [
    {
        'name': "Yvette Cauchois",
        'birth': date(1908, 12, 19),
        'death': date(1999, 11, 19),
        'award': "President of the French Society of Physical Chemistry",
        'publication': "Spectrographie des rayons X par transmission d'un faisceau non canalisé à travers un cristal courbé, 1933",
        'contribution': "Cauchois spectrometer, x-ray analysis using a curved crystal",
    },
    {
        'name': "Yvette Cauchois",
        'birth': date(1908, 12, 19),
        'death': date(1999, 11, 19),
        'award': "President of the French Society of Physical Chemistry",
        'publication': "Spectrographie des rayons X par transmission d'un faisceau non canalisé à travers un cristal courbé, 1933",
        'contribution': "Cauchois spectrometer, studied x-rays using a curved crystal",
        'lContribution': "Cauchois studied actinides and developed actinide spectroscopy. The Cauchois spectrometer has allowed scientists to observe x-rays and gamma rays to futher study radiation"
    },
]


@app.route('/')
def index():
    return render_template('index.html', cards = cards) 
