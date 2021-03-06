#!/usr/bin/env python
# -*- coding: utf-8 -*-
from itertools import count

from typing import List


def convert_to_absolute(number: float) -> float:

    valeur_absolue = number
    if number < 0:
        valeur_absolue *= -1

    return valeur_absolue


def use_prefixes() -> List[str]:
    prefixes, suffixe = 'JKLMNOPQ', 'ack'
    liste_nom = []
    for i in prefixes:
        liste_nom.append(i + suffixe)

    return liste_nom


def prime_integer_summation() -> int:

    nombre = 2
    nbr_premier = []
    while len(nbr_premier) < 100:
        premier = 1
        for i in range(2, nombre):
            if nombre % i == 0:
                premier = 0
                break
        if premier == 1:
            nbr_premier.append(nombre)
        nombre += 1

    return sum(nbr_premier)


def factorial(number: int) -> int:

    somme_factorielle = 1
    for i in range(1, number+1):
        somme_factorielle *= i

    return somme_factorielle


def use_continue() -> None:

    liste = []
    for i in range(1, 11):
        if i == 5:
            continue
        else:
            liste.append(i)

    print(liste)


def verify_ages(groups: List[List[int]]) -> List[bool]:
    return []


def main() -> None:
    number = -4.325
    print(f"La valeur absolue du nombre {number} est {convert_to_absolute(number)}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des 100 premiers nombre premier est : {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()

    groups = [
        [15, 28, 65, 70, 72], [18, 24, 22, 50, 70], [25, 2],
              [20, 22, 23, 24, 18, 75, 51, 49, 100, 18, 20, 20], [70, 50, 26, 28], [75, 50, 18, 25],
              [13, 25, 80, 15], [20, 30, 40, 50, 60], [75, 50, 100, 28]
    ]
    print(f"Les différents groupes sont: {groups}")
    print(f"L'acceptance des groupes est: {verify_ages(groups)}")


if __name__ == '__main__':
    main()
