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
        self.buttons_status[global_index] = self.current_player
        self.all_buttons[global_index].config(background=self.current_player, state='disabled')
        self.update_frames_status(button_index)
        self.check_winner()
        self.current_player = 'blue' if self.current_player == 'red' else 'red'


    def update_frames_status(self, frame_index):
        if self.frames_status[frame_index] != "none":
            for i in range(81):
                if self.buttons_status[i] == 'locked':
                    self.all_buttons[i].config(state='normal', background=self.default_button_color)
                    self.buttons_status[i] = 'unlocked'
            return

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
        # Update local winners
        for i in range(9):
            if self.frames_status[i] == "none":
                self.check_local_winner(i)

        # Check Global Winner
        # Check rows
        for i in range(3):
            if (self.frames_status[3*i] == self.frames_status[3*i + 1] == self.frames_status[3*i + 2] 
                and self.frames_status[3*i] != "none"):
                self.show_winner(self.frames_status[3*i])
                return
        
        # Check columns
        for i in range(3):
            if (self.frames_status[i] == self.frames_status[i + 3] == self.frames_status[i + 6] 
                and self.frames_status[i] != "none"):
                self.show_winner(self.frames_status[i])
                return
        
        # Check diagonals
        if (self.frames_status[0] == self.frames_status[4] == self.frames_status[8] 
            and self.frames_status[0] != "none"):
            self.show_winner(self.frames_status[0])
            return
        if (self.frames_status[2] == self.frames_status[4] == self.frames_status[6]
            and self.frames_status[2] != "none"):
            self.show_winner(self.frames_status[2])
            return
        
        # Check for a draw
        if "unlocked" not in self.buttons_status:
            self.show_winner("draw")

    
    def check_local_winner(self, frame_index):
        #check rows
        for i in range(3):
            if (self.buttons_status[frame_index*9 + 3*i] == self.buttons_status[frame_index*9 + 3*i + 1] == self.buttons_status[frame_index*9 + 3*i + 2] 
                and self.buttons_status[frame_index*9 + 3*i] != 'locked' and self.buttons_status[frame_index*9 + 3*i] != 'unlocked'):
                self.update_won_frame(frame_index, self.current_player)
                return
        
        #check columns
        for i in range(3):
            if (self.buttons_status[frame_index*9 + i] == self.buttons_status[frame_index*9 + i + 3] == self.buttons_status[frame_index*9 + i + 6] 
                and self.buttons_status[frame_index*9 + i] != 'locked' and self.buttons_status[frame_index*9 + i] != 'unlocked'):
                self.update_won_frame(frame_index, self.current_player)
                return
            
        #check diagonals
        if (self.buttons_status[frame_index*9] == self.buttons_status[frame_index*9 + 4] == self.buttons_status[frame_index*9 + 8] 
            and self.buttons_status[frame_index*9] != 'locked' and self.buttons_status[frame_index*9] != 'unlocked'):
            self.update_won_frame(frame_index, self.current_player)
            return
        if (self.buttons_status[frame_index*9 + 2] == self.buttons_status[frame_index*9 + 4] == self.buttons_status[frame_index*9 + 6] 
            and self.buttons_status[frame_index*9 + 2] != 'locked' and self.buttons_status[frame_index*9 + 2] != 'unlocked'):
            self.update_won_frame(frame_index, self.current_player)
            return
    
    def update_won_frame(self, frame_index, winner):
        self.frames_status[frame_index] = winner

        start_index = frame_index * 9
        end_index = start_index + 9

        for i in range(start_index, end_index):
            self.all_buttons[i].config(background=winner, state='disabled')
            self.buttons_status[i] = winner
    
    def show_winner(self, winner):
        if winner == 'draw':
            messagebox.showinfo("Game Over", "It's a draw!")
        else:
            messagebox.showinfo("Game Over", f"{winner} wins!")
        

EnhancedTicTacToe(tk.Tk())
    
