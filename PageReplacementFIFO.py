from collections import deque #Imports a double-ended queue for the program
import random #Imports a random module for randomly generated pages
from tkinter import * #Imports a GUI to use

#Function That transfers the logical memory to physical memory 
def fifo_page_replacement(Pages, Frame_Count, OutputTxt):
    Queue = deque() #Initialize a queue for the process
    Page_Faults = 0
    OutputTxt.delete("1.0", END)


    #Initialize a For loop to determine each page
    for page in Pages:
        #If the current page is not currently within the queue, it will add an increment to page_fault
        if page not in Queue:
            #If the queue is less than the frame_count(3), then the algorithm will add the current page into the queue
            if len(Queue) < Frame_Count:
                Queue.append(page)
            #If the queue is more or equals than the frame_count(3), the algorithm will replace the oldest page with the current one
            else:
                Queue.popleft()
                Queue.append(page)

            Page_Faults += 1
        OutputTxt.insert(END, f"Page: {page} -> Frames: {list(Queue)}\n")

    OutputTxt.insert(END, f"\nTotal Page Faults: {Page_Faults}\n")

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
Frame1 = Frame(Window, width=300, height=300)
Frame1.grid(row=0, column=0)

#Shows the output of the Program
OutputTxt = Text(Window, width= 60, height=20)
OutputTxt.place(relx=0.5, rely=0.6, anchor=CENTER)

#Parameters Used
MaxPages = 10#Maximum number of pages in a logical memory
Frame_Count = 3 #Maximum size of physical address
Pages = []

#Used to call the function
GeneratePages(MaxPages, Pages)
fifo_page_replacement(Pages, Frame_Count, OutputTxt)

#Shows the Randomly Generated Number
RandomNumLbl = Label(Window, text=f"Pages inside inside the memory: {Pages}")
RandomNumLbl.place(relx=0.5, rely=0.1, anchor=CENTER)

#Start the GUI
Window.mainloop()
