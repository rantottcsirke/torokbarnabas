"""
Kérjünk be a felhasználótól egy szöveget és alakítsuk át a magánhangzókat 0-ra, a többi karaktert (szóközt is) 1-re.
Printeljük ki az eredeti és az átalakított stringet is.
Pl.:
Alma a fa alatt
011010110101011
"""
maganhangzok = 'aáeéiíoóöőuúüű'

szoveg = input("Adj meg egy szöveget: ")

atalakitott = ''
for c in szoveg:
    if c in maganhangzok:
        atalakitott += '0'
    else:
        atalakitott += '1'

print(szoveg)
print(atalakitott)