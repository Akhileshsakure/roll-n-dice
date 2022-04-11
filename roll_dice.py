import random
import threading
import time
import sys

def rollDice():
    dicer = random.choice(Sample)
    print("Dice rolled {}".format(dicer))

if __name__ == '__main__':

    '''This program rolls n number of dice concurrently by creating n thread instances'''

    rollAgain = 'Y'
    Sample = (1, 2, 3, 4, 5, 6)
    threads = []


    while rollAgain not in ('N', 'n'):
        if rollAgain in ('Y', 'y'):
            # Enter number of dice to be rolled
            no_of_dice = int(input("How many dices do you want to roll : "))
            start = time.perf_counter()
            # for loop to create multiple thread instances
            for _ in range(no_of_dice):
                t = threading.Thread(target=rollDice())
                # starting thread instance
                t.start()
                threads.append(t)

            # for loop to join all child threads with maon thread
            for thread in threads:
                thread.join()

            end = time.perf_counter()
            print(f'Finished in {round(end - start, 2)} second(s)')
            rollAgain = input("Do you want to roll again? (Y or N) : ")
        else:
            rollAgain = input(rollAgain + " is invalid input. \nKindly input either 'Y' or 'N' : ")
