# FIFO Page Replacement in Python

# Input
frame_size = int(input("Enter frame size: "))
num_pages = int(input("Enter number of pages: "))
pages = list(map(int, input("Enter page reference sequence: ").split()))

frames = [-1] * frame_size
fifo_queue = []
page_faults = 0
page_hits = 0

print("\nPage Reference | Frames Status | Hit/Miss")
print("--------------------------------------------")

for current_page in pages:
    found = False

    if current_page in frames:
        found = True
        page_hits += 1

    print(f"      {current_page}        | ", end='')

    if not found:
        page_faults += 1

        if len(fifo_queue) < frame_size:
            for i in range(frame_size):
                if frames[i] == -1:
                    frames[i] = current_page
                    fifo_queue.append(current_page)
                    break
        else:
            page_to_replace = fifo_queue.pop(0)
            for i in range(frame_size):
                if frames[i] == page_to_replace:
                    frames[i] = current_page
                    fifo_queue.append(current_page)
                    break

        for f in frames:
            print(f"[{f}]" if f != -1 else "[ ]", end=" ")
        print("| MISS")
    else:
        for f in frames:
            print(f"[{f}]" if f != -1 else "[ ]", end=" ")
        print("| HIT")

print("\n====== RESULTS ======")
print(f"Total Page Requests: {num_pages}")
print(f"Total Page Hits: {page_hits}")
print(f"Total Page Faults: {page_faults}")
print(f"Hit Ratio: {page_hits / num_pages * 100:.2f}%")
print(f"Fault Ratio: {page_faults / num_pages * 100:.2f}%")
