from collections import deque #Imports a double-ended queue for the program
import random #Imports a random module for randomly generated pages
from tkinter import * #Imports a GUI to use

#Function That transfers the logical memory to physical memory 
def fifo_page_replacement(Pages, frame_count, Output):
    queue = deque() #Initialize a queue for the process
    page_faults = 0
    Output.delete("1.0", END)


    #Initialize a For loop to determine each page
    for page in Pages:
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
        Output.insert(END, f"Page: {page} -> Frames: {list(queue)}\n")

    Output.insert(END, f"\nTotal Page Faults: {page_faults}\n")

#Function that randomly Generates Number for the pages 
def GeneratePages(MaxPages, Pages): 
    
    for i in range(MaxPages): #The code will randomly generate 10 numbers in logical memory
        Pages.append(random.randint(0,9))
    return Pages

#Initialize the GUI
Window = Tk()
Window.title("First In First Out")
Window.geometry("500x500")
#Frame for the GUI
frame1 = Frame(Window, width=300, height=300)
frame1.grid(row=0, column=0)

#Shows the output of the Program
Output = Text(Window, width= 60, height=20)
Output.place(relx=0.5, rely=0.6, anchor=CENTER)

#Parameters Used
MaxPages = 10#Maximum number of pages in a logical memory
frame_count = 3 #Maximum size of physical address
Pages = []

#Used to call the function
GeneratePages(MaxPages, Pages)
fifo_page_replacement(Pages, frame_count, Output)

#Shows the Randomly Generated Number
RandomNum = Label(Window, text=f"Pages inside inside the memory: {GeneratePages(MaxPages, Pages)}")
RandomNum.place(relx=0.5, rely=0.1, anchor=CENTER)

#Start the GUI
Window.mainloop()
