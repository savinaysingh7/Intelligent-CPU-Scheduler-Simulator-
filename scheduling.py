def fcfs(processes):
    processes.sort(key=lambda x: x['arrival'])  # Sort by Arrival Time
    time = 0
    for p in processes:
        if time < p['arrival']:
            time = p['arrival']
        time += p['burst']
        print(f"Process {p['id']} executed at time {time}")

processes = [{'id': 1, 'arrival': 0, 'burst': 5}, {'id': 2, 'arrival': 2, 'burst': 3}]
fcfs(processes)


def round_robin(processes, quantum):
    queue = processes[:]
    time = 0
    while queue:
        process = queue.pop(0)
        if process['burst'] > quantum:
            time += quantum
            process['burst'] -= quantum
            queue.append(process)
        else:
            time += process['burst']
            process['burst'] = 0
            print(f"Process {process['id']} finished at time {time}")

processes = [{'id': 1, 'burst': 5}, {'id': 2, 'burst': 8}]
round_robin(processes, quantum=3)

