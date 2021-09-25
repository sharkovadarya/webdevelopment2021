from models.models import Show, ShowType, Recording, Completeness, Authorship
from util.data import les_miserables, les_mis_25_uk_tour_production, les_mis_25_concert_production, elisabeth, \
    elisabeth_original_vienna_production

les_mis_25_uk_tour = Show(title=les_miserables, production=les_mis_25_uk_tour_production, cast={
    "Jean Valjean": "John Owen-Jones",
    "Javert": "Earl Carpenter",
    "Fantine": "Madalena Alberto"
}, type=ShowType(recording=Recording.VIDEO,
                 completeness=Completeness.FULL,
                 authorship=Authorship.BOOTLEG),
                          id=0)
les_mis_25_uk_tour_audio = Show(title=les_miserables, production=les_mis_25_uk_tour_production, cast={
    "Jean Valjean": "John Owen-Jones",
    "Javert": "Earl Carpenter",
    "Fantine": "Madalena Alberto"
}, type=ShowType(recording=Recording.AUDIO,
                 completeness=Completeness.FULL,
                 authorship=Authorship.PROSHOT),
                                id=3)
les_mis_25_concert = Show(title=les_miserables, production=les_mis_25_concert_production, cast={
    "Jean Valjean": "Alfie Boe",
    "Javert": "Norm Lewis",
    "Fantine": "Lea Salonga"
}, type=ShowType(recording=Recording.VIDEO,
                 completeness=Completeness.FULL,
                 authorship=Authorship.PROSHOT),
                          id=1)
elisabeth_vienna_original = Show(title=elisabeth, production=elisabeth_original_vienna_production, cast={
    "Elisabeth": "Pia Douwes",
    "Death": "Uwe Kroger"
}, type=ShowType(recording=Recording.AUDIO,
                 completeness=Completeness.HIGHLIGHTS,
                 authorship=Authorship.PROSHOT),
                                 id=2)
tanz_der_vampire_spb = Show(title="Tanz der Vampire", production="Saint Petersburg production", cast={
    "Graf von Krolock": "Ivan Ozhogin",
    "Sarah": "Vera Sveshnikova",
    "Alfred": "Sergey Denisov"
}, type=ShowType(recording=Recording.AUDIO,
                 completeness=Completeness.FULL,
                 authorship=Authorship.BOOTLEG),
                            id=4)