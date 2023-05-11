# Import Libraries
import tkinter as tk
from tkinter import ttk
from Tabs.NetworkTab import NetworkTab
from Tabs.ResourceUsageTab import ResourceUsageTab
from Tabs.ProcessInfoTab import ProcessInfoTab
from Tabs.SystemInfoTab import SystemInfoTab
from Tabs.ChartTab import ChartTab
from Tabs.MemoryUsageTab import MemoryUsageTab


# Main
class Main:
    # Init
    def __init__(self):
        self.root = tk.Tk()
        self.style = ttk.Style()
        self.notebook = ttk.Notebook(self.root, padding=(10, 5))
        self.create_notebook_tabs()
        self.setup_main_window()

    # Methods
    def setup_main_window(self):
        self.root.title("System Monitoring")
        # self.root.iconbitmap('icon.ico')
        self.notebook.pack(fill="both", expand=True)
        self.root.geometry("900x500+300+50")
        self.root.resizable(width=False, height=False)
        self.root.mainloop()

    def create_notebook_tabs(self):
        SystemInfoTab(self.notebook)
        ProcessInfoTab(self.notebook)
        ResourceUsageTab(self.notebook)
        NetworkTab(self.notebook)
        ChartTab(self.notebook)
        MemoryUsageTab(self.notebook)


# App Launching
if __name__ == '__main__':
    Main()
