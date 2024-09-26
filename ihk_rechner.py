def ihk_noten_prozent(punkte:int, max_punkte:int):
    if not isinstance(punkte, int):
        raise TypeError("Nur int erlaubt.")
    type = isinstance(punkte, max_punkte)
    valueCheck1 = punkte < max_punkte
    valueCheck2 = punkte < 0
    valueCheck3 = max_punkte < 0
    if type and valueCheck3 and valueCheck1 and valueCheck2:
        res = punkte * 100 / max_punkte
        print(res)
        return res
    if type == False:
        raise TypeError
    else:
        raise ValueError


def ihk_noten_rechner(punkte: int, max_punkte:int):
    res:float = punkte * 100 / max_punkte
    note = ""
    if res >= 92:
        note = "sehr gut"
        return note
    elif 81 <= res <= 91:
        note = "gut"
        return note
    elif 67 <= res <= 90:
        note = "befriedigend"
        return note
    elif 50 <= res <= 66:
        note = "ausreichend"
        return note
    elif res >= 30 and res <= 65:
        note = "mangelhaft"
        return note
    else:
        note = "ungenügend"
        return note