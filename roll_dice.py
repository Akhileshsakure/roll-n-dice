import random
import threading
import time
import sys

rollAgain = 'Y'
Sample = (1, 2, 3, 4, 5, 6)
threads = []


# def dice_result(r):
#     if r == 1:
#         print("-------\n|     |\n|  •  |\n|     |\n-------")
#     elif r == 2:
#         print("-------\n| •   |\n|     |\n|   • |\n-------")
#     elif r == 3:
#         print("-------\n|     |\n|• • •|\n|     |\n-------")
#     elif r == 4:
#         print("-------\n| • • |\n|     |\n| • • |\n-------")
#     elif r == 5:
#         print("-------\n| • • |\n|  •  |\n| • • |\n-------")
#     elif r == 6:
#         print("-------\n|•   •|\n|•   •|\n|•   •|\n-------")


def rollDice():
    dicer = random.choice(Sample)
    print("Dice rolled {}".format(dicer))


while rollAgain not in ('N', 'n'):
    if rollAgain in ('Y', 'y'):
        no_of_dice = int(input("How many dices do you want to roll : "))
        start = time.perf_counter()
        for _ in range(no_of_dice):
            t = threading.Thread(target=rollDice())
            t.start()
            threads.append(t)

        for thread in threads:
            thread.join()

        end = time.perf_counter()
        print(f'Finished in {round(end - start, 2)} second(s)')
        rollAgain = input("Do you want to roll again? (Y or N) : ")
    else:
        rollAgain = input(rollAgain + " is invalid input. \nKindly input either 'Y' or 'N' : ")
