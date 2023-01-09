
def fuzzificationPrice(harga):
    if harga < 3:
        return {"murah": 1, "terjangkau": 0, "mahal": 0}
    elif harga < 5:
        return {"murah": (5 - harga) / 2, "terjangkau": (harga - 3) / 2, "mahal": 0}
    elif harga < 6:
        return {"murah": 0, "terjangkau": 1, "mahal": 0}
    elif harga < 8:
        return {"murah": 0, "terjangkau": (8 - harga) / 2, "mahal": (harga - 6) / 2}
    else:
        return {"murah": 0, "terjangkau": 0, "mahal": 1}


def fuzzificationQuality(kualitas):
    if kualitas < 30:
        return {"jelek": 1, "biasa": 0, "bagus": 0}
    elif kualitas < 50:
        return {"jelek": (50 - kualitas) / 20, "biasa": (kualitas - 30) / 20, "bagus": 0}
    elif kualitas < 70:
        return {"jelek": 0, "biasa": 1, "bagus": 0}
    elif kualitas < 80:
        return {"jelek": 0, "biasa": (80 - kualitas) / 10, "bagus": (kualitas - 70) / 10}
    else:
        return {"jelek": 0, "biasa": 0, "bagus": 1}
