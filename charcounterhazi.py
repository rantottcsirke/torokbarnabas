"""
Kérjünk be a felhasználótól egy szöveget és számoljuk meg hányféle karaktert tartalmaz.
Printeljük is ki ezt a számot.
Pl.:
alma -> 3
(a, l, m)

kellemes -> 5
(k, e, l, m, s)
"""

szoveg = input("Adj meg egy szöveget: ")

szurt_szoveg = ''.join(c for c in szoveg if c.isalnum())

kulonbozo_karakterek = set(szurt_szoveg)

db = len(kulonbozo_karakterek)

print(f"A szöveg {db} féle karaktert tartalmaz (szóköz és írásjelek nélkül).")
print(f"({', '.join(sorted(kulonbozo_karakterek))})")