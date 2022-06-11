import tkinter as tk
from tkinter import ttk
import os
import imagehash
from PIL import Image
from threading import Thread

class AsyncCheck(Thread):
    def __init__(self, InputPath):
        super().__init__()
        self.InputPath = InputPath.replace('\\', '/')
        self.result = ''
        self.progress = 0
        self.hash     = []

    def getProgress(self):
        return self.progress

    def getResult(self):
        duplicate = []
        hash = sorted(self.hash, key=lambda x: str(x['hash']))

        i = 1
        while i < len(hash)-1:
            j = 1
            while (i+j < len(hash)) and (hash[i]['hash'] == hash[i+j]['hash']):
                duplicate.append(hash[i+j]['file'])
                j += 1

            i += j

        self.result = '|'.join(duplicate)
        return self.result

    def run(self):
        if not os.path.exists(self.InputPath):
            return None

        inputdir = os.listdir(self.InputPath)
        for i, file in enumerate(inputdir, 1):
            self.progress = i / len(inputdir) * 100
            if file.lower().endswith('.png') or file.lower().endswith('.jpg'):
                self.hash.append(
                    {
                        'file': file,
                        'hash': imagehash.average_hash(Image.open(self.InputPath + '/' + file).convert('RGB'))
                    }
                )

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        # <Window/>
        self.title('Duplicate Finder')
        self.geometry('600x400')
        self.minsize(300, 200)

        # <Grid/>
        self.columnconfigure(0, weight=4)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, minsize=36)
        self.rowconfigure(1, minsize=36)
        self.rowconfigure(2, weight=1)

        # Widgets
        # Input fields
        self.folder_entry = ttk.Entry(self)
        self.folder_entry.grid(column=0, row=0, sticky=tk.EW, padx=8, pady=8)

        # Progressbar
        self.progress = ttk.Progressbar(self, orient=tk.HORIZONTAL, mode = 'determinate')
        self.progress.grid(columnspan=2, row=1, sticky=tk.EW, padx=8, pady=8)

        # Output field
        self.output_entry = ttk.Entry(self)
        self.output_entry.grid(columnspan=2, row=2, sticky=tk.NSEW, padx=8, pady=8)

        # Check button
        self.start = ttk.Button(self, text="Find", command=self.do_check)
        self.start.grid(column=1, row=0, sticky=tk.EW, padx=8, pady=8)

    def do_check(self):
        self.output_entry.delete(0, tk.END)
        
        checkThread = AsyncCheck(self.folder_entry.get())
        checkThread.start()

        self.monitor(checkThread)

    def monitor(self, thread):
        if thread.is_alive():
            self.after(100, lambda: self.monitor(thread))
            self.progress['value'] = thread.getProgress()

            self.output_entry.delete(0, tk.END)
            self.output_entry.insert(0, thread.getResult())
        else:
            self.progress['value'] = 100

            self.output_entry.delete(0, tk.END)
            self.output_entry.insert(0, thread.getResult())

        

if __name__ == "__main__":
    try:
        from ctypes import windll
        windll.shcore.SetProcessDpiAwareness(1)

    finally:
        app = App()
        app.mainloop()
