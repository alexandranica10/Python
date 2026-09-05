import random

print('\n================================')
print('          Py Wizards ')
print('================================\n')

username = input('Enter your wizard name: ')
print(f'\nCool! Welcome to The Py Wizard Game, {username}!')

energy = 60
health = 100
coins = 20
minutes_past_seven = 0
is_awake = False 

print('\nThese are your starting stats:')
print(f'{energy} Energy')
print(f'{coins} Gold Coins')
print(f'{health} Health\n')

print('The sun rises, and your magical alarm clock (a loud, enchanted toad) starts croaking at 7:00 AM.\n')

while is_awake == False and minutes_past_seven < 60:
    print('Do you want to: ')
    print('1) Hit the toad (Snooze)')
    print('2) Get out of bed')

    choice = input('\nChoose between 1 or 2: ')
    if choice == '1':
        print('\n15 minutes pass...')
        minutes_past_seven += 15
        energy += 10
        if minutes_past_seven == 60:
            print('\nThe time is now 08:00 AM, you are late!')
            print('The toad gets angry for hitting snooze too many times')
            print('and bites you!! Your health drops by 10 and your energy drops by 30.')
            energy -= 30
            health -= 10
        else:
            print(f'\nThe time is now 7:{minutes_past_seven} AM. Energy is now {energy}.\n')
    elif choice == '2':
        print('\nYou have some time before you need to leave,')
        print('so you choose to search for some gold coins.')

        print('You think of some places where you can find the gold:')
        print('1) The drawer next to your bed')
        print('2) The fridge')
        print('3) The desk where you do your homework')
        choice = input(f'\nWhere are you looking, {username}? ')

        if choice == '1':
            print('\nThe toad hops over and steals some of your stash! (Coins -5)')
            coins -= 5
        elif choice == '2':
            print('\nNothing here, as expected...')
        else:
            print('\nYou found some loose change! (Coins +10)')
            coins += 10

        is_awake = True 
    else: 
        print('\nInvalid choice. The toad stares at you..')
        print('Please, choose again\n')

print('\nYour current stats are: ')
print(f'{energy} Energy')
print(f'{coins} Gold Coins')
print(f'{health} Health\n')

if minutes_past_seven == 60:
    print('You don\'t have time for breakfast now and must leave immediately for school.\n')
else:
    print(f'{username} decides to stop at the "Old Brooms" tavern before the first class.')
    print('You\'re hungry and need to decide what to eat to fuel your magic for the day!\n')

    print('The tavern keeper knows you and greets you with the menu:')
    print('1) The "Syntax Sizzler" Breakfast (Cost 5 Gold, restores 25 Energy)')
    print('2) A stale piece of "Soggy Pie" (Cost 2 Gold, restores 10 Energy)')
    print('3) Steal an apple (Cost 0 Gold, 50% chance to fail)')
    choice = input(f'\nWelcome back {username}! What can I get you today? ')
    
    if choice == '1' and coins >= 5:
        coins -= 5
        energy += 25
        print(f'\nYou have {coins} gold coins left and your energy is now {energy}!')
    elif choice == '2' and coins >= 2:
        coins -= 2
        energy += 10
        print(f'\nYou have {coins} gold coins left and your energy is now {energy}!')
    elif choice == '3':
        num = random.randint(0, 1)
        if num > 0.5:
            print('\nYou have been caught :( ')
            if coins < 20:
                coins = 0
                print('You don\'t have enough to pay, so he makes you scrub dishes!')
                energy -= 10
                print('Your energy decreases by 10.')
            else: 
                print('The tavern keeper fines you 20 coins!')
                coins -= 20
        else:
            print("\nThe tavern keeper didn't catch you!")
            energy += 5
            print(f'Your energy is now {energy}, after eating that apple you hardly worked for...')
    else:
        print('\nYou don\'t have enough money or made an invalid choice, so you resume your way to school.')

print('\nYour current stats are: ')
print(f'{energy} Energy')
print(f'{coins} Gold Coins')
print(f'{health} Health\n')

print('After the morning events, you find your way to The Py Academy.')
print('You arrive just in time for Herbology class in the Enchanted Garden.')
print('Miss Bonny tells the class that today\'s task is to find at least 5 Glowing Mushrooms.')

mushrooms = 0
total = False 

while mushrooms < 5 and total == False:
    print("\nEveryone is looking around. You see two paths: ")   
    print('1) The Enchanted Forest')
    print('2) The Big Cave\'s entrance')
    choice = input(f'\nWhere do you want to go, {username}? ')
    
    if choice == '1':
        print('\nYay, you found 1 mushroom!')
        mushrooms += 1
        print('But a magical dog followed you and you ran away in fear. (Energy - 2)')
        energy -= 2
    else:
        print('\nOh, nothing here... The walk was not easy though. (Energy - 2)')
        energy -= 2
    print(f'You now have {mushrooms} mushrooms.')

    print('\nYou continue to look. The other students are whispering that')
    print('The Haunted Bush and The Scary Hut have lots of mushrooms.')
    print('1) The Haunted Bush')
    print('2) The Scary Hut')
    choice = input('\nYou check: ')
    
    if choice == '1':
        print("\nYou found 2 mushrooms.")
        print('Oh, no! Something attacked you from the bush! (Health - 5, Energy - 2)')
        health -= 5
        energy -= 2
        mushrooms += 2
    else:
        print('\nNothing here besides some very strange noises.')
        print('Something came out of nowhere and attacked you! (Health - 5, Energy - 2)')
        health -= 5
        energy -= 2
    print(f'You now have {mushrooms} mushrooms.')

    print('\nFor your last location, you can see two landmarks.')
    print('1) The Strange Mountain')
    print('2) The Moldy Tower')
    choice = input(f'\nWhere should you go, {username}? ')
    
    if choice == '1':
        print('\nYou climbed the mountain and found 2 more mushrooms! Good job!')
        print('But the effort was huge. (Energy - 10 )')
        energy -= 10
        mushrooms += 2
    else:
        print('\nYou walked all the way here to find... nothing. (Energy - 3)')
        energy -= 3        

    print(f'\nYou check your bag. You have {mushrooms} mushrooms!')
    if mushrooms < 5:
        print('Unfortunately, you didn\'t complete the assignment.')
        print('You fly back down to the start of the garden to keep searching.')
        print('The extra flying exhausts you. (Energy - 10)')
        energy -= 10
        total = False
    else: 
        print('You fly back to the classroom with your assignment finished!')
        print(f'{username} is crushing it! Miss Bonny congratulates you.')
        print('The time is now 12:00 PM.')
        total = True

print('\nYour current stats are: ')
print(f'{energy} Energy')
print(f'{coins} Gold Coins')
print(f'{health} Health\n')

print('You run to your next course. Mr. Mandy tells you that you will be feeding')
print('a temperamental Griffin named "Bitey" for today\'s Magical Creatures class.')
print('He is giving you multiple options: ')
print('1) Bow deeply and approach slowly')
print('     --> The traditional, safest method.')
print('2) Distract it with a shiny coin')
print(f'     --> {username} tosses a coin and throws the food while distracted. (Coins - 1)')
print('3) Cast a Calming Spell (Energy - 20)')
print('     --> A risky magical move. If you have at least 50 energy,')
print('         the spell will work flawlessly and the professor praises you.')
print('         Else, Bitey will scratch you! (Health - 15)')

choice = input(f'\nWhat do you do, {username}? Choose now: ')
if choice == '1':
    print(f'\nIt takes a lot of focus and sweat, but keeps {username} completely safe! (Energy - 10)')
    energy -= 10
elif choice == '2':
    if coins >= 1:
        print('\nEverything went smoothly! (Coins - 1)')
        coins -= 1
    else:
        print('\nYou don\'t have any coins! You hesitate, and Bitey snaps at you. (Health - 5)')
        health -= 5
else: 
    print('\nThis is a risky move....let\'s see!')
    energy -= 20
    if energy >= 50:
        print('You did a perfect job! The spell worked and the professor congratulated you in front of the class!')
    else:
        print('Ouch! You tried your luck but it didn\'t pay off. You are too tired to cast this spell and Bitey attacks you! (Health - 15)')
        health -= 15

print('\nYour current stats are: ')
print(f'{energy} Energy')
print(f'{coins} Gold Coins')
print(f'{health} Health\n')

print('After a long, exhausting day, you spot "Madame Py\'s Potions".')
print(f'Madame Py recognizes you: "Hello {username}! What would you like today?"')
print('1) Potion of Vigor (Cost 10 Gold Coins, +20 Energy, +5 Health)')
print('2) Healing Liquor (Cost 7 Gold Coins, +5 Energy, +10 Health)')
print('3) Leave: You decide to keep your money for another day.')

choice = input(f'\nWhat do you say, {username}? What should you get? ')
if choice == '1':
    if coins >= 10:
        coins -= 10
        energy += 20
        health += 5
        print('\nYummm, tasty!')
    else:
        print('\nNot enough gold!')
elif choice == '2':
    if coins >= 7:
        coins -= 7
        energy += 5
        health += 10
        print('\nYummy, that was good!')
    else:
        print('\nNot enough gold!')
else:
    print('\nYou thanked Madame Py and left the shop.')

print('\nThe clock strikes 5:00 PM as you arrive home.')
print('Let\'s take a look at how your day went!\n')

print('Your FINAL stats are: ')
print(f'{energy} Energy')
print(f'{coins} Gold Coins')
print(f'{health} Health\n')

if health <= 0 or energy <= 0:
    print('You open the door and immediately collapse onto the floor.')
    print('The day drained you completely.')
    print('\n=============================================')
    print('        GAME OVER ~ Magical Exhaustion...')
    print('=============================================')
elif health >= 60 and energy >= 60:
    print('You sit on your bed, feeling surprisingly great!')
    print('You survived your classes, explored the grounds, and fed a Griffin.')
    print('You read a spellbook before drifting into a deep sleep.')
    print('\n=============================================')
    print('          YOU WIN! ~ Master Wizard!')
    print('=============================================')
else: 
    print('You drag your feet across the floor and flop onto your bed.')
    print('You are covered in dirt and scratches, but you survived.')
    print('\n=============================================')
    print('        GAME OVER ~ Barely Survived...')
    print('=============================================')
