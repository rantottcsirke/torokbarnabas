"""
Kérdezd meg a felhasználótól, hogy milyen magas a New-York-i Szabadság-szobor.
Ha a válasz 93, írd ki, hogy "Gratulálok, eltaláltad.
Ha a válasz kisebb, mint 93, írd ki, hogy "Nem, ennél kicsit magasabb."
Ha a válasz nagyobb, mint 93, írd ki, hogy "Nem, ennél kicsit alacsonyabb."
A megoldáshoz használjunk while ciklust és mindaddig kérdezzünk rá a magasságra, amíg a felhasználó el nem találja,
vagy ki nem lép az "exit" beírásával.
"""

while True:
    valasz = input("Milyen magas a New York-i Szabadság-szobor? (Írj 'exit'-et a kilépéshez): ")

    if valasz.lower() == "exit":
        print("Kiléptél a programból.")
        break

    if not valasz.isdigit():
        print("Kérlek, számot adj meg!")
        continue

    magassag = int(valasz)

    if magassag == 93:
        print("Gratulálok, eltaláltad!")
        break
    elif magassag < 93:
        print("Nem, ennél kicsit magasabb.")
    else:
        print("Nem, ennél kicsit alacsonyabb.")