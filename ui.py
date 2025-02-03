import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("CPU Scheduler Simulator")

ttk.Label(root, text="Process ID").grid(row=0, column=0)
process_id = ttk.Entry(root)
process_id.grid(row=0, column=1)

ttk.Label(root, text="Arrival Time").grid(row=1, column=0)
arrival_time = ttk.Entry(root)
arrival_time.grid(row=1, column=1)

ttk.Label(root, text="Burst Time").grid(row=2, column=0)
burst_time = ttk.Entry(root)
burst_time.grid(row=2, column=1)

ttk.Label(root, text="Algorithm").grid(row=3, column=0)
algorithm = ttk.Combobox(root, values=["FCFS", "SJF", "Round Robin", "Priority"])
algorithm.grid(row=3, column=1)

root.mainloop()
