USER = {
    'username': '',
    'password': ''
}

def register(username, password):
    USER['username'] = username
    USER['password'] = password
    print("Sikeres regisztráció!")

def login(username, password):
    if USER['username'] == username and USER['password'] == password:
        print("Sikeres bejelentkezés!")
    else:
        print("Hibás felhasználónév vagy jelszó.")

# Példa futtatás
reg_nev = input("Felhasználónév: ")
reg_jelszo = input("Jelszó: ")
register(reg_nev, reg_jelszo)

login_nev = input("Felhasználónév: ")
login_jelszo = input("Jelszó: ")
login(login_nev, login_jelszo)