import socket
import tkinter as tk
from socket import *


class AXEPapichClientApp:
    def __init__(self):
        self.win = tk.Tk()
        self.win.title('AXEpapich')
        self.win.geometry("500x300+400+300")
        self.win.config(bg='#800000')

        self.client = socket(AF_INET, SOCK_STREAM)
        self.client.connect(("192.168.26.73", 6842))

        self.setup_ui()

    def setup_ui(self):
        btn = tk.Button(self.win, text='AXE', font="Arial 40", width=5, height=2, command=self.click)
        btn.place(relx=0.5, rely=0.5, anchor='center')
        btn.focus()

        self.win.protocol("WM_DELETE_WINDOW", self.finish)

    def click(self):  # отправка серверу однобайтовую команду
        self.client.send(bytes("\00", 'ascii'))

    def finish(self):
        self.win.destroy()
        self.client.close()

    def run(self):
        self.win.mainloop()


if __name__ == "__main__":
    app = AXEPapichClientApp()
    app.run()
