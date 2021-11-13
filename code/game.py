from random import choice
from time import sleep


class Game:

    def __init__(self):
        self.winning_combos = [{1, 5, 9}, {1, 2, 3}, {1, 4, 7}, {2, 5, 8}, {3, 6, 9}, {4, 5, 6}, {7, 8, 9}, {3, 5, 7}]
        self.player_choices = {0}
        self.computer_choices = {0}
        self.remaining_choices = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def who_first(self):
        first_person = choice(["player", "computer"])
        if first_person == "player":
            return ["player", "../images/x_img.png", "../images/o_img.png"]
        else:
            return ["computer", "../images/o_img.png", "../images/x_img.png"]

    def computer_turn(self):
        sleep(0.4)
        comp_choice = 0
        while comp_choice == 0:
            for win in self.winning_combos:
                if len(win.intersection(self.computer_choices)) == 2:
                    for num in win:
                        if num in self.remaining_choices:
                            comp_choice = num
                            break
                        else:
                            pass
                    break
            if comp_choice != 0:
                break
            for win in self.winning_combos:
                if len(win.intersection(self.player_choices)) == 2:
                    for num in win:
                        if num in self.remaining_choices:
                            comp_choice = num
                            break
                        else:
                            pass
            if comp_choice == 0:
                comp_choice = choice(self.remaining_choices)
        self.computer_choices.add(comp_choice)
        self.remaining_choices.remove(comp_choice)
        return [comp_choice, self.check_if_winner()]

    def player_turn(self, choice):
        self.player_choices.add(choice)
        self.remaining_choices.remove(choice)
        return self.check_if_winner()

    def check_if_winner(self):
        winner = None
        for win in self.winning_combos:
            if win.issubset(self.player_choices):
                winner = ["player", win]
                break
            elif win.issubset(self.computer_choices):
                winner = ["computer", win]
                break
            elif self.remaining_choices == []:
                winner = ["tie"]
            else:
                continue
        return winner

