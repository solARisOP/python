import random

def game(comp, you):
    if(comp == you):
        return None
    elif(comp == 's'):
        if you == 'g':
            return True
        elif you == 'w':
            return False        
    elif(comp == 'w'):
        if you == 's':
            return True
        elif you == 'g':
            return False        
    elif(comp == 'g'):
        if you == 'w':
            return True
        elif you == 's':
            return False 

print('computer : snake(s) water(w) gun(g)')
rd = random.randint(1,3)

if rd == 1:
    comp = 's'
elif rd == 2:
    comp = 'w'
elif rd == 3:
    comp = 'g' 

you = input('player : snake(s) water(w) gun(g) : ')

print(f'you chose {you}')
print(f'computer chose {comp}')

a = game(comp, you)

if a == None:
    print('tie')
elif a:
    print('you won')
else:
    print('computer won')        
