def c_scan(requests, head, direction):
    total_movement = 0


    requests = [r for r in requests if r != head]


    requests.sort()


    left = [r for r in requests if r < head]
    right = [r for r in requests if r > head]

    if direction == "right":

        for r in right:
            total_movement += abs(head - r)
            head = r


        if left:
            total_movement += abs(head - 0)
            head = 0
            for r in left:
                total_movement += abs(head - r)
                head = r

    elif direction == "left":

        for r in reversed(left):
            total_movement += abs(head - r)
            head = r


        if right:
            disk_end = max(requests + [head])
            total_movement += abs(head - disk_end)
            head = disk_end
            for r in reversed(right):
                total_movement += abs(head - r)
                head = r
    else:
        print("Invalid direction! Please enter 'left' or 'right'.")
        return

    print("Total Seek Operations:", total_movement)



requests = list(map(int, input("Enter requests separated by space: ").split()))
head = int(input("Enter current head position: "))
direction = input("Enter direction (left/right): ").lower()


c_scan(requests, head, direction)