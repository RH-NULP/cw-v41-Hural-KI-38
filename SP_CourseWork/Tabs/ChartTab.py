# Importing Libraries
import tkinter as tk
import matplotlib.pyplot as plt
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from Services.DiskInfoService import DiskInfoService


# ChartTab
class ChartTab:
    # Init
    def __init__(self, notebook):
        self.tab = ttk.Frame(notebook)

        # Add the tab to the notebook
        notebook.add(self.tab, text="Disk Usage")

        # Create a placeholder for the chart
        self.figure = plt.figure(figsize=(5, 5), dpi=100)
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.tab)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

        # Call the method to show the chart initially
        self.show_chart()

    # Method
    def show_chart(self):
        # Get the disk information
        disk_info_list = DiskInfoService.get_disk_info()

        # Create a figure with two subplots
        fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))

        # Create pie charts for each disk
        for i, disk_info in enumerate(disk_info_list):
            labels = ["Used", "Free"]
            values = [disk_info[3], disk_info[2]]

            # Select the appropriate subplot
            ax = axes[i]
            colors = ["#FF0000", "#00FF00"]

            # Create the pie chart
            ax.pie(values,
                   labels=labels,
                   colors=colors,
                   autopct=lambda x: f"{x:.1f}%",
                   startangle=90)
            ax.axis('equal')
            ax.set_title(f"Disk {disk_info[0]} Total Memory: {disk_info[1]} GB")

        # Draw the figure on the canvas
        self.canvas.figure = fig
        self.canvas.draw()
