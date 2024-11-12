# homerseklet:int = int(input('írd be hány °C van odakint: '))

# if homerseklet <= 0:
#   print('odakint fagy van')

# comment selected lines: Ctrl + K, Ctrl + C
# uncomment selected lines: Ctrl + K, Ctrl + U

# ------------------------------------

# if valasz in ['igen', 'ja', 'yes', 'Igen!', 'IGEN']:
#   print('még sokra viheted az életben!')

# ------------------------------------

# kerdes = 'szeretsz programozni? (y/n) '

# valasz:str = input(kerdes)
# while valasz not in ['y', 'n']:
#   print('hibás input, csak a [y, n] karakterek elfogadottak!')
#   valasz = input(kerdes)

# if valasz == 'y': print('még sokra viheted az életben')

# print('viszlát!')

# n:int = int(input('írj be egy számot: '))

# if n % 2 == 0: print('ez a szám páros')
# else: print('ez a szám páratlan')

# n:int = int(input('írj be egy számot: '))

# if n % 3 == 0: print('ez a szám osztható 3al')
# else: print('ez a szám nem osztható 3al')

# n:int = int(input('írj be egy számot: '))

# if n < 0: print('ez a szám negatív')
# elif (n > 0): print('ez a szám pozitív')
# else: print('ez a szám se nem negatív, se nem pozitív')

# x:int = int(input('x:= '))
# y:int = int(input('y:= '))

# if x < y: print(f'{x} < {y}')
# elif x > y: print(f'{x} > {y}')
# else: print(f'{x} = {y}')

# x:int = int(input('x:= '))

# # if -30 <= x <= 40: <-- pythonban ez 'is' működik:

# if -30 <= x and x <= 40:
#   print(f'az {x} a [-30, 40] intervallumon belül található')
# else:
#   print(f'az {x} a [-30, 40] intervallumon kívül esik')

# pontszam:int = int(input('add meg a dolgozaton elért pontszámot: '))

# if   pontszam <= 42: print('elégtelen')
# elif pontszam <= 57: print('elégséges')
# elif pontszam <= 72: print('közepes')
# elif pontszam <= 87: print('jó')
# else:                print('jeles')

# telepules:str = input('település neve: ')
# lelekszam:int = int(input(f'{telepules} lélekszáma: '))

# if lelekszam <= 0: print("hibás adatbevitel!")
# elif lelekszam < 5000: print(f'{telepules} egy község')
# elif lelekszam < 20000: print(f'{telepules} egy kisváros')
# elif lelekszam < 100000: print(f'{telepules} egy középváros')
# elif lelekszam < 1000000: print(f'{telepules} egy nagyváros')
# else: print(f'{telepules} egy metropolis')

# termek:str = input('mit szeretnél venni?: ')
# egysegar:int = int(input(f'mennyibe kerül egy {termek} (HUF)?:= '))
# mennyiseg:int = int(input(f'hány db {termek}-t szeretnél venni?:= '))
# penz:int = int(input('mennyi pénzed van (HUF)?:= '))

# if mennyiseg * egysegar <= penz:
#   print(f'ki tudod fizetni a(z) {mennyiseg} db {termek}-t')
#   print(f'{penz - (mennyiseg * egysegar)} Ft-od marad!')
# else:
#   print(f'sajnos maximum {penz // egysegar} db {termek}-t tudsz venni')
#   print(f'ebben az esetben {penz - (penz // egysegar * egysegar)} Ft-od maradna')


# 1600 <- igen
# 1900 <- nem
# 1993 <- nem
# 2008 <- igen


ev:int = int(input('adj meg egy évszámot: '))

# if ev % 400 == 0: print(f'{ev} szökőév')
# elif ev % 100 == 0: print(f'{ev} nem szökőév')
# elif ev % 4 == 0: print(f'{ev} szökőév')
# else: print(f'{ev} nem szökőév')

if ev % 400 == 0 or (ev % 4 == 0 and ev % 100 != 0): print(f'{ev} szökőév')
else: print(f'{ev} nem szökőév')


sorszam:int = int(input('add meg a nap sorszamat: '))

match sorszam:
  case 1:
    print(f'a hét {sorszam}. napja a hétfő')
  case 2:
    print(f'a hét {sorszam}. napja a kedd')
  case 3:
    print(f'a hét {sorszam}. napja a szerda')
  case 4:
    print(f'a hét {sorszam}. napja a csütörtök')
  case 5:
    print(f'a hét {sorszam}. napja a péntek')
  case 6:
    print(f'a hét {sorszam}. napja a szombat')
  case 7:
    print(f'a hét {sorszam}. napja a vasárnap')
  case _:
    print(f'hibás adatbevitel')