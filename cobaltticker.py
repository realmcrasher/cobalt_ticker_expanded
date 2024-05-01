import random, os
from asciimatics.screen import Screen
import time
last = ""

def out(screen):
    board = []
    while True:
        while len(board) < 10:
            liner = str(cobalttext())
            board.append(f'{liner.strip()}')
            board.append(f'          ')
        bprin = ''.join(board)
        p = 0
        while len(board[0]) > abs(p):
            screen.print_at(bprin, p, 0)
            # screen.print_at(abs(len(board[0])), 0, 0)
            screen.refresh()
            p = p - 1
            time.sleep(.1)
        board.pop(0)

        

def cobalttext():
    global last
    file = random.choice(os.listdir("./cobaltticker/talks/"))
    while file == last:
        file = random.choice(os.listdir("./cobaltticker/talks/"))
    last = file
    path = f'./cobaltticker/talks/{file}'
    if file == "weather.txt":
        liner = makeweather(path)
    elif file == "fanbase.txt":
        liner = makename(path)
    else:
        liner = noedittext(path)
    
    # print(liner)
    return liner

def makeweather(path):
    with open(path, "r") as file:
        lines = file.readlines()
        liner = random.choice(lines).strip()
    with open("./cobaltticker/weather/weather_events.txt", "r") as file:
        lines = file.readlines()
        liner = f'{liner} {random.choice(lines).strip()}'
    return liner

def makename(path):
    with open(path, "r") as file:
        lines = file.readlines()
        liner = random.choice(lines).strip()
    liner = f'{liner} {gfirst()} {glast()}'
    return liner

def gfirst():
    rngesus = random.random()
    if rngesus > 0.75:
        path = "./cobaltticker/names/flavor"
    elif rngesus > 0.55:
        path = "./cobaltticker/names/flavor"
    elif rngesus > 0.25:
        path = "./cobaltticker/names/softbase"
    else:
        path = "./cobaltticker/names/base"
    with open(path, "r") as file:
        lines = file.readlines()
        word = random.choice(lines).strip()
    return word

def glast():
    rngesus = random.random()
    if rngesus > 0.75:
        path = "./cobaltticker/names/softbase"
    elif rngesus > 0.55:
        path = "./cobaltticker/names/base"
    elif rngesus > 0.25:
        path = "./cobaltticker/names/base"
    else:
        return " "
    with open(path, "r") as file:
        lines = file.readlines()
        word = random.choice(lines).strip()
    return word

def noedittext(path):
    with open(path, "r") as file:
        lines = file.readlines()
        liner = random.choice(lines)
    return liner

Screen.wrapper(out)
# # cobalttext()
# while True:
#     time.sleep(4)
#     print(cobalttext())