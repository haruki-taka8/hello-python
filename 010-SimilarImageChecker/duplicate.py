# The GUI portion of this code is based on the rdbende/Sun-Valley-ttk-examples
# License as below

"""
Example script for testing the Sun Valley theme
Author: rdbende
License: GNU GPLv3 license
Source: https://github.com/rdbende/ttk-widget-factory
"""

# Changes to the script
#     - Adding function to list out similar images in a given directory

# Default variables
SEARCH_PATH=''
USE_SUN_VALLEY_THEME=True

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
        self.result = []
        self.progress = 0
        self.hash     = []

    def getProgress(self):
        return self.progress

    def getResult(self):
        self.result = []
        hash = sorted(self.hash, key=lambda x: str(x['hash']))

        x = 1
        lastX = 1

        i = 0
        while i <= len(hash)-1:
            j = 1
            while (i+j <= len(hash)-1) and (hash[i]['hash'] == hash[i+j]['hash']):

                if j == 1:
                    lastX = x
                    self.result.append(('', x, hash[i]['file'], '')) # no need replace because last argument is specified
                    x += 1

                    self.result.append((lastX, x, 0, hash[i]['file'].replace(' ', '\ ')))
                    x += 1

                self.result.append((lastX, x, j, hash[i+j]['file'].replace(' ', '\ ')))
                x += 1
                j += 1
            i += j

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

class App(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self)

        # Make the app responsive
        self.columnconfigure(index=0, weight=1)
        self.rowconfigure(index=0, weight=1)

        # Create widgets :)
        # Create a Frame for input widgets
        self.widgets_frame = ttk.Frame(self)
        self.widgets_frame.grid(
            row=0, column=0, padx=16, pady=16, sticky="nsew"
        )

        self.widgets_frame.columnconfigure(index=0, weight=1)
        self.widgets_frame.columnconfigure(index=1, weight=1)
        self.widgets_frame.rowconfigure(index=2, weight=1)

        # Entry
        self.entry = ttk.Entry(self.widgets_frame)
        self.entry.insert(0, SEARCH_PATH)
        self.entry.grid(row=0, column=0, padx=0, pady=0, sticky="ew")

        # Button
        self.button = ttk.Button(self.widgets_frame, text="Scan", command=self.do_check)
        self.button.grid(row=0, column=1, padx=8, pady=8, sticky="nsew")
        
        # Progressbar
        self.progress = ttk.Progressbar(self.widgets_frame)
        self.progress.grid(row=1, column=0, padx=(0, 8), pady=0, sticky="ew", columnspan=2)

        # Panedwindow
        self.paned = ttk.PanedWindow(self.widgets_frame)
        self.paned.grid(row=2, column=0, pady=8, sticky="nsew", columnspan=2)

        # Pane #1
        self.pane_1 = ttk.Frame(self.paned, padding=0)
        self.paned.add(self.pane_1, weight=1)

        # Scrollbar
        self.scrollbar = ttk.Scrollbar(self.pane_1)
        self.scrollbar.pack(side="right", fill="y")

        # Treeview
        self.treeviewData = []
        self.treeview = ttk.Treeview(
            self.pane_1,
            selectmode="browse",
            yscrollcommand=self.scrollbar.set,
            columns=1,
            height=10,
        )
        self.treeview.pack(expand=True, fill="both")
        self.scrollbar.config(command=self.treeview.yview)

        # Treeview columns
        self.treeview.column("#0", anchor="w")
        self.treeview.column(1, anchor="w")        

    def do_check(self):
        # self.output_entry.delete(0, tk.END)
        
        checkThread = AsyncCheck(self.entry.get())
        checkThread.start()

        self.monitor(checkThread)

    def monitor(self, thread):
        if thread.is_alive():
            self.after(100, lambda: self.monitor(thread))
            self.progress['value'] = thread.getProgress()

            for row in self.treeview.get_children():
                self.treeview.delete(row)
        else:
            self.progress['value'] = 100
            for item in thread.getResult():
                print(item)

            for item in thread.getResult():
                self.treeview.insert(
                    parent=item[0], index="end", iid=item[1], text=item[2], values=item[3]
                )
                if item[0] == "":
                    self.treeview.item(item[1], open=True)  # Open parents

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Similar Image Checker")

    # Set the theme
    if USE_SUN_VALLEY_THEME:
        root.tk.call("source", "sun-valley.tcl")
        root.tk.call("set_theme", "light")

    app = App(root)
    app.pack(fill="both", expand=True)

    # Set a minsize for the window
    root.update()
    root.minsize(root.winfo_width(), root.winfo_height())

    root.mainloop()