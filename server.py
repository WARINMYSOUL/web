import tkinter as tk
import threading
from PIL import ImageTk, Image
from socket import *


class AXEPapichAXE:
    def __init__(self):
        self.win = tk.Tk()
        self.win.title('AXEpapichAXE')
        self.win.geometry("256x256+150+80")
        self.win.config(bg='#800000')
        self.win.minsize(512, 294)

        self.images = [ImageTk.PhotoImage(Image.open(f"images/axe{i}.jpg")) for i in range(1, 35)]
        self.image_index = 0

        self.frame = None
        self.lab = None

        self.setup_ui()
        self.start_server()

    def setup_ui(self):
        self.frame = tk.Frame(self.win, bg='#800000')
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.lab = tk.Label(self.frame, image=self.images[0])
        self.lab.pack(pady=20)

        self.win.protocol("WM_DELETE_WINDOW", self.finish)

    def change_image(self):
        self.image_index = (self.image_index + 1) % len(self.images)
        self.lab.configure(image=self.images[self.image_index])

    def start_server(self):
        new_thread = threading.Thread(target=self._server_thread)
        new_thread.start()

    def _server_thread(self):
        server = socket(AF_INET, SOCK_STREAM)
        server.bind(("192.168.26.73", 6842))
        server.listen()

        user, addr = server.accept()

        while True:
            data = user.recv(1)
            if not data:
                break
            self.change_image()

    def finish(self):
        self.win.destroy()

    def run(self):
        self.win.mainloop()


if __name__ == "__main__":
    app = AXEPapichAXE()
    app.run()