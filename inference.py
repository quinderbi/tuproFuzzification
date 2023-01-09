def inference(fuzzInputPrice, fuzzInputQuality):
    # Inference
    rendah = []
    tinggi = []
    if fuzzInputPrice["murah"] > 0 and fuzzInputQuality["jelek"] > 0:
        rendah.append(min(fuzzInputPrice["murah"], fuzzInputQuality["jelek"]))
    if fuzzInputPrice["murah"] > 0 and fuzzInputQuality["biasa"] > 0:
        tinggi.append(min(fuzzInputPrice["murah"], fuzzInputQuality["biasa"]))
    if fuzzInputPrice["murah"] > 0 and fuzzInputQuality["bagus"] > 0:
        tinggi.append(min(fuzzInputPrice["murah"], fuzzInputQuality["bagus"]))
    if fuzzInputPrice["terjangkau"] > 0 and fuzzInputQuality["jelek"] > 0:
        rendah.append(
            min(fuzzInputPrice["terjangkau"], fuzzInputQuality["jelek"]))
    if fuzzInputPrice["terjangkau"] > 0 and fuzzInputQuality["biasa"] > 0:
        rendah.append(
            min(fuzzInputPrice["terjangkau"], fuzzInputQuality["biasa"]))
    if fuzzInputPrice["terjangkau"] > 0 and fuzzInputQuality["bagus"] > 0:
        tinggi.append(
            min(fuzzInputPrice["terjangkau"], fuzzInputQuality["bagus"]))
    if fuzzInputPrice["mahal"] > 0 and fuzzInputQuality["jelek"] > 0:
        rendah.append(min(fuzzInputPrice["mahal"], fuzzInputQuality["jelek"]))
    if fuzzInputPrice["mahal"] > 0 and fuzzInputQuality["biasa"] > 0:
        rendah.append(min(fuzzInputPrice["mahal"], fuzzInputQuality["biasa"]))
    if fuzzInputPrice["mahal"] > 0 and fuzzInputQuality["bagus"] > 0:
        rendah.append(min(fuzzInputPrice["mahal"], fuzzInputQuality["bagus"]))

    return {"rendah": max(rendah) if len(rendah) > 0 else 0, "tinggi": max(tinggi) if len(tinggi) > 0 else 0}
