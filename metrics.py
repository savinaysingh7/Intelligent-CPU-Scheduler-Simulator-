def calculate_metrics(processes):
    processes.sort(key=lambda x: x['arrival'])  # Sort by Arrival Time
    time = 0
    waiting_time = []
    turnaround_time = []

    for process in processes:
        if time < process['arrival']:
            time = process['arrival']
        waiting_time.append(time - process['arrival'])
        time += process['burst']
        turnaround_time.append(time - process['arrival'])

    avg_waiting_time = sum(waiting_time) / len(processes)
    avg_turnaround_time = sum(turnaround_time) / len(processes)

    print(f"Average Waiting Time: {avg_waiting_time}")
    print(f"Average Turnaround Time: {avg_turnaround_time}")

processes = [{'id': 1, 'arrival': 0, 'burst': 5},
             {'id': 2, 'arrival': 2, 'burst': 3}]
calculate_metrics(processes)
