# Importing Libraries
import tkinter as tk
from tkinter import ttk
from Services.SystemInfoService import SystemInfoService


# SystemInfoTab
class SystemInfoTab:
    # Init
    def __init__(self, notebook):
        self.tab1 = ttk.Frame(notebook)
        notebook.add(self.tab1, text="System Info")
        self.create_tab(self.tab1)

    # Method
    @staticmethod
    def create_tab(tab):
        def create_label(label_text, x_position, y_position, text_size=16):
            label = tk.Label(tab,
                             text=label_text,
                             font=("Times New Roman", text_size))
            label.place(x=x_position, y=y_position)

        create_label("System Information:", 50, 10, 40)
        create_label("System name: " + SystemInfoService.get_system(), 50, 100)
        create_label("Node name: " + SystemInfoService.get_node(), 50, 150)
        create_label("System version: " + SystemInfoService.get_version(), 50, 200)
        create_label("Processor name: " + SystemInfoService.get_processor(), 50, 250)
        create_label("Processor cores: " + str(SystemInfoService.get_cpu_count()) + " cores", 50, 300)
        create_label("Memory: " + str(round(SystemInfoService.get_total_virtual_memory() / (1024.0 ** 3))) + " GB",
                     50,
                     350)
