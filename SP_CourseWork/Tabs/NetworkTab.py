# Importing Libraries
import tkinter as tk
from tkinter import ttk
from Services.NetworkConnectionsService import NetworkConnectionsService


# NetworkTab
class NetworkTab:
    # Init
    def __init__(self, notebook):
        self.tab = tk.Frame(notebook)

        # create a table to display the network connections
        self.treeview = tk.ttk.Treeview(self.tab, columns=('Protocol', 'Local Address', 'Remote Address', 'Status'))
        self.treeview.heading('#0', text='No.')
        self.treeview.column('#0', width=40, stretch=False)
        self.treeview.heading('Protocol', text='Protocol')
        self.treeview.column('Protocol', width=170, stretch=False)
        self.treeview.heading('Local Address', text='Local Address')
        self.treeview.column('Local Address', width=200, stretch=False)
        self.treeview.heading('Remote Address', text='Remote Address')
        self.treeview.column('Remote Address', width=200, stretch=False)
        self.treeview.heading('Status', text='Status')
        self.treeview.column('Status', width=100, stretch=False)
        self.treeview.pack()

        # create a button to refresh the network connections
        self.refresh_button = tk.Button(self.tab, text='Refresh', command=self.refresh)
        self.refresh_button.pack()

        # display the initial network connections
        self.refresh()

        # add the tab to the notebook
        notebook.add(self.tab, text='Network Connections')

    # Method
    def refresh(self):
        # clear the table
        self.treeview.delete(*self.treeview.get_children())

        # get the network connections
        connection_list = NetworkConnectionsService.get_network_connections()

        # display the network connections in the table
        for i, connection in enumerate(connection_list):
            self.treeview.insert('', tk.END, text=str(i + 1), values=(connection['protocol'],
                                                                      connection['local_address'],
                                                                      connection['remote_address'],
                                                                      connection['status'])
                                 )
