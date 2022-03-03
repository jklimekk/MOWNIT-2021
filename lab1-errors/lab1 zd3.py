from math import sin, asin

values = [0.1, 0.5, 1.0]

print("Przyblizanie pierwszym czlonem rozwiniecia\n")

for x in values:
    print("Wartosc x: ", x)
    print("Wartosc sin(x): ", sin(x))
    print("Wartosc arcsin(x): ", asin(x))
    print("Blad progresywny: ", x - sin(x))
    print("Blad wsteczny: ", asin(x) - x, "\n")

print("Przyblizanie dwoma pierwszymi czlonami rozwiniecia\n")

for x in values:
    print("Wartosc x: ", x)
    print("Wartosc x-(x^3)/6: ", x - pow(x, 3)/6)
    print("Wartosc sin(x): ", sin(x))
    print("Wartosc arcsin(x-(x^3)/6): ", asin(x - pow(x, 3)/6))
    print("Blad progresywny: ", x - pow(x, 3)/6 - sin(x))
    print("Blad wsteczny: ", asin(x - pow(x, 3)/6) - x, "\n")
