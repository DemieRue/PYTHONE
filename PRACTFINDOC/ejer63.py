import tkinter as tk

class MouseCounter:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("300x200")
        self.root.title("Mouse Counter")

        self.left_clicks = 0
        self.right_clicks = 0
        self.middle_clicks = 0

        self.label_left = tk.Label(self.root, text="Left Clicks: 0")
        self.label_left.pack()

        self.label_right = tk.Label(self.root, text="Right Clicks: 0")
        self.label_right.pack()

        self.label_middle = tk.Label(self.root, text="Middle Clicks: 0")
        self.label_middle.pack()

        self.root.bind("<Button-1>", self.left_click)
        self.root.bind("<Button-2>", self.middle_click)
        self.root.bind("<Button-3>", self.right_click)

    def left_click(self, event):
        self.left_clicks += 1
        self.label_left.config(text=f"Left Clicks: {self.left_clicks}")

    def right_click(self, event):
        self.right_clicks += 1
        self.label_right.config(text=f"Right Clicks: {self.right_clicks}")

    def middle_click(self, event):
        self.middle_clicks += 1
        self.label_middle.config(text=f"Middle Clicks: {self.middle_clicks}")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    counter = MouseCounter()
    counter.run()