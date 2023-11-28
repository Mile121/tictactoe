board = [' ' for x in range(10)]

def läggnummer(letter,pos):
    board[pos] = letter

def rutaärledig(pos):
    return board[pos] == ' '

def printBräde(board):
    print('   |   |   ')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |   ')

def ärbrädetfullt(board):
    if board.count(' ') > 1:
        return False
    else:
        return True

def ärvinnare(b,l):
    return ((b[1] == l and b[2] == l and b[3] == l) or
    (b[4] == l and b[5] == l and b[6] == l) or
    (b[7] == l and b[8] == l and b[9] == l) or
    (b[1] == l and b[4] == l and b[7] == l) or
    (b[2] == l and b[5] == l and b[8] == l) or
    (b[3] == l and b[6] == l and b[9] == l) or
    (b[1] == l and b[5] == l and b[9] == l) or
    (b[3] == l and b[5] == l and b[7] == l))

def flyttaspelare():
    run = True
    while run:
        move = input("Snälla välj en position för att välja värde för X mellan 1 till 9\n")
        try:
            move = int(move)
            if move > 0 and move < 10:
                if rutaärledig(move):
                    run = False
                    läggnummer('X' , move)
                else:
                    print('Snälla, den här rutan är upptagen')
            else:
                print('snälla välj ett nummer mellan 1 och 9')

        except:
            print('Snälla skriv ett nummer')

def datorflytta():
    possibleMoves = [x for x , letter in enumerate(board) if letter == ' ' and x != 0  ]
    move = 0

    for let in ['O' , 'X']:
        for i in possibleMoves:
            boardcopy = board[:]
            boardcopy[i] = let
            if ärvinnare(boardcopy, let):
                move = i
                return move

    öppnahörn = []
    for i in possibleMoves:
        if i in [1 , 3 , 7 , 9]:
            öppnahörn.append(i)

    if len(öppnahörn) > 0:
        move = väljRandom(öppnahörn)
        return move

    if 5 in possibleMoves:
        move = 5
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)

    if len(edgesOpen) > 0:
        move = väljRandom(edgesOpen)
        return move

def väljRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]

def main():
    print("Wälkommen till spelet!")
    printBräde(board)

    while not(ärbrädetfullt(board)):
        if not(ärvinnare(board , 'O')):
            flyttaspelare()
            printBräde(board)
        else:
            print("Fölråt du förlora!")
            break

        if not(ärvinnare(board , 'X')):
            move = datorflytta()
            if move == 0:
                print(" ")
            else:
                läggnummer('O' , move)
                print('Datorn placerade ett o på positionen' , move , ':')
                printBräde(board)
        else:
            print("Du vann!")
            break




    if ärbrädetfullt(board):
        print("Det blev oavgjort")

while True:
    x = input("Vill du köra? tryck y för ja eller n för nej (y/n)\n")
    if x.lower() == 'y':
        board = [' ' for x in range(10)]
        print('--------------------')
        main()
    else:
        break
