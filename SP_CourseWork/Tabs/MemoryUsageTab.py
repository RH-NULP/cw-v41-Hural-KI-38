# Importing Libraries
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from Services.MemoryUsageService import MemoryUsageService


# MemoryUsageTab
class MemoryUsageTab:
    # Init
    def __init__(self, notebook):
        # Create a frame for the graph
        self.tab = tk.Frame(notebook)
        notebook.add(self.tab, text='Memory Usage')

        # Create a figure and axes for the graph
        self.fig, self.ax = plt.subplots()
        self.ax.set_title('Memory usage')
        self.ax.set_xlabel('Time (s)')
        self.ax.set_ylabel('Memory used (%)')

        # Create a canvas to display the graph in the frame
        self.frame = tk.Frame(self.tab)  # create a new frame attribute
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.frame)
        self.canvas.get_tk_widget().pack(fill='both', expand=True)
        self.frame.pack(fill='both', expand=True)

        # Initialize variables for the graph data
        self.timestamps = []
        self.usage_history = []

        # Schedule the update function to run every second
        self.update_graph()

    # Method
    def update_graph(self):
        # Get the current memory usage percentage
        memory_usage = MemoryUsageService.get_memory_usage_percent()

        # Add the current memory usage percentage to the history
        self.usage_history.append(memory_usage)

        # Add the current timestamp to the list of timestamps
        self.timestamps.append(len(self.timestamps))

        # Clear the previous graph and plot the new one
        self.ax.clear()
        self.ax.set_title('Memory Usage Plot', fontsize=25)
        self.ax.set_xlabel('Time (s)', fontsize=16)
        self.ax.set_ylabel('Memory used (%)', fontsize=16)
        self.ax.plot(self.timestamps, self.usage_history)

        # Update the canvas using blitting
        self.canvas.draw_idle()

        # Schedule the next update
        self.frame.after(1000, self.update_graph)
