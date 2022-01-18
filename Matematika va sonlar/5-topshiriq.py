import math

son = float(input("Haqiqiy sonni kiriting: "))
if 0 <= son < 1:
    raqam_uzunligi = 3 - len(str(son))
    ilmiy_korinsh = son / pow(10, raqam_uzunligi)
    print(f"Ilmiy ko'rinish -> {ilmiy_korinsh} * 10^{raqam_uzunligi}")
elif -1 < son <= 0:
    raqam_uzunligi = 4 - len(str(son))
    ilmiy_korinsh = son / pow(10, raqam_uzunligi)
    print(f"Ilmiy ko'rinish -> {ilmiy_korinsh} * 10^{raqam_uzunligi}")
elif son//10 <= -1:
    son_butubqismi = math.floor(son)
    raqam_uzunligi = len(str(son_butubqismi))-2
    ilmiy_korinsh = son / pow(10, raqam_uzunligi)
    print(f"Ilmiy ko'rinish -> {ilmiy_korinsh} * 10^{raqam_uzunligi}")
if son//10 >= 1:
    son_butubqismi = math.floor(son)
    raqam_uzunligi = len(str(son_butubqismi)) - 1
    ilmiy_korinsh = son / pow(10, raqam_uzunligi)
    print(f"Ilmiy ko'rinish -> {ilmiy_korinsh} * 10^{raqam_uzunligi}")
