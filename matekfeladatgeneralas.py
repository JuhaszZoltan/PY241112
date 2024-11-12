from random import randint

for _ in range(10):
    a:int = randint(10, 50)
    b:int = randint(10, 50)
    r:int = int(input(f'{a} + {b} = '))
    if r == a + b: print('helyes!')
    else: print(f'neeeem! :((((, a megoldás: {a+b}')