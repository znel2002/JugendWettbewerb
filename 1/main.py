"""
Aufgabe J1: Wundertüte
Umgesetzt von Kim Harre

Dieses Problem wurde in Python gelöst.
"""
def main(path: str):
    # Variablen für die Anzahl der Boxen und Spiele    
    boxAmount = 0
    gamesAmount = 0

    # Öffnen der Datei und lesen der Zeilen
    with open(path, "r") as file:
        lines = file.readlines()
        boxAmount = int(lines[0])
        gamesAmount = int(lines[1])
        # Entfernen der ersten beiden Zeilen so dass nur noch die Spiele übrig bleiben
        lines = lines[2:]

    # Liste für die Boxen und Spiele
    boxes = [[]*boxAmount for i in range(boxAmount)]
    games = []
    # Code und Kurzform
    for i in range(len(lines)):

        if lines[i].isspace():
            continue

        x = int(lines[i])

        # for j in range(x):
        #     games.append(f"Type: {i}")


        games += [f"Type: {i+1}"] * x

    #games = [f"Type: {i+1}" for i in range(len(lines)) for j in range(int(lines[i]))] fehlerhaft da die leeren Zeilen nicht beachtet werden
        
    for i in range(len(games)):
        box = i % boxAmount
        boxes[box].append(games[i])

    return boxes


if __name__ == '__main__':
   print( main("wundertuete0.txt"))