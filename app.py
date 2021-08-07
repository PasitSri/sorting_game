#!/bin/python3
class game:
    def __init__(self):
        self.board_game = [['A', 'B', 'C', 'D'], ['E' ,'F', 'G', 'H'], ['I', 'J', ' ', 'K']]
        self.blank = [2,2]
        self.play_game()

    def show_board(self):
        for i in self.board_game:
            print(i[0], '|', i[1], '|', i[2], '|', i[3])

    def check_win(self):
        return self.board_game == [['A', 'B', 'C', 'D'], ['E', 'F', 'G', 'H'], ['I', 'J', 'K', ' ']]

    def find_char(self, char):
        for index_row, row in enumerate(self.board_game):
            try:
                index_col = row.index(char)
                return index_row, index_col
            except:
                pass

    def check_swap(self, position):
        row, col = position
        row_b, col_b = self.blank
        if (row+1 == row_b or row-1 == row_b) and (col == col_b):
            return True
        elif (col+1 == col_b or col-1 == col_b) and (row == row_b):
            return True
        else:
            return False

    def swap_char(self, position):
        row, col = position
        row_b, col_b = self.blank
        self.board_game[row_b][col_b] = self.board_game[row][col]
        self.board_game[row][col] = " "
        self.blank = position


    def play_game(self):
        input_class = input_processer()
        while True:
            print('\n')
            self.show_board();
            input_class.input_checker()
            char = input_class.get_char()
            position = self.find_char(char)
            if self.check_swap(position):
                self.swap_char(position)

            if self.check_win():
                print('\n')
                self.show_board();
                print('Your win')
                break



class input_processer:
    def __init__(self):
        self.char = ''
        self.position = [False, False]

    def input_checker(self):
        while True:
            self.char = input("Enter charactor : ")
            if self.char in "ABCDEFGHIJK":
                break
            else:
                print('\n')
                print("Input not valid")
                print('\n')
        return True
    
    def get_char(self):
        return self.char



if __name__ == '__main__':
    game() 
