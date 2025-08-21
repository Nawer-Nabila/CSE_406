def SSTF(requests, head):
    seek_count = 0
    seek_sequence = []


    served = [False] * len(requests)

    for _ in range(len(requests)):
        min_distance = float('inf')
        index = -1


        for i in range(len(requests)):
            if not served[i]:
                distance = abs(requests[i] - head)
                if distance < min_distance:
                    min_distance = distance
                    index = i


        seek_count += min_distance
        head = requests[index]
        seek_sequence.append(head)
        served[index] = True


    print("\nTotal number of seek operations:", seek_count)
    print("Seek sequence:")
    for track in seek_sequence:
        print(track)


n = int(input("Enter number of disk requests: "))
requests = []

print("Enter the request values:")
for i in range(n):
    req = int(input(f"Request {i+1}: "))
    requests.append(req)

head = int(input("Enter initial head position: "))


SSTF(requests, head)