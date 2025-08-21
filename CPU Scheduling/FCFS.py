def FCFS(requests, head):
    seek_count = 0
    visited=set()
    visited.add(head)


    for track in requests:
        if track not in visited:
            distance = abs(track - head)
            seek_count += distance
            head = track
            visited.add(track)

        else:
            print(f" {track} already visited")



    print("\nTotal number of seek operations =", seek_count)


n = int(input("Enter the number of disk requests: "))

requests = []
print(f"Enter {n} request values (one by one):")
for i in range(n):
    val = int(input(f"Request {i + 1}: "))
    requests.append(val)

head = int(input("Enter the initial head position: "))

FCFS(requests, head)