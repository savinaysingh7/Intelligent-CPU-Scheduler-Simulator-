import matplotlib.pyplot as plt

def draw_gantt_chart(processes):
    start_times = []
    durations = []
    labels = []

    time = 0
    for process in processes:
        start_times.append(time)
        durations.append(process['burst'])
        labels.append(f"P{process['id']}")
        time += process['burst']

    plt.barh(labels, durations, left=start_times, color='skyblue')
    plt.xlabel("Time")
    plt.ylabel("Processes")
    plt.title("CPU Scheduling Gantt Chart")
    plt.show()

processes = [{'id': 1, 'burst': 3}, {'id': 2, 'burst': 5}, {'id': 3, 'burst': 2}]
draw_gantt_chart(processes)
