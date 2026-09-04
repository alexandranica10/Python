print('================================\n')
print('          Py Wizzards \n')
print('================================\n')

energy = 100
health = 100
coins = 20
minutes_past_seven = 0
is_awake = False 
answer = 0

print('Inventory&Stats: \n')
print(f'{energy} Energy')
print(f'{coins} Gold Coins')
print(f'{health} Health\n')

print('The sun rises, and your magical alarm clock (a loud, enchanted toad) starts croaking at 7:00 AM.\n')
while is_awake == False and minutes_past_seven < 60:
    print('Do you want to: ')
    print('1) Hit the toad (Snooze)')
    print('2) Get out of bed!')

    choice = int(input('Choose between 1 or 2: '))
    if choice == 1:
        print('\n15 minutes pass...')
        minutes_past_seven += 15
        energy += 10
        print(f'\nThe time is now 7:{minutes_past_seven} AM. Energy is now {energy}.')
    elif choice == 2:
        print('\nYou jump out of bed, ready for the day!')
        is_awake = True 
    else: 
        print('\nInvalid choice. The toad stares at you..')

if minutes_past_seven >= 60:
    print('Oh no! Is 08:00 AM, you are late!!')
    print('The toad bites your finger in anger!')
    energy -= 30
    health -= 10
    print(f'Energy dropped to {energy} and health to {health}')
else:
    print('\nYou have some extra time to search your room for gold!')
    coins += 10
    print(f'\nYou found some coins! Now you have {coins} gold coins!')

print('\nYou arrive at the local tavern before your first class.')
print('\nYou are hungry and you need to decide what to eat to fuel your magic.')

print(f'\nYou have {coins} gold coins.\n')

print('Decide what to get: ')
print('1) The "Syntax Sizzler" Breakfast(Cost 15 Gold, restore 50 Energy)')
print('2) A stale piece of Elven bread(Cost 5 Gold, restores 10 Energy)')
print('3) Steal an apple(Cost 0 Gold). 50 procent chance to fail')

choice = int(input('\nChoose bewteen 1, 2 or 3: '))
if choice == 1:
    coins -= 15
    energy += 50
    print(f'\nYou have {coins} gold coins left and your energy is now {energy}!')
elif choice == 2:
    coins -= 5
    energy += 10
    print(f'\nYou have {coins} gold coins left and your energy is now {energy}!')
else:
    import random
    num = random.randint(0, 1)
    if num > 0.5:
        print('You have been caught :( You are being fined 20 coins.')
        coins -= 10
        print(f'You now have {coins} gold coins.')
    else:
        print("The tavern keeper didn't caught you!")
        energy += 5
        print(f'Your energy is now {energy}')

print('\nYou arrive at the Academy, and the professor tells you')
print('to go to the enchanted garden ')
print('and gather exactly 5 Glowing Mushrooms for a potion.')

print('\nYou are searching the garden.')

mushrooms = 0
total = False 

while mushrooms < 5 and total == False:
    print("\nIt's time for decisions!")   
    print('\n1) Left')
    print('2) Right\n')
    choice = int(input('Choose 1 or 2: \n')) 
    if choice == 1:
        print('\nYaaay you found 1 mushroom.')
        mushrooms += 1
        print(f'You now have {mushrooms} mushrooms')
        energy -= 2
        print(f'\nIs very hot outside, you lost 2 energy and now have {energy}')
    else:
        print('\nOh, nothing here..')
        print(f'\nIs very hot outside, you lost 2 energy and now have {energy}')

    print('\nEveryone is going to the right but you choose to go..')
    print('1) Left')
    print('2) Right\n')
    choice = int(input('Choose 1 or 2: \n'))
    if choice == 1:
        print("\nOh, that's why nobody was here...")
        print(f'You now have {mushrooms} mushrooms')
        energy -= 2
        print(f'\nIs very hot outside, you lost 2 energy and now have {energy}')
    else:
        print('\nEveryone found 2 mushrooms!')
        mushrooms += 2
        print(f'You now have {mushrooms} mushrooms.')
        energy -= 2
        print(f'\nIs very hot outside, you lost 2 energy and now have {energy}')

    print('\nYou are lost now and choose to go to the...')
    print('1) Big Tower')
    print('2) Strange Mountain\n')
    choice = int(input('Choose where you want to go: '))
    if choice == 1:
        print('\1Nothing here, you are still lost now.')
        print(f'You now have {mushrooms} mushrooms')
        energy -= 2
        print(f'\nIs very hot outside, you lost 2 energy and now have {energy}')
        print('\nYou failed to find the mushrooms and decide to trace your steps back to the professor :( )')
        mushrooms = 0;
        
    else:
        print('\nYou climbed the mountain and found 2 more mushrooms!!')
        mushrooms += 2 
        print(f'You now have {mushrooms} mushrooms.')
        energy -= 2
        print(f'\nIt is very hot outside, you lost 2 energy and now have {energy}.')
        
        if mushrooms >= 5:
            print('\nYou succeeded in finding all 5 mushrooms!')
            print('From up here you see where you left off and you take your broom out and go there.')
            total = True 
        else:
            print(f'\nYou check your bag... you have {mushrooms} mushrooms :( Try again!')
            print('You fly back down to the start of the garden to keep searching.')
            mushrooms = 0

print('\nYou finallt return home.')
print(f'\nYou have {energy} energy left')
print(f'\nYou have {coins} gold coins left')
print(f'\nYou have {health} health left')
print('========================================================')
print('\nYou finished the day, but the jorney is not over yet')
print('See you next time!')
print('========================================================')





