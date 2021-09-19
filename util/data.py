from models.models import Show, ShowType, Recording, Completeness, Authorship

recordings = [
    Show(title="Les Miserables", production="25th Anniversary UK Tour", cast={
        "Jean Valjean": "John Owen-Jones",
        "Javert": "Earl Carpenter",
        "Fantine": "Madalena Alberto"
    }, type=ShowType(recording=Recording.VIDEO,
                     completeness=Completeness.FULL,
                     authorship=Authorship.BOOTLEG),
         id=0),
    Show(title="Les Miserables", production="25th Anniversary Concert", cast={
        "Jean Valjean": "Alfie Boe",
        "Javert": "Norm Lewis",
        "Fantine": "Lea Salonga"
    }, type=ShowType(recording=Recording.VIDEO,
                     completeness=Completeness.FULL,
                     authorship=Authorship.PROSHOT),
         id=1),
    Show(title="Elisabeth", production="Original Vienna production", cast={
        "Elisabeth": "Pia Douwes",
        "Death": "Uwe Kroger"
    }, type=ShowType(recording=Recording.AUDIO,
                     completeness=Completeness.HIGHLIGHTS,
                     authorship=Authorship.PROSHOT),
         id=2)
]
