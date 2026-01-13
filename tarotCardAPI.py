import requests, json   # importeer 2 modules
keuze = 0   # maak variabele keuze aan en gelijk aan 0
namen = {}  # maak variabele namen aan en maak er een lege dict van

# blijf de gebruiker om een input vragen totdat de gebruiker 1 of 2 of 3 typt en gebruik de bijhorende url
while True:
    keuze = input("Wil je een kaart kiezen (1) of uit een soort kaarten kiezen (2) of uit 2 random kaarten kiezen (3): ")
    if keuze == int:
        keuze = int(keuze)

    if keuze == "1":
        url = "https://tarotapi.dev/api/v1/cards"
        break
    # blijf de gebruiker om een input vragen totdat de gebruiker major of minor typt
    elif keuze == "2":
        while True:
            soort = input("Welk soort kaart wil je kiezen major of minor: ")
            if soort == "major" or soort == "minor":
                break
            else:
                print("Typ major of minor.")
        url = f"https://tarotapi.dev/api/v1/cards/search?type={soort}"
        break
    
    elif keuze == "3":
        url = "https://tarotapi.dev/api/v1/cards/random?n=2"
        break

    else:
        print("Je moet 1 of 2 of 3 typen")

# zet de data in variabele responseJson en dump de data in een apart bestand genaamd card
responseJson = requests.get(url).json()
with open("card.json", "w") as fp:
    json.dump(responseJson, fp)

# maak een functie aan die 2 variabelen nodig heeft en geef de info over de gekozen kaart als de gebruiker dit vraagt
def infoOverKaart(namen:dict, cardName:str) -> None:
    for info in namen[cardName]:
        print(info)
    while True:
        gevraagdeInfo = input("Welke info wil je weten (STOP om te stoppen): ")
        if gevraagdeInfo.upper() == "STOP":
            break
        elif gevraagdeInfo in namen[cardName]:
            print(namen[cardName][gevraagdeInfo])
        else:
            print("Typ STOP om te stoppen of een woord uit de lijst voor die info.")

# laat de gebruiker een kaart kiezen en vraag of de gebruiker de info wilt en als de gebruiker de info wilt, maak de juiste variabelen aan voor de functie en laat de functie lopen
for kaart in responseJson["cards"]:
    print(kaart["name"])
    namen[kaart["name"]] = kaart
while True:
    cardName = input("geef de naam van de kaart die je wilt: ")
    if cardName in namen:
        while True:
            info = input("Wil je info over deze kaart krijgen(y/n): ")
            if info.lower() == "y":
                infoOverKaart(namen, cardName)
                break
            elif info.lower() == "n":
                break
            else:
                print("Typ y of n")
        break
    else:
        print("Geef de juiste naam in met hoofdletters")