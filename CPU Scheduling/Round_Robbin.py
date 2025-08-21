num_process = int(input("Enter the number of process: "))
quantum = int(input("Enter the quantum: "))
process_list,at_list,bt_list = [],[],[]

for _ in range(num_process):
    name,at,bt = input("Enter Process(P1-9 AT BT): ").split()
    process_list.append(name)
    at_list.append(int(at))
    bt_list.append(int(bt))

remaining_time_list = bt_list.copy()
ct_list = [0]*num_process
tat_list = [0]*num_process
wt_list = [0]*num_process

visited = [False]* num_process

time = 0
gantt = "|0|"
ready = []
done = 0

while done < num_process:
    for i in range(num_process):
        if at_list[i] <= time and not visited[i]:
            ready.append(i)
            visited[i] = True

    if ready:
        i = ready.pop(0)
        if remaining_time_list[i] > quantum:
            time += quantum
            remaining_time_list[i] -= quantum
        else:
            time += remaining_time_list[i]
            remaining_time_list[i] = 0
            ct_list[i] = time
            tat_list[i] = ct_list[i] - at_list[i]
            wt_list[i] = tat_list[i] - bt_list[i]
            done += 1
        gantt += f"{process_list[i]}|{time}|"

        for j in range(num_process):
            if at_list[j] <= time and not visited[j]:
                ready.append(j)
                visited[j] = True
        if remaining_time_list[i] > 0:
            ready.append(i)


avg_tat = sum(tat_list)/num_process
avg_wt = sum(wt_list)/num_process

print("\nProcess\tAT\tBT\tCT\tTAT\tWT")
for i in range(num_process):
    print(f"{process_list[i]}\t{at_list[i]}\t{bt_list[i]}\t{ct_list[i]}\t{tat_list[i]}\t{wt_list[i]}")

print("\nGantt Chart:")
print(gantt)
print(f"\nAverage Turnaround Time: {avg_tat:.2f} ms")
print(f"Average Waiting Time: {avg_wt:.2f} ms")


