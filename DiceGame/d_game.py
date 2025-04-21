import random as rd
import time
import keyboard as kb


names = []

def slow_text(s, tm: float):
    for _ in s:
        time.sleep(tm)
        print(_, end='', flush=True)

def game():
    global names

    posit = {2: 10, 3: -3, 4: 2, 5: 2, 6: 1,
             7: -3, 8: 1, 9: 2, 10: -2, 11: 1, 12: 1}

    plr_pos = [0, 0]

    print('Alright! getting everything ready', end='')
    slow_text('...', tm=.8)
    print('Done!')

    while plr_pos[0] < 10 or plr_pos[1] < 10:
        for i in range(0, len(names)):
            die1 = rd.randint(1, 6)
            die2 = rd.randint(1, 6)

            print(f"{names[i]}'s Turn: Press SpaceBar to roll dice.")

            kb.wait('SPACE')
            print(f"{names[i]} rolled a {die1 + die2} \n")
            if plr_pos[i] + posit.get(die1+die2) > 0:
                plr_pos[i] += posit.get(die1+die2)

        print(f"{names[0]}'s position: {plr_pos[0]}")
        print(f"{names[1]}'s position: {plr_pos[1]} \n")

        if plr_pos[0] >= 10 or plr_pos[1] >= 10:
            break

    for ps in range(0, 2):
        if plr_pos[ps] >= 10:
            print(f'{names[ps]} Wins! \n')
    cont()

def cont():
    try:
        answer = input('Want to go again? (Type Y or N): ').lower()
        if answer == 'y':
            return game()
        elif answer == 'n':
            print('Cya!')
            time.sleep(.9)
            exit()
        else:
            print('Please type Y or N.')
            return cont()
    except (ValueError, EOFError):
        print('Error occurred; try again.')
        return cont()

def menu():
    greeting = 'Hey there! Welcome to [DICE GAME]! Here are the rules: \n'
    rules = '''(1) Both players will take turns rolling the dice, and each roll will move your position. 
(2) There are 10 positions; whoever gets to the end first wins. \n'''
    rolls = """     2. +10  | 3. -3 | 4. +2 | 5.  +2 | 6.   +1 
     7. -3   | 8. +1 | 9. +2 | 10. -2 | 11.  +1 
     12. +1 \n"""

# tm was .15
    slow_text(greeting, .14)
    slow_text(rules, .14)
    slow_text(rolls, .14)

    try:
        for i in range(2):
            usr = input(f'[Player {i+1}] Enter username: ')
            names.append(usr)

    except EOFError:
        raise Exception('Error occurred. Please try again.')

    game()

menu()
