def defuzzification(fuzzy_set):
    # inisialisasi
    n = 1  # interval
    sumTop = 0
    sumBottom = 0
    # MENGHITUNG NILAI PADA RENTANG 0 - 50
    for i in range(0, 50, n):
        sumTop += i * fuzzy_set["rendah"]
        sumBottom += fuzzy_set["rendah"]

    # MENGHITUNG NILAI PADA RENTANG 50 - 80
    # # rentang 50-65
    if fuzzy_set["rendah"] < 0.5:
        titikPotong1 = 50 + (fuzzy_set["rendah"])*(80-50)
        for i in range(50, int(titikPotong1), n):
            sumTop += i * fuzzy_set["rendah"]
            sumBottom += fuzzy_set["rendah"]
        for i in range(int(titikPotong1), 65, n):
            sumTop += i * ((i-50)/30)
            sumBottom += ((i-50)/30)
    else:
        titikPotong1 = 50 + (1-fuzzy_set["rendah"])*(80-50)
        for i in range(50, int(titikPotong1), n):
            sumTop += i * fuzzy_set["rendah"]
            sumBottom += fuzzy_set["rendah"]
        for i in range(int(titikPotong1), 65, n):
            sumTop += i * (1-((i-50)/30))
            sumBottom += 1-((i-50)/30)
    # # rentang 50-65
    if fuzzy_set["tinggi"] < 0.5:
        titikPotong2 = 50 + (1-fuzzy_set["tinggi"])*(80-50)
        for i in range(65, int(titikPotong2), n):
            sumTop += i*(1-((i-50)/30))
            sumBottom += 1-((i-50)/30)
        for i in range(int(titikPotong2), 80, n):
            sumTop += i * fuzzy_set["tinggi"]
            sumBottom += fuzzy_set["tinggi"]
    else:
        titikPotong2 = 50 + (fuzzy_set["tinggi"])*(80-50)
        for i in range(65, int(titikPotong2), n):
            sumTop += i * fuzzy_set["tinggi"]
            sumBottom += fuzzy_set["tinggi"]
        for i in range(int(titikPotong2), 80, n):
            sumTop += i * ((i-50)/30)
            sumBottom += ((i-50)/30)

    # MENGHITUNG NILAI PADA RENTANG 0 - 50
    for i in range(80, 100, n):
        sumTop += i * fuzzy_set["tinggi"]
        sumBottom += fuzzy_set["tinggi"]

    # menghasilkan nilai
    return sumTop/sumBottom
