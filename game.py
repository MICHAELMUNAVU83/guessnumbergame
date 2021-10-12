print('Welcome to the Treasure game...\n')

print(' ')
direction =input('Which direction do you want to go?\n left or right \n')
if direction=='right':
    print('Game is over !!')
    
if direction== 'left':
    move = input('Do you want to swim or wait \n')
    if move=='swim':
        print('Game is over')
    else:
        door = input('Three doors are infront of you ..yellow, red and blue..which door do you open?\n') 
        if door=='red':
            print('Game over!!')
        if door== 'blue':
            print('Game Over !')
        if door=='yellow':
            print('You Won!!')           