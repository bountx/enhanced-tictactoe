import tkinter as tk
from tkinter import messagebox

class EnhancedTicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Enhanced tic tac toe")
        self.frames = []
        self.all_buttons = []
        self.frames_status = ["none" for _ in range(9)]
        self.buttons_status = ["unlocked"] * 81
        self.current_player = 'red'
        self.default_button_color = 'lightgray'
        self.locked_button_color = 'gray'
        self.create_grids()
    
    def create_grids(self):
        for i in range(9):
            frame = tk.Frame(self.root, borderwidth=1, relief="solid")
            frame.grid(row=i//3, column=i%3, padx=10, pady=10)
            self.frames.append(frame)
            self.create_buttons(frame, i)
        self.root.mainloop()
    
    def create_buttons(self, frame, frame_index):
        for i in range(9):
            button = tk.Button(frame, text='', width=2, height=2, command=lambda i=i: self.on_button_click(frame_index, i)
                               , background=self.default_button_color)
            button.grid(row=i//3, column=i%3)
            self.all_buttons.append(button)
            button.config()

    def on_button_click(self, frame_index, button_index):
        global_index = frame_index * 9 + button_index
        self.buttons_status[global_index] = 'clicked'
        self.all_buttons[global_index].config(background=self.current_player, state='disabled')
        self.update_frames_status(button_index)
        self.check_winner()
        self.current_player = 'blue' if self.current_player == 'red' else 'red'


    def update_frames_status(self, frame_index):
        # Reset all buttons to disabled unless they belong to the active frame
        for i in range(81):  # Assuming 9x9 grid of buttons
            if self.buttons_status[i] == 'unlocked':
                self.all_buttons[i].config(state='disabled', background=self.locked_button_color)
                self.buttons_status[i] = 'locked'
    
        # Calculate the range for the current active frame
        start_index = frame_index * 9
        end_index = start_index + 9
    
        # Enable all buttons in the current active frame
        for i in range(start_index, end_index):
            if self.buttons_status[i] == 'locked':
                self.all_buttons[i].config(state='normal', background=self.default_button_color)
                self.buttons_status[i] = 'unlocked'



    def check_winner(self):
        for i in range(9):
            if self.frames_status[i] == "none":
                self.check_local_winner(i)
    
    def check_local_winner(self, frame_index):
        #check rows
        for i in range(3):
            if (self.buttons_status[frame_index*9 + 3*i] == self.buttons_status[frame_index*9 + 3*i + 1] == self.buttons_status[frame_index*9 + 3*i + 2] 
                and self.buttons_status[frame_index*9 + 3*i] == 'clicked'):
                self.update_won_frame(frame_index, self.current_player)
                return
        
        #check columns
        for i in range(3):
            if (self.buttons_status[frame_index*9 + i] == self.buttons_status[frame_index*9 + i + 3] == self.buttons_status[frame_index*9 + i + 6] 
                and self.buttons_status[frame_index*9 + i] == 'clicked'):
                self.update_won_frame(frame_index, self.current_player)
                return
            
        #check diagonals
        if (self.buttons_status[frame_index*9] == self.buttons_status[frame_index*9 + 4] == self.buttons_status[frame_index*9 + 8] 
            and self.buttons_status[frame_index*9] == 'clicked'):
            self.update_won_frame(frame_index, self.current_player)
            return
        if (self.buttons_status[frame_index*9 + 2] == self.buttons_status[frame_index*9 + 4] == self.buttons_status[frame_index*9 + 6] 
            and self.buttons_status[frame_index*9 + 2] == 'clicked'):
            self.update_won_frame(frame_index, self.current_player)
            return
    
    def update_won_frame(self, frame_index, winner):
        self.frames_status[frame_index] = winner
        buttons = self.all_buttons[frame_index*9:frame_index*9+9]
        for button in buttons:
            button.config(state='disabled', background=winner)
        

EnhancedTicTacToe(tk.Tk())
    
