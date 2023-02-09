import random
import numpy as np
import matplotlib.pyplot as plt

BET = ("odd", "even", "black", "red", "1-18", "19-36", "1-12", "13-24", "25-36", "%0", "%1", "%2")

def main():
    MONEY = 100000
    BET_PER_ROUND = 100
    ROULETTE_ROUNDS = 10000
    graphy = np.array([])
    graphx = np.arange(1, ROULETTE_ROUNDS + 1)

    for i in range(ROULETTE_ROUNDS):
        MONEY = MONEY + play(BET_PER_ROUND)
        graphy = np.append(graphy, MONEY)

    plt.title("Money over time (no strategy)")
    plt.xlabel("times played")
    plt.ylabel("money")
    plt.plot(graphx, graphy, color="blue")
    plt.show()

def strat():
    INIT_MONEY = 100000
    BET_PER_ROUND = 100
    ROULETTE_ROUNDS = 10000
    money = INIT_MONEY
    graphy = np.array([])
    graphx = np.arange(1, ROULETTE_ROUNDS + 1)

    for i in range(ROULETTE_ROUNDS):
        if INIT_MONEY - money > 0:
            money = money + play(INIT_MONEY - money)
        else:
            money = money + play(BET_PER_ROUND)
        graphy = np.append(graphy, money)

    plt.title("Money over time (with strategy)")
    plt.xlabel("times played")
    plt.ylabel("money")
    plt.plot(graphx, graphy, color="red")
    plt.show()


def play(bet):
    result = random.randint(0, 36)
    current_bet = random.choice(BET)

    if current_bet == "odd":
        if result % 2 == 1:
            return bet
        else:
            return -bet

    if current_bet == "even":
        if result % 2 == 0:
            return bet
        else:
            return -bet

    if current_bet == "black":
        if result in [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33]:
            return bet
        else:
            return -bet

    if current_bet == "red":
        if result in [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 35, 36]:
            return bet
        else:
            return -bet

    if current_bet == "1-18":
        if 1 <= result <= 18:
            return bet
        else:
            return -bet

    if current_bet == "19-36":
        if 19 <= result <= 36:
            return bet
        else:
            return -bet

    if current_bet == "1-12":
        if 1 <= result <= 12:
            return 2 * bet
        else:
            return -bet

    if current_bet == "13-24":
        if 13 <= result <= 24:
            return 2 * bet
        else:
            return -bet

    if current_bet == "25-36":
        if 25 <= result <= 36:
            return 2 * bet
        else:
            return -bet

    if current_bet == "%0":
        if result % 3 == 0:
            return 2 * bet
        else:
            return -bet

    if current_bet == "%1":
        if result % 3 == 1:
            return 2 * bet
        else:
            return -bet

    if current_bet == "%2":
        if result % 3 == 2:
            return 2 * bet
        else:
            return -bet


main()
strat()
