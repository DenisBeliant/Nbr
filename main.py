# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import random

def fillListe(nbr):
    liste = []

    for i in range(nbr):
        liste.append(random.randrange(0, 1000))

    return sorted(liste)

def main():

    nbr = input("Nombre de nombres à générer ?")
    listeNbr = fillListe(int(nbr))

    for i, el in enumerate(listeNbr):
        print(el)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
