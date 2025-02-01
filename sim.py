'''
Martingale Roulette Simulation
'''
import os
import collections
import random

class Roulette:
    def __init__(self, _balance = 50.0, _init_bet_amt = 0.2, _stop_at = 100.0, _cut_streak_at = 7):
        # Logging variables
        self.starting_balance = _balance
        self.total_spins = 0
        self.cut_streaks = 0 # number of times we stopped a losing streak early


        # Betting controls
        self.balance = _balance
        self.bet = _init_bet_amt
        self.starting_bet_size = _init_bet_amt
        self.stop_at = _stop_at
        self.cut_losing_streak_at = _cut_streak_at

        # Game variables
        self.colors = ([0] * 18) + ([1] * 18) + [2, 2]
        self.BLACK, self.RED = 0, 1


    def spin_martingale(self, COLOR = 0) -> bool: # 
        losing_streak = 0
        while self.starting_bet_size < self.balance < self.stop_at:
            # start a new spin, reset bet size of current bet is greater than balance
            if self.bet >= self.balance:
                self.bet = self.starting_bet_size
            self.balance -= self.bet

            if random.choice(self.colors) != COLOR:     # LOST the bet
                self.bet = (self.bet * 2) # double the bet size
                losing_streak += 1
                if losing_streak == self.cut_losing_streak_at:
                    self.cut_streaks += 1
                    self.bet = self.starting_bet_size
                    losing_streak = 0
            else:                                       # WON the bet
                self.balance += (self.bet * 2)
                self.bet = self.starting_bet_size
                losing_streak = 0

            self.total_spins += 1

        # save betting results to a file
        self.log_results()

    def log_results(self):
        with open("results.txt", 'a') as file:
            file.write("=============================================\n")
            file.write("Final Game Results\n")
            file.write(f"Ending Balance: ${self.balance}, profit = ${self.balance - self.starting_balance}\n")
            file.write(f"Total spins: {self.total_spins}, Initial Bet Size: {self.starting_bet_size}\n")
            file.write(f"Cut a {self.cut_losing_streak_at}-streak loss {self.cut_streaks} times...\n")
            file.write("=============================================\n\n")

if __name__ == "__main__":
    game = Roulette()
    game.spin_martingale()