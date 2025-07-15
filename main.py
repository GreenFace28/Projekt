"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Michal Vlach
email: mvlach@seznam.cz
"""
# text
TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

# pomocné proměnné
cara = "-" * 35
# registrovaní uživatelé
users = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}

# přihlášení
username = input("username: ").lower()
password = input("password: ").lower()
print(cara)
if username in users and password == users.get(username):
    print("Vítej v aplikaci, " + username + "\nMáš 3 texty na analízu. ")
else:
    print("Neregistrovaný uživatel, ukončuji program.")
    quit()
print(cara)

# zadaní čísla textu
zadani_textu = (input("Zadej číslo textu 1 až 3: "))
print(cara)

# kontrola zadaného čísla textu
if not zadani_textu.isdigit():
    print("Nezadal jste číslo, ukončuji program.")
    quit()
zadani_textu = int(zadani_textu)
# kontrola rozsahu zadaného čísla textu
if 1<= zadani_textu <=3:
    text_číslo = TEXTS[zadani_textu - 1]
else:
    print("Text neexistuje")
    quit()

# počet slov
slova = text_číslo.split()
pocet_slov = len(slova)

# počet slov s velkým písmenem
s_velkym_pismenem = 0
for velke_pismeno in slova:
    if velke_pismeno[0].isupper():
        if not velke_pismeno[1].isupper():
            s_velkym_pismenem += 1

# počet slov psané velkými písmeny a malými písmeny
velkymi_pismeny = 0
mala_slova = 0
for slovo in slova:
    if slovo.isupper():
        velkymi_pismeny += 1
    elif slovo.islower():
        mala_slova += 1

# počet čísel
pocet_cisel = 0
suma = 0
for slovo in slova:
    if slovo.isnumeric():
        pocet_cisel += 1
        suma += int(slovo)

# statistika slov
delky_slov = {}
for slovo in slova:
    ciste_slovo = slovo.strip(",.!:'")
    delka = len(ciste_slovo)
    if delka in delky_slov:
        delky_slov[delka] += 1
    else:
        delky_slov[delka] = 1

# výstup programu
print(f"Ve vybraném textu je {pocet_slov} počet slov.")
print(f"Velkým písmenem začíná {s_velkym_pismenem} slov.")
print(f"Počet slov psaných velkými písmeny {velkymi_pismeny}.")
print(f"Počet slov psaných malími písmeny {mala_slova}.")
print(f"Počet čísel {pocet_cisel}.")
print(f"Suma čísel {suma}.")
print(cara)
print("Délka | Výskyt | Počet")
print(cara)
for delka in sorted(delky_slov):
    pocet = delky_slov[delka]
    hvezdy = "*" * pocet
    print(f"{delka:3} | {hvezdy: <17} | {pocet}")