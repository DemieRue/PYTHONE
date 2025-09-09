import tkinter as tk


bandera = tk.Tk()
bandera.title("BANDERA LA PAZ")

frame = tk.Frame()
frame.pack()


colroj = tk.Frame(frame, bg='red', width=600, height=200)
colroj.pack()


colver = tk.Frame(frame, bg='green', width=600, height=200)
colver.pack()

bandera.mainloop()


