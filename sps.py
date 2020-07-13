import random

print("WELCOME".center(25, '-'))
print("...you have to choose number of this elements...")
print("1.stone")
print("2.paper")
print("3.scissor")


def again():
    element = {'1': 'stone', '2': 'paper', '3': 'scissor'}
    round = 1
    i, j = 0, 0
    while(round != 4):
        if round == 3:
            print("...Last Round...")
        else:
            print("Round no. :", round)

        user = input("Stone-Paper-Scissor 1-2-3: ")
        com = key, val = random.choice(list(element.items()))
        print("computer choose.. :", com)
        if (user == 1 and com[0] == 2) or (user == 1 and com[0] == 3) or (user == 2 and com[0] == 1) or (user == 3 and com[0] == 2):
            i = i+1
            print("....you win.... you got", i, "point")
        elif user == com[0]:
            print("....draw....")
        else:
            j = j+1
            print("....you lose... computer got", j, "point")
        round = round+1
    if i > j:
        print("..........YOU WIN..........")
    else:
        print("..........YOU LOSE..........")


again()
res = input("if you want to play again.. press Y/N: ")
if res == 'Y' or res == 'y':
    again()
else:
    print("...Thank You..,")
