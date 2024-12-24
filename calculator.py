import tkinter as tk
from tkinter import ttk
import math

class CalculatorGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")
        self.master.geometry("300x400")
        self.master.resizable(False, False)
        
        # Variables
        self.current = ""
        self.display_var = tk.StringVar()
        self.display_var.set("0")
        
        self.create_widgets()
    
    def create_widgets(self):
        # Display
        display = ttk.Entry(self.master, textvariable=self.display_var, 
                          justify="right", font=('Arial', 20))
        display.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")
        
        # Buttons
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]
        
        # Create and place buttons
        row = 1
        col = 0
        for button in buttons:
            cmd = lambda x=button: self.click(x)
            ttk.Button(self.master, text=button, command=cmd).grid(
                row=row, column=col, padx=2, pady=2, sticky="nsew"
            )
            col += 1
            if col > 3:
                col = 0
                row += 1
        
        # Clear button
        ttk.Button(self.master, text="C", 
                  command=self.clear).grid(row=row, column=0, 
                                         columnspan=4, sticky="nsew")
        
        # Configure grid
        for i in range(5):
            self.master.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.master.grid_columnconfigure(i, weight=1)
    
    def click(self, key):
        if key == '=':
            try:
                result = eval(self.current)
                self.display_var.set(result)
                self.current = str(result)
            except:
                self.display_var.set("Error")
                self.current = ""
        else:
            self.current += key
            self.display_var.set(self.current)
    
    def clear(self):
        self.current = ""
        self.display_var.set("0")

def main():
    root = tk.Tk()
    app = CalculatorGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()