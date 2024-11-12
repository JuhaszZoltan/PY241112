from random import randint

gondolt:int = randint(1, 100)

print('gondoltam egy számra [1, 100] között, próbáld meg kitalálni!')

tipp:int = -1
proba:int = 0

while tipp != gondolt:
    tipp:int = int(input('mi a tipped?: '))
    if gondolt < tipp:
        print('nem, ennél kisebb számra gondoltam, próbáld újra!')
    elif gondolt > tipp:
        print('nem, ennél nagyobb számra gondoltam, próbáld újra!')
    proba = proba + 1

print(f'gratulálok, kitaláltad! próbálkozásaid száma: {proba}')