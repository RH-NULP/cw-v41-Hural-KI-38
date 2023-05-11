# Importing Libraries
import threading
from tkinter import ttk
from datetime import datetime
from Services.ProcessInfoService import ProcessInfoService


# ProcessInfoTab
class ProcessInfoTab:
    # Init
    def __init__(self, notebook):
        self.tab2 = ttk.Frame(notebook)
        self.tab2.pack(fill='both', expand=True)

        # Create a treeview widget to display the process information
        columns = ['PID', 'Name', 'Status', 'Memory Used (MB)', 'Create Time']
        self.treeview = ttk.Treeview(self.tab2, columns=columns, show='headings')
        self.treeview.pack(fill='both', expand=True)

        # Add the columns to the treeview
        for col in columns:
            self.treeview.heading(col, text=col)

        # Add the horizontal scrollbar to the treeview
        h_scrollbar = ttk.Scrollbar(self.tab2, orient='horizontal', command=self.treeview.xview)
        h_scrollbar.pack(side='bottom', fill='x')
        self.treeview.configure(xscrollcommand=h_scrollbar.set)

        # Add the process frame to the notebook tab
        notebook.add(self.tab2, text='Process Info')

        self.root = self.tab2.winfo_toplevel()
        self.start_periodic_updates()

    # Methods
    def update_process_table(self):
        # Clear the current contents of the table
        self.treeview.delete(*self.treeview.get_children())

        def get_process_list():
            # Get the latest process information
            process_list = ProcessInfoService.get_process_info()
            return sorted(process_list, key=lambda p: p['create_time'], reverse=True)

        def update_table(process_list):
            # Add the latest process information to the table
            for process_info in process_list:
                pid = process_info['pid']
                name = process_info['name']
                status = process_info['status']
                memory = process_info['memory_info'].rss // 1024 // 1024  # convert to MB
                create_time = datetime.fromtimestamp(process_info['create_time']).strftime('%Y-%m-%d %H:%M:%S')
                self.treeview.insert('', 'end', values=(pid, name, status, memory, create_time))

        def update_table_thread():
            process_list = get_process_list()
            self.treeview.after(0, update_table, process_list)

        # Start the update process in a separate thread
        threading.Thread(target=update_table_thread).start()

    def start_periodic_updates(self):
        self.update_process_table()  # Run once immediately
        self.root.after(5000, self.start_periodic_updates)  # Schedule to run every 5 seconds

