import PIL

from PIL import Image

"""
Dieses Problem wurde in Python gelöst.
Folgende Packages wurden verwendet:
- PIL
"""


# Verwendung readMesssage(path) -> String 
def readMessage(path: str):
    # Öffnen des Bildes
    img = Image.open(path)

    # X und Y Koordinaten zur Navigation
    x = 0
    y = 0

    # String für die Nachricht zum speichern
    message = ""

    # Breite und Höhe des Bildes
    width, height = img.size

    # Solange die Schleife läuft, wird die Nachricht gelesen bis die Werte von g und b 0 sind
    while True:
        # Pixel von x und y Koordinaten 
        pixel = img.getpixel((x, y))
        # Hinzufügen des Buchstaben zur Nachricht und ASCII Wert in String umwandeln
        message += str(chr(pixel[0]))
        # Navigation zu den nächsten Koordinaten
        x += pixel[1] % width
        y += pixel[2] % height
        # Wenn x oder y größer als die Breite oder Höhe sind, wird der Wert durch die Breite oder Höhe geteilt so das ein Wert zwischen 0 und der Breite oder Höhe entsteht
        if x >= width:
            x = x % width  
        if y >= height:
            y = y % height
        
        # Abbrechen wenn die Werte von g und b 0 sind
        if pixel[1] == 0 and pixel[2] == 0:
            break
    # Ausgabe der Nachricht und Rückgabe
    return message


if __name__ == '__main__':
    # Pfad zum Bild
    path = "bild07.png"
    print(readMessage(path))


""" 
Antworten:

1:
Hallo Welt

2:
Hallo Gloria

Wie treffen uns am Freitag um 15:00 Uhr vor der Eisdiele am Markplatz.

Alle Liebe,
Juliane

3:
Hallo Juliane,

Super, ich werde da sein! Ich freue mich schon auf den riesen Eisbecher mit Erdbeeren.

Bis bald,
Gloria

4:
Der Jugendwettbewerb Informatik ist ein Programmierwettbewerb für alle, die erste Programmiererfahrungen sammeln und vertiefen möchten. Programmiert wird mit Blockly, einer Bausteinorientierten Programmiersprache. Vorkenntnisse sind nicht nötig. Um sich mit den Aufgaben des Wettbewerbs vertraut zu machen, empfehlen wir unsere Trainingsseite . Er richtet sich an Schülerinnen und Schüler der Jahrgangsstufen 5 - 13, prinzipiell ist aber eine Teilnahme ab Jahrgangsstufe 3 möglich. Der Wettbewerb besteht aus drei Runden. Die ersten beiden Runden erfolgen online. In der 3. Runde werden zwei Aufgaben gestellt, diese gilt es mit eigenen Programmierwerkzeugen zuhause zu bearbeiten.

5:
Der Bundeswettbewerb Informatik richtet sich an Jugendliche bis 21 Jahre, vor dem Studium oder einer Berufstätigkeit. Der Wettbewerb beginnt am 1. September, dauert etwa ein Jahr und besteht aus drei Runden. Dabei können die Aufgaben der 1. Runde ohne größere Informatikkenntnisse gelöst werden; die Aufgaben der 2. Runde sind deutlich schwieriger.

Der Bundeswettbewerb ist fachlich so anspruchsvoll, dass die Gewinner i.d.R. in die Studienstiftung des deutschen Volkes aufgenommen werden. Aus den Besten werden die TeilnehmerInnen für 
die Internationale Informatik-Olympiade ermittelt. Der Bundeswettbewerb ermöglicht den Teilnehmenden, ihr Wissen zu vertiefen und ihre Begabung weiterzuentwickeln. So trägt der Wettbewerb dazu bei, Jugendliche mit besonderem fachlichen Potenzial zu erkennen.


Bild 6 und 7:
Nicht in dieser Datei enthalten, da die Bilder zu groß sind.
Selber ausführen:
- Die Variable "path" in Zeile 51 auf den Pfad des Bildes ändern
"""
