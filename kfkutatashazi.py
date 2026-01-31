"""
kf (kutatás-fejlesztés) feladat: a megoldáshoz némi önálló keresésre is szükség lehet.

Kérjük le az aktuális dátumot és időt.
Egyetlen formázókóddal printeljük ki az alábbi alakban (két sorban, a nyelv mindegy):
Pl.:
July 18 (Fri), 2025
04:07:12 PM


* Szorgalmi:
A lekért dátumhoz adjunk hozzá 10 napot és egy üres sorral elválaszva írjuk ki mindkét dátumot (egyetlen printet használhatunk).
A formázást szervezzük ki függvénybe.
Pl.:
July 18 (Fri), 2025
04:07:12 PM

July 28 (Mon), 2025
04:07:12 PM
"""

from datetime import datetime

now = datetime.now()
print(now.strftime("%B %d (%a), %Y\n%I:%M:%S %p"))