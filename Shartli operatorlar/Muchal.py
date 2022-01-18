year = int(input("Yilni kiriting : "))
muchal = ""

if year % 12 == 0:
    muchal = "Maymun"
elif year % 12 == 1:
    muchal = "Xo'roz"
elif year % 12 == 2:
    muchal = "It"
elif year % 12 == 3:
    muchal = "To'ng'iz"
elif year % 12 == 4:
    muchal = "Sichqon"
elif year % 12 == 5:
    muchal = "Hokiz"
elif year % 12 == 6:
    muchal = "Yo'lbars"
elif year % 12 == 7:
    muchal = "Quyon"
elif year % 12 == 8:
    muchal = "Ajdarho"
elif year % 12 == 9:
    muchal = "Ilon"
elif year % 12 == 10:
    muchal = "Ot"
else:
    muchal = "Tog' echkisi"

print(f"{year} - {muchal} yil")