# Spelbrädet med 10 positioner (ignorera index 0)
bräde = [' ' for x in range(10)]

# Funktion för att placera en spelares eller datorns symbol på en given position
def placeraSymbol(symbol, position):
    bräde[position] = symbol

# Funktion för att kontrollera om en position på spelplanen är ledig
def ärPlatsLedig(position):
    return bräde[position] == ' '

# Funktion för att skriva ut spelplanen i terminalen
def skrivUtSpelbräde(spelbräde):
    print('   |   |   ')
    print(' ' + spelbräde[1] + ' | ' + spelbräde[2] + ' | ' + spelbräde[3])
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(' ' + spelbräde[4] + ' | ' + spelbräde[5] + ' | ' + spelbräde[6])
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(' ' + spelbräde[7] + ' | ' + spelbräde[8] + ' | ' + spelbräde[9])
    print('   |   |   ')

# Funktion för att kontrollera om brädet är fullt
def ärSpelbrädetFullt(spelbräde):
    if spelbräde.count(' ') > 1:
        return False
    else:
        return True

# Funktion för att kontrollera om en spelare har vunnit
def ärVinnare(spelbräde, symbol):
    # Vinnande kombinationer för tre i rad
    vinnande_kombinationer = [
        # Horisontella
        [1, 2, 3], [4, 5, 6], [7, 8, 9], 
        # Vertikala 
        [1, 4, 7], [2, 5, 8], [3, 6, 9],  
        # Diagonala
        [1, 5, 9], [3, 5, 7]              
    ]
    
# Funktion för spelarens drag
def spelarensDrag():
    kör = True
    while kör:
        drag = input("Vänligen välj en position att placera X mellan 1 och 9\n")
        try:
            drag = int(drag)
            if 0 < drag < 10:
                if ärPlatsLedig(drag):
                    kör = False
                    placeraSymbol('X', drag)
                else:
                    print('Tyvärr, den här platsen är upptagen')
            else:
                print('Ange ett nummer mellan 1 och 9')

        except ValueError:
            print('Vänligen ange ett nummer')

# Funktion för datorns drag
def datornsDrag():
    möjligaDrag = [x for x, symbol in enumerate(bräde) if symbol == ' ' and x != 0]
    drag = 0

    for symbol in ['O', 'X']:
        for i in möjligaDrag:
            kopiaAvSpelbräde = bräde[:]
            kopiaAvSpelbräde[i] = symbol
            if ärVinnare(kopiaAvSpelbräde, symbol):
                drag = i
                return drag

    hörnLediga = []
    for i in möjligaDrag:
        if i in [1, 3, 7, 9]:
            hörnLediga.append(i)

    if len(hörnLediga) > 0:
        drag = slumpmässigtVal(hörnLediga)
        return drag

    if 5 in möjligaDrag:
        drag = 5
        return drag

    kanterLediga = []
    for i in möjligaDrag:
        if i in [2, 4, 6, 8]:
            kanterLediga.append(i)

    if len(kanterLediga) > 0:
        drag = slumpmässigtVal(kanterLediga)
        return drag

# Funktion för slumpmässigt val
def slumpmässigtVal(lista):
    import random
    ln = len(lista)
    r = random.randrange(0, ln)
    return lista[r]

# Huvudfunktionen för att köra spelet
def huvud():
    print("Välkommen till spelet!")
    skrivUtSpelbräde(bräde)

    while not ärSpelbrädetFullt(bräde):
        if not ärVinnare(bräde, 'O'):
            spelarensDrag()
            skrivUtSpelbräde(bräde)
        else:
            print("Bra försök, spela igen!")
            break

        if not ärVinnare(bräde, 'X'):
            drag = datornsDrag()
            if drag == 0:
                print(" ")
            else:
                placeraSymbol('O', drag)
                print('Datorn placerade en O på position', drag, ':')
                skrivUtSpelbräde(bräde)
        else:
            print("Du vann!")
            break

    if ärSpelbrädetFullt(bräde):
        print("Oavgjort!")

# Huvudloop för att spela igen
while True:
    x = input("Vill du spela? Tryck 'y' för ja eller 'n' för nej (y/n)\n")
    if x.lower() == 'y':
        bräde = [' ' for x in range(10)]
        print('--------------------')
        huvud()
    else:
        break