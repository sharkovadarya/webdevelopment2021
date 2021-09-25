from util.data import recordings, shows, productions


def find_recordings_by_show_title(title):
    if title not in shows:
        return []
    title = shows[title]
    if title in recordings:
        return [item for sublist in list(recordings[title].values()) for item in sublist]
    return []


def find_recordings_by_show_title_and_production(title, production):
    if title not in shows:
        return []
    title = shows[title]
    print(production)
    print(productions)
    if production not in productions:
        return []
    production = productions[production]
    if title in recordings and production in recordings[title]:
        return recordings[title][production]
    return []
