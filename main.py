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
separator = "-" * 35
# registrovaní uživatelé
users = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}

# přihlášení
username = input("username: ").lower()
password = input("password: ").lower()
print(separator)
if username in users and password == users.get(username):
    print("Welcome to the app, " + username + f"\nWe have {len(TEXTS)} texts to be analyzed. ") # podle zadání print("Welcome to the app, " + username + "\nWe have 3 texts to be analyzed. ")
else:
    print("unregistered user, terminating the program..")
    quit()
print(separator)

# výpis textů
print("Available texts:")
for i, text in enumerate(TEXTS):
    print(f"{i + 1}: {text[:30]}...")  
print(separator)

# zadaní čísla textu
index_text = (input("Enter the number of the text to analyze: ")) # podle zadání print("Enter a number btw. 1 and 3 to select: ")
print(separator)

# kontrola zadaného čísla textu
if not index_text.isdigit():
    print("This isn't a number, terminating the program..")
    quit()

index_text = int(index_text)
# kontrola rozsahu zadaného čísla textu
if 1 <= index_text <= len(TEXTS):
    select_text = TEXTS[index_text - 1]
else:
    print("Text number is out of range, terminating the program..")
    quit()

# analýza textu
word_count = 0
titlecase = 0
uppercase = 0
lowercase = 0
numeric = 0
sum_numbers = 0
length_words = {}
for word in select_text.split():
    cleaned = word.strip(",.!:'") # odstranění interpunkce a bílých znaků
    if cleaned:
        word_count += 1 # záznam počtu slov

        length = len(cleaned) # zjištění délky slova
        length_words[length] = length_words.get(length, 0) + 1 # záznam délky slova a jeho výskytu

        if cleaned.istitle(): # započítání slov s velkým počátečním písmenem
            titlecase += 1
        elif cleaned.isupper(): # započítání slov psaných velkými písmeny
            uppercase += 1
        elif cleaned.islower(): # započítání slov psaných malými písmeny
            lowercase += 1
        elif cleaned.isdigit(): # započítání čísel a jejich součet
            numeric += 1
            sum_numbers += int(cleaned)


# výstup programu
print(f"There are {word_count} words in the selected text.")
print(f"There are {titlecase} titlecase words.")
print(f"There are {uppercase} uppercase words.")
print(f"There are {lowercase} lowercase words.")
print(f"There are {numeric} numeric strings.")
print(f"The sum of all the numbers {sum_numbers}.")
print(separator)
print("LEN |    OCCURRENCES    | NR.")
print(separator)
for length in sorted(length_words):
    stars = "*" * min(length_words[length], 20) # omezení počtu hvězdiček na 20
    print(f"{length: <3} | {stars: <20} | {length_words[length]}")
