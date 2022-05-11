from datetime import date
from flask import render_template
from app import app

cards = [
    {
        'name': "Yvette Cauchois",
        'birth': date(1908, 12, 19),
        'death': date(1999, 11, 19),
        'award': "President of the French Society of Physical Chemistry",
        'publication': ["Spectrographie des rayons X par transmission d'un faisceau non canalisé à travers un cristal courbé, 1933"],
        'contribution': "Cauchois spectrometer, studied x-rays using a curved crystal",
        'lContribution': "Cauchois studied actinides and developed actinide spectroscopy. The Cauchois spectrometer has allowed scientists to observe x-rays and gamma rays to futher study radiation",
        'unknown': None,
        'pic': "YC"
    },
    {
        'name': "Rosalind Franklin",
        'birth': date(1920, 7, 25),
        'death': date(1958, 4, 16),
        'award': None,
        'publication': ["Photo 51 showing double helix, 1952", "Numerous publications studying coal, DNA, and viruses"],
        'contribution': "DNA double helix structure",
        'lContribution': "Franklin was instrumental to the discovery of DNA's double helix structure. Using x-ray crystallography, she was the first to obtain an x-ray diffusion image of DNA showing a possible double helix structure. The discovery of DNA shape formed the foundation for further study into DNA, such as current day investigations into genetic diseases.",
        'unknown': "Her unpublished evidence was used by Francis Crick and Jim Watson, who were credited for the discovery",
        'sUnknown': "Her unpublished evidence was used by Francis Crick and Jim Watson, who were credited for the discovery",
        'pic': "RF"
    },
    {
        'name': "Melissa Franklin",
        'birth': date(1956, 9, 30),
        'death': None,
        'award': "First woman to receive tenure in the physics department at Harvard University",
        'publication': ["Selected Studies of Charmonium Decays, 1982", ],
        'contribution': "Co-discoverer of the top quark",
        'lContribution': "While at Fermilab, a labratory focussed on studying high-energy particle physics, Franklin and her team discovered the top quark. This discovery further developed scientists' understanding of elementary particles.",
        'unknown': "She may not be well known because her area of study regards complex topics that most people are not familiar with and is out of the scope of high school curriculum",
        'sUnknown': "Studies complex topics unfamiliar to most people",
        'pic': "MF"
    },
    {
        'name': "Berta Karlik",
        'birth': date(1904, 1, 24),
        'death': date(1990, 2, 4),
        'award': "First female full University Professor in Austria, Member of the Academy of Sciences",
        'publication': ["An Alpha-Radiation Ascribed to Element 85, 1943, with T.Bernert", "Element 85 in the Natural Disintegration Series, 1944, with T.Bernert"],
        'contribution': "Discovered natural astatine",
        'lContribution': "When observing the radioactive decay of another element, Karlik discovered naturally ocurring astatine (element 85)",
        'unknown': "Living under German occupation in Austria during World War II may have reduced the reach of her discovery. Additionally, as a female scientist, her academic achievements and recognition were often scrutinized",
        'sUnknown': "World events at time of discovery, female scientist",
        'pic': "BK",
    },
    {
        'name': "Luis Walter Alvarez",
        'birth': date(1911, 6, 13),
        'death': date(1988, 9, 1),
        'award': "Inducted to the National Inventors Hall of Fame",
        'publication': ["Adventures of a Physicist, 1987 (autobiography)"],
        'contribution': "Discovering resonance states using a hydrogen bubble chamber",
        'lContribution': "Using a hydrogen bubble chamber capable of taking many recordings of particles, Alvarez observed resonance states. This equipment later led to the discovery of numerous new particles. Alvarez also worked alongside his son, Walter Alvarez, to publish their theory that the extinction of the dinosaurs was the result of an asteroid impacting the earth",
        'unknown': None,
        'pic': "LA"
    },
    {
        'name': "James A. Harris",
        'birth': date(1932, 3, 26),
        'death': date(2000, 12, 12),
        'award': "Honorary Doctorate, Huston-Tillotson College",
        'publication': None,
        'contribution': "Discovery of Rutherfordium and Dubnium",
        'lContribution': "Harris is known for being the first African American to discover a new element. His major contribution was preparing the atomic targets used in these experiments, as they had to be chemically pure to avoid interference from other elements. The discovery of new elements adds to scientists' knowledge of atomic structures",
        'unknown': "Harris faced many racial challenges on his journey. Possible employers frequently assumed that he was applying to be a janitor instead of a chemist. His contributions took place during a time of racial segregation in the United States",
        'sUnknown': "Racial challenges intefered with his career and popularity",
        'pic': "JH"
    },
]


@app.route('/')
def index():
    return render_template('index.html', cards=cards)
