num_process = int(input("Enter the number of processes: "))

process_list = []
arrival_time = []
burst_time = []
priority = []


for i in range(num_process):
    p, at, bt, pr = input(f"Enter process{i+1} (format: Name AT BT Priority): ").split()
    process_list.append(p)
    arrival_time.append(int(at))
    burst_time.append(int(bt))
    priority.append(int(pr))


original_order = list(zip(process_list, arrival_time, burst_time, priority))
original_names = [p[0] for p in original_order]


combined = list(zip(process_list, arrival_time, burst_time, priority))


combined.sort(key=lambda x: (x[1], x[3]))


process_list, arrival_time, burst_time, priority = zip(*combined)

completion_time = [0] * num_process
turnaround_time = [0] * num_process
waiting_time = [0] * num_process
start_time = [0] * num_process
visited = [False] * num_process

time = 0
completed = 0
gantt_chart = "|0|"

while completed < num_process:
    idx = -1
    min_priority = float('inf')


    for i in range(num_process):
        if arrival_time[i] <= time and not visited[i]:
            if priority[i] < min_priority:
                min_priority = priority[i]
                idx = i
            elif priority[i] == min_priority:
                if arrival_time[i] < arrival_time[idx]:
                    idx = i

    if idx != -1:
        start_time[idx] = time
        time += burst_time[idx]
        completion_time[idx] = time
        turnaround_time[idx] = completion_time[idx] - arrival_time[idx]
        waiting_time[idx] = turnaround_time[idx] - burst_time[idx]
        visited[idx] = True
        completed += 1
        gantt_chart += f"{process_list[idx]}|{time}|"
    else:
        time += 1
        gantt_chart += f"idle|{time}|"


results = list(zip(process_list, arrival_time, burst_time, priority, completion_time, turnaround_time, waiting_time))


results.sort(key=lambda x: original_names.index(x[0]))


avg_tat = sum(tat for *_, tat, _ in results) / num_process
avg_wt = sum(wt for *_, wt in results) / num_process


print("\nProcess\tAT\tBT\tPR\tCT\tTAT\tWT")
for row in results:
    print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}\t{row[4]}\t{row[5]}\t{row[6]}")

print("\nGantt Chart:")
print(gantt_chart)
print(f"\nAverage Turnaround Time: {avg_tat:.2f} ms")
print(f"Average Waiting Time: {avg_wt:.2f} ms")