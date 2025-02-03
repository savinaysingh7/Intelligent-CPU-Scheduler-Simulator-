import matplotlib.pyplot as plt

processes = ['P1', 'P2', 'P3']
start_times = [0, 3, 7]
durations = [3, 4, 2]

plt.barh(processes, durations, left=start_times, color='skyblue')
plt.xlabel("Time")
plt.ylabel("Processes")
plt.title("CPU Scheduling Gantt Chart")
plt.show()
