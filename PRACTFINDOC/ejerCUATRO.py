#UNIV. RODRIGO SILVA MAMANI
import tkinter as tk

dibu_estrella = tk.Tk()
dibu_estrella.title("Estrellitas")
dibu = tk.Canvas(dibu_estrella, width=600, height=500)
dibu.pack()


dibu.create_line(100, 25, 100, 175) 
dibu.create_line(0, 100, 200, 100) 
dibu.create_line(50, 50, 150, 150) 
dibu.create_line(50, 150, 150, 50) 

dibu.create_line(200, 225, 200, 375) 
dibu.create_line(100, 300, 300, 300) 
dibu.create_line(150, 250, 250, 350) 
dibu.create_line(150, 350, 250, 250) 

dibu.create_line(400, 125, 400, 275) 
dibu.create_line(300, 200, 500, 200) 
dibu.create_line(350, 150, 450, 250) 
dibu.create_line(350, 250, 450, 150) 

dibu_estrella.mainloop()