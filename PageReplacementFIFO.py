from collections import deque #Imports a double-ended queue for the program
import random #Imports a random module for randomly generated pages

#Function That transfers the logical memory to physical memory 
def fifo_page_replacement(pages, frame_count):
    queue = deque() #Initialize a queue for the process
    page_faults = 0

    #Initialize a For loop to determine each page
    for page in pages:
        #If the current page is not currently within the queue, it will add an increment to page_fault
        if page not in queue:
            #If the queue is less than the frame_count(3), then the algorithm will add the current page into the queue
            if len(queue) < frame_count:
                queue.append(page)
            #If the queue is more or equals than the frame_count(3), the algorithm will replace the oldest page with the current one
            else:
                queue.popleft()
                queue.append(page)

            page_faults += 1
        print(f"Page: {page} -> Frames: {list(queue)}")

    print(f"\nTotal Page Faults: {page_faults}")

MaxPages=10 #Maximum number of pages in a logical memory
pages = [random.randint(1, 9) for frames in range(MaxPages)] #The code will randomly generate 10 numbers in logical memory
frame_count = 3 #Maximum size of physical address
print(f"Logical Memory: {pages}")
fifo_page_replacement(pages, frame_count)#Used to call the function
