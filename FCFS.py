
num_processes = int(input("Enter total number of processes: "))

processes = []
arrival_times = []
burst_times = []

for i in range(num_processes):
    name, arrival, burst = input(f"Enter process name, arrival time, and burst time (e.g. P1 0 5): ").split()
    processes.append(name)
    arrival_times.append(int(arrival))
    burst_times.append(int(burst))

process_info = []
for i in range(num_processes):
    process_info.append((processes[i], arrival_times[i], burst_times[i]))


process_info.sort(key=lambda x: x[1])

processes, arrival_times, burst_times = [], [], []
for info in process_info:
    processes.append(info[0])
    arrival_times.append(info[1])
    burst_times.append(info[2])

current_time = 0
total_waiting = 0
total_turnaround = 0
gantt_chart = f"|{current_time}|"

waiting_times = []
turnaround_times = []
completion_times = []

for i in range(num_processes):
    if current_time < arrival_times[i]:
        current_time = arrival_times[i]  
        
    waiting = current_time - arrival_times[i]
    turnaround = waiting + burst_times[i]
    completion_time = current_time + burst_times[i]

    waiting_times.append(waiting)
    turnaround_times.append(turnaround)
    completion_times.append(completion_time)

    total_waiting += waiting
    total_turnaround += turnaround

    current_time += burst_times[i]
    gantt_chart += f"{processes[i]}|{current_time}|"


avg_waiting = total_waiting / num_processes
avg_turnaround = total_turnaround / num_processes

print("\n🔷 Gantt Chart:")
print(gantt_chart)

print("\nProcess\tArrival\tBurst\tWaiting\tTurnaround\tCT")
for i in range(num_processes):
    print(f"{processes[i]}\t{arrival_times[i]}\t{burst_times[i]}\t{waiting_times[i]}\t{turnaround_times[i]}\t\t{completion_times[i]}")

print(f"\n📊 Average Waiting Time: {avg_waiting:.2f} ms")
print(f"📊 Average Turnaround Time: {avg_turnaround:.2f} ms")
