def scan(requests, head, direction):
    seek_count = 0

    left = [r for r in requests if r < head]
    right = [r for r in requests if r >= head]

    left.sort()
    right.sort()

    if direction == "left":
        if left:
            seek_count += abs(head - left[0])
            head = left[0]

        if right:
            seek_count += abs(head - right[-1])
            head = right[-1]

    elif direction == "right":

        if right:
            seek_count += abs(head - right[-1])
            head = right[-1]


        if left:
            seek_count += abs(head - left[0])
            head = left[0]

    return seek_count


requests = list(map(int, input("Enter requests separated by space: ").split()))
head = int(input("Enter current head position: "))
direction = input("Enter direction (left/right): ").lower()

total_seek = scan(requests, head, direction)
if total_seek is not None:
    print(f"Total seek time: {total_seek}")
