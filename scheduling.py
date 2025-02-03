def fcfs_scheduling(processes):
    processes.sort(key=lambda x: x['arrival'])
    time = 0
    for p in processes:
        time += p['burst']
        print(f"Process {p['id']} executed at time {time}")

processes = [{'id': 1, 'arrival': 0, 'burst': 5}, {'id': 2, 'arrival': 2, 'burst': 3}]
fcfs_scheduling(processes)
