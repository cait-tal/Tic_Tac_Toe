from tkinter import *
from game import Game

BACKGROUND_COLOR = "#f7e0e8"
class GameUI():

    def __init__(self, game: Game):

        self.window = Tk()
        self.window.title("Tic-Tac-Toe")
        self.window.geometry("880x704-100+40")

        background_image = PhotoImage(file="../images/bg_img.png", width=880, height=704)
        self.game_board_img = PhotoImage(file="../images/game_board.png", width=880, height=704)
        self.canvas = Canvas(width=880, height=704)
        self.bg_image = self.canvas.create_image(440, 352, image=background_image)
        self.start_text = self.canvas.create_text(440,
                                                  280,
                                                  text="Tic-\n Tac-\nToe",
                                                  font=("Comic Sans MS", 80, "bold"),
                                                  width=300,
                                                  fill="#343F56")
        self.canvas.grid(column=0, row=0)

        self.game = game
        # Return list in form of ["first player", "img for player", "img for computer"]
        self.first_person = self.game.who_first()
        self.player_image = PhotoImage(file=self.first_person[1])
        self.computer_image = PhotoImage(file=self.first_person[2])
        start_img = PhotoImage(file="../images/start_button.png")
        start_button = Button(image=start_img, highlightthickness=0, command=self.begin_game, bg=BACKGROUND_COLOR)
        self.start_button_win = self.canvas.create_window(440, 570,
                                                      window=start_button,
                                                      height=126,
                                                      width=200)
        self.board_text = self.canvas.create_text(440,
                                                   50,
                                                   text="You are X's",
                                                   font=("Comic Sans MS", 20, "bold"),
                                                   width=300,
                                                   fill="#343F56",
                                                   state="hidden")
        play_again_img = PhotoImage(file="../images/play_again_btn.png")
        play_again = Button(image=play_again_img, highlightthickness=0, command=self.play_again, bg=BACKGROUND_COLOR)
        self.play_button = self.canvas.create_window(440, 630,
                                                     window=play_again,
                                                     height=126,
                                                     width=200,
                                                     state="hidden")
        # Game Board, initially hidden
        # Game Buttons, initially hidden
        self.button1 = Button(width = 5, height = 4, highlightthickness=0, bg=BACKGROUND_COLOR, command = self.player_turn1,)
        self.button2 = Button(width = 5, height = 4, highlightthickness=0, bg=BACKGROUND_COLOR, command = self.player_turn2,)
        self.button3 = Button(width = 5, height = 4, highlightthickness=0, bg=BACKGROUND_COLOR, command = self.player_turn3,)
        self.button4 = Button(width = 5, height = 4, highlightthickness=0, bg=BACKGROUND_COLOR, command = self.player_turn4,)
        self.button5 = Button(width = 5, height = 4, highlightthickness=0, bg=BACKGROUND_COLOR, command = self.player_turn5,)
        self.button6 = Button(width = 5, height = 4, highlightthickness=0, bg=BACKGROUND_COLOR, command = self.player_turn6,)
        self.button7 = Button(width = 5, height = 4, highlightthickness=0, bg=BACKGROUND_COLOR, command = self.player_turn7,)
        self.button8 = Button(width = 5, height = 4, highlightthickness=0, bg=BACKGROUND_COLOR, command = self.player_turn8,)
        self.button9 = Button(width = 5, height = 4, highlightthickness=0, bg=BACKGROUND_COLOR, command = self.player_turn9,)

        self.button1_win = self.canvas.create_window(270, 150, window=self.button1, state="hidden")
        self.button2_win = self.canvas.create_window(460, 150, window=self.button2, state="hidden")
        self.button3_win = self.canvas.create_window(650, 150, window=self.button3, state="hidden")
        self.button4_win = self.canvas.create_window(270, 310, window=self.button4, state="hidden")
        self.button5_win = self.canvas.create_window(460, 310, window=self.button5, state="hidden")
        self.button6_win = self.canvas.create_window(650, 310, window=self.button6, state="hidden")
        self.button7_win = self.canvas.create_window(270, 470, window=self.button7, state="hidden")
        self.button8_win = self.canvas.create_window(460, 470, window=self.button8, state="hidden")
        self.button9_win = self.canvas.create_window(650, 470, window=self.button9, state="hidden")

        self.winning_line = self.canvas.create_line(1000, 1000, 1000, 1000, width=5, fill="#343F56")
        # List of button objects
        self.window_list = [self.button1_win, self.button2_win, self.button3_win, self.button4_win, self.button5_win, self.button6_win, self.button7_win, self.button8_win, self.button9_win]
        self.button_list = [self.button1, self.button2, self.button3, self.button4, self.button5, self.button6, self.button7, self.button8, self.button9]
        self.window.mainloop()

    def begin_game(self):
        self.canvas.itemconfig(self.bg_image, image=self.game_board_img)
        self.canvas.itemconfig(self.start_text, state="hidden")
        self.canvas.itemconfig(self.start_button_win, state="hidden")
        self.canvas.itemconfig(self.board_text, state="normal")

        for window in self.window_list:
            self.canvas.itemconfig(window, state="normal")
        if self.first_person[0] == "computer":
            self.canvas.itemconfig(self.board_text, text="You are O's")
            first_play = self.game.computer_turn()[0]
            self.button_list[first_play - 1].configure(image=self.computer_image, width=100, height=100,
                                                      state="disabled")

    def player_turn1(self):
        self.button1.configure(image=self.player_image, width=100, height=100, state="disabled")
        next_play = self.game.player_turn(1)
        if next_play != None:
            self.display_winner(next_play)
        else:
            computer = self.game.computer_turn()
            self.button_list[computer[0] - 1].configure(image=self.computer_image, width=100, height=100, state="disabled")
            if computer[1] != None:
                self.display_winner(computer[1])

    def player_turn2(self):
        self.button2.configure(image=self.player_image, width=100, height=100, state="disabled")
        next_play = self.game.player_turn(2)
        if next_play != None:
            self.display_winner(next_play)
        else:
            computer = self.game.computer_turn()
            self.button_list[computer[0] - 1].configure(image=self.computer_image, width=100, height=100,
                                                        state="disabled")
            if computer[1] != None:
                self.display_winner(computer[1])

    def player_turn3(self):
        self.button3.configure(image=self.player_image, width=100, height=100, state="disabled")
        next_play = self.game.player_turn(3)
        if next_play != None:
            self.display_winner(next_play)
        else:
            computer = self.game.computer_turn()
            self.button_list[computer[0] - 1].configure(image=self.computer_image, width=100, height=100,
                                                        state="disabled")
            if computer[1] != None:
                self.display_winner(computer[1])
    def player_turn4(self):
        self.button4.configure(image=self.player_image, width=100, height=100, state="disabled")
        next_play = self.game.player_turn(4)
        if next_play != None:
            self.display_winner(next_play)
        else:
            computer = self.game.computer_turn()
            self.button_list[computer[0] - 1].configure(image=self.computer_image, width=100, height=100,
                                                        state="disabled")
            if computer[1] != None:
                self.display_winner(computer[1])

    def player_turn5(self):
        self.button5.configure(image=self.player_image, width=100, height=100, state="disabled")
        next_play = self.game.player_turn(5)
        if next_play != None:
            self.display_winner(next_play)
        else:
            computer = self.game.computer_turn()
            self.button_list[computer[0] - 1].configure(image=self.computer_image, width=100, height=100,
                                                        state="disabled")
            if computer[1] != None:
                self.display_winner(computer[1])
    def player_turn6(self):
        self.button6.configure(image=self.player_image, width=100, height=100, state="disabled")
        next_play = self.game.player_turn(6)
        if next_play != None:
            self.display_winner(next_play)
        else:
            computer = self.game.computer_turn()
            self.button_list[computer[0] - 1].configure(image=self.computer_image, width=100, height=100,
                                                        state="disabled")
            if computer[1] != None:
                self.display_winner(computer[1])
    def player_turn7(self):
        self.button7.configure(image=self.player_image, width=100, height=100, state="disabled")
        next_play = self.game.player_turn(7)
        if next_play != None:
            self.display_winner(next_play)
        else:
            computer = self.game.computer_turn()
            self.button_list[computer[0] - 1].configure(image=self.computer_image, width=100, height=100,
                                                        state="disabled")
            if computer[1] != None:
                self.display_winner(computer[1])
    def player_turn8(self):
        self.button8.configure(image=self.player_image, width=100, height=100, state="disabled")
        next_play = self.game.player_turn(8)
        if next_play != None:
            self.display_winner(next_play)
        else:
            computer = self.game.computer_turn()
            self.button_list[computer[0] - 1].configure(image=self.computer_image, width=100, height=100,
                                                        state="disabled")
            if computer[1] != None:
                self.display_winner(computer[1])
    def player_turn9(self):
        self.button9.configure(image=self.player_image, width=100, height=100, state="disabled")
        next_play = self.game.player_turn(9)
        if next_play != None:
            self.display_winner(next_play)
        else:
            computer = self.game.computer_turn()
            self.button_list[computer[0] - 1].configure(image=self.computer_image, width=100, height=100, state="disabled")
            if computer[1] != None:
                self.display_winner(computer[1])
            

    def display_winner(self, winner):
        winner = winner
        if winner != None:
            for buttons in self.game.remaining_choices:
                self.button_list[buttons - 1].configure(state="disabled")
            self.canvas.itemconfig(self.play_button, state="normal")
            if winner[0] == "player":
                self.canvas.itemconfig(self.board_text, text="You won!", state="normal")
                self.draw_winning_line(winner[1])
            elif winner[0] == "computer":
                self.canvas.itemconfig(self.board_text, text="You lost  :(", state="normal")
                self.draw_winning_line(winner[1])
            else:
                self.canvas.itemconfig(self.board_text, text="It's a Tie!", state="normal")

    def draw_winning_line(self, winning_combo):
        if winning_combo == {1, 4, 7}:
            self.canvas.coords(self.winning_line, 270, 130, 270, 490)
        elif winning_combo == {1, 2, 3}:
            self.canvas.coords(self.winning_line, 250, 150, 670, 150)
        elif winning_combo == {1, 5, 9}:
            self.canvas.coords(self.winning_line, 250, 130, 690, 490)
        elif winning_combo == {2, 5, 8}:
            self.canvas.coords(self.winning_line, 460, 130, 460, 490)
        elif winning_combo == {3, 6, 9}:
            self.canvas.coords(self.winning_line, 650, 130, 650, 490)
        elif winning_combo == {4, 5, 6}:
            self.canvas.coords(self.winning_line, 250, 310, 670, 310)
        elif winning_combo == {7, 8, 9}:
            self.canvas.coords(self.winning_line, 250, 470, 670, 470)
        else:
            self.canvas.coords(self.winning_line, 650, 150, 270, 470)
    def play_again(self):
        # Reset board and game sets
        for button in self.button_list:
            button.configure(image="", width=5, height=4, state="normal")
        self.canvas.coords(self.winning_line, 1000, 1000, 1000, 1000)
        self.canvas.itemconfig(self.board_text, text="You are X's")
        self.canvas.itemconfig(self.play_button, state="hidden")
        self.game.player_choices = {0}
        self.game.computer_choices = {0}
        self.game.remaining_choices = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.first_person = self.game.who_first()
        self.player_image = PhotoImage(file=self.first_person[1])
        self.computer_image = PhotoImage(file=self.first_person[2])
        self.begin_game()
















