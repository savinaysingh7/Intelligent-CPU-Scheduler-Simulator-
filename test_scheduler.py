from scheduling import fcfs

def test_fcfs():
    processes = [{'id': 1, 'arrival': 0, 'burst': 5}, {'id': 2, 'arrival': 2, 'burst': 3}]
    print("Testing FCFS:")
    fcfs(processes)

test_fcfs()

from scheduling import sjf

def test_sjf():
    processes = [{'id': 1, 'arrival': 0, 'burst': 6}, {'id': 2, 'arrival': 2, 'burst': 4}, {'id': 3, 'arrival': 4, 'burst': 2}]
    print("Testing SJF:")
    sjf(processes)

test_sjf()

from scheduling import round_robin

def test_round_robin():
    processes = [{'id': 1, 'burst': 5}, {'id': 2, 'burst': 8}]
    print("Testing Round Robin:")
    round_robin(processes, quantum=3)

test_round_robin()

from scheduling import priority_scheduling

def test_priority():
    processes = [{'id': 1, 'arrival': 0, 'burst': 5, 'priority': 2},
                 {'id': 2, 'arrival': 2, 'burst': 3, 'priority': 1}]
    print("Testing Priority Scheduling:")
    priority_scheduling(processes)

test_priority()
