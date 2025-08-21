
num_processes = int(input("Enter total number of processes: "))

processes = []
for _ in range(num_processes):
    name, at, bt = input("Enter process name, arrival time and burst time (e.g. P1 0 5): ").split()
    processes.append({
        "name": name,
        "arrival_time": int(at),
        "burst_time": int(bt)
    })


processes.sort(key=lambda x: x["arrival_time"])


time = 0
completed = 0
gantt_chart = ""
waiting_times = []
turnaround_times = []

while completed < num_processes:
    
    available = [p for p in processes if p["arrival_time"] <= time and "completed" not in p]

    if not available:
        time += 1
        continue

   
    current_process = min(available, key=lambda x: x["burst_time"])

    
    current_process["start_time"] = time
    current_process["completion_time"] = time + current_process["burst_time"]
    current_process["turnaround_time"] = current_process["completion_time"] - current_process["arrival_time"]
    current_process["waiting_time"] = current_process["turnaround_time"] - current_process["burst_time"]
    current_process["completed"] = True

    
    time = current_process["completion_time"]
    completed += 1
    gantt_chart += f"|{current_process['start_time']} {current_process['name']} {current_process['completion_time']}|"

    waiting_times.append(current_process["waiting_time"])
    turnaround_times.append(current_process["turnaround_time"])


print("\nGantt Chart:")
print(gantt_chart)

print("\nProcess Details:")
print(f"{'Process':<10}{'AT':<5}{'BT':<5}{'CT':<5}{'TAT':<5}{'WT':<5}")
for p in processes:
    print(f"{p['name']:<10}{p['arrival_time']:<5}{p['burst_time']:<5}{p['completion_time']:<5}{p['turnaround_time']:<5}{p['waiting_time']:<5}")

avg_tat = sum(turnaround_times) / num_processes
avg_wt = sum(waiting_times) / num_processes

print(f"\nAverage Turnaround Time: {avg_tat:.2f} ms")
print(f"Average Waiting Time: {avg_wt:.2f} ms")
