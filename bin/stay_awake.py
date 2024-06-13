import time, pyautogui, threading
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

class GUI(tk.Tk):
    def __init__(self):
        super().__init__()

        # Tkinter
        self.title("Stay Awake")
        # self.iconbitmap("images/coffee.ico")
        self.geometry("400x200")

        # main layout for widgets
        main_frame = ttk.Frame(self)
        main_frame.pack()

        # define a grid
        main_frame.columnconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.columnconfigure(2, weight=1)
        main_frame.rowconfigure(0, weight=1)
        main_frame.rowconfigure(1, weight=1)
        main_frame.rowconfigure(2, weight=1)

        # place widgets
        label = ttk.Label(main_frame, text="StayAwake is now running.\nYou can keep it minimized and it will continue running.\nPress Cancel to disable it.").grid(row=0, column=1)
        # convert image To photoimage
        tkimage = ImageTk.PhotoImage(Image.open("images/coffee_100.jpg"))
        image = ttk.Label(main_frame, image=tkimage).grid(row=1, column=1)
        button = ttk.Button(main_frame, text="Cancel", command=self.Close).grid(row=2, column=1)

        # Make X button use close method in order to kill awake process
        self.protocol("WM_DELETE_WINDOW", self.Close)

        self.after(100, self.Start)
        self.mainloop()

    def Start(self):
        thread = threading.Thread(target=self.Awake)
        # makes the Awake thread terminate when the user exits the window
        thread.daemon = True
        thread.start()

    def Awake(self):
        screen_size_x, screen_size_y = pyautogui.size()
        while True:
            pyautogui.press('f15')
            time.sleep(120)

    def Close(self):
        self.destroy()

if __name__ == '__main__':
   GUI()
