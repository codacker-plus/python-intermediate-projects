# gui_calculator.py
import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
        """Initialize the GUI calculator."""
        self.root = root
        self.root.title("GUI Calculator")
        
        self.entry = tk.Entry(root, width=20)
        self.entry.grid(row=0, column=0, columnspan=4)
        
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]
        
        row, col = 1, 0
        for button in buttons:
            cmd = lambda x=button: self.click(x)
            tk.Button(root, text=button, width=5, command=cmd).grid(row=row, column=col)
            col += 1
            if col > 3:
                col = 0
                row += 1
        
        tk.Button(root, text='C', width=5, command=self.clear).grid(row=row, column=col)

    def click(self, char):
        """Handle button clicks."""
        if char == '=':
            try:
                result = eval(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except:
                messagebox.showerror("Error", "Invalid expression")
                self.clear()
        else:
            self.entry.insert(tk.END, char)

    def clear(self):
        """Clear the entry field."""
        self.entry.delete(0, tk.END)

def gui_calculator():
    """Main function for GUI calculator."""
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()

if __name__ == "__main__":
    gui_calculator()
