# Importing Libraries
import tkinter as tk
from tkinter import ttk
from Services.ResourceUsageService import ResourceUsageService


# ResourceUsageTab
class ResourceUsageTab:
    # Init
    def __init__(self, notebook):
        self.x_pos = 200
        self.y_pos = 100
        self.tab3 = ttk.Frame(notebook)
        notebook.add(self.tab3, text="Resource Usage")
        label = tk.Label(self.tab3,
                         text="Resources:",
                         font=("Times New Roman", 30))
        label.place(x=50, y=20)

        # Define x and y positions for the progress bars
        self.cpu_bar = ttk.Progressbar(self.tab3,
                                       orient="horizontal",
                                       length=300,
                                       mode="determinate")
        self.cpu_bar["maximum"] = 100
        self.cpu_bar["value"] = 0
        self.cpu_bar_label = tk.Label(self.tab3,
                                      text=f"CPU Usage: {self.cpu_bar['value']}%",
                                      font=("Times New Roman", 15))
        self.cpu_bar.place(x=self.x_pos, y=self.y_pos)
        self.cpu_bar_label.place(x=self.x_pos, y=self.y_pos+30)

        self.mem_bar = ttk.Progressbar(self.tab3,
                                       orient="horizontal",
                                       length=300,
                                       mode="determinate")
        self.mem_bar["maximum"] = 100
        self.mem_bar["value"] = 0
        self.mem_bar_label = tk.Label(self.tab3,
                                      text=f"Memory Usage: {self.mem_bar['value']}%",
                                      font=("Times New Roman", 15))
        self.mem_bar.place(x=self.x_pos, y=self.y_pos+100)
        self.mem_bar_label.place(x=self.x_pos, y=self.y_pos+130)

        self.disk_bar = ttk.Progressbar(self.tab3,
                                        orient="horizontal",
                                        length=300,
                                        mode="determinate")
        self.disk_bar["maximum"] = 100
        self.disk_bar["value"] = 0
        self.disk_bar_label = tk.Label(self.tab3,
                                       text=f"Disk Usage: {100 - self.disk_bar['value']}%",
                                       font=("Times New Roman", 15))
        self.disk_bar.place(x=self.x_pos, y=self.y_pos+200)
        self.disk_bar_label.place(x=self.x_pos, y=self.y_pos+230)

        self.bytes_sent_label = tk.Label(self.tab3,
                                         text=f"Bytes Sent: 0",
                                         font=("Times New Roman", 15))
        self.bytes_sent_label.place(x=self.x_pos, y=self.y_pos+310)

        self.bytes_recv_label = tk.Label(self.tab3,
                                         text=f"Bytes Received: 0",
                                         font=("Times New Roman", 15))
        self.bytes_recv_label.place(x=self.x_pos + 220, y=self.y_pos+310)

        self.update_progress_bars()

    # Method
    def update_progress_bars(self):
        resource_usage = ResourceUsageService.get_resource_usage()
        self.cpu_bar["value"] = resource_usage["cpu_percent"]
        self.cpu_bar_label.config(text=f"CPU Usage: {resource_usage['cpu_percent']}%")
        self.mem_bar["value"] = resource_usage["mem_percent"]
        self.mem_bar_label.config(text=f"Memory Usage: {resource_usage['mem_percent']}%")
        self.disk_bar["value"] = 100 - resource_usage["disk_percent"]
        self.disk_bar_label.config(text=f"Disk Usage: {100 - resource_usage['disk_percent']}%")
        self.bytes_sent_label.config(text=f"Bytes Sent: {resource_usage['bytes_sent']}")
        self.bytes_recv_label.config(text=f"Bytes Received: {resource_usage['bytes_recv']}")
        self.tab3.after(5000, self.update_progress_bars)
