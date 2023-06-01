"tkinter for importing library"
from tkinter import*
from tkinter.ttk import* #from tkinter import another library name ttk
#the library contains all the buttons such as add, edit, delete, and quit)

def addEvent():
    time_input= timeEntry.get().strip()#strip delete spaces infront
    event_input = eventEntry.get().strip()
    if len(time_input)==0 or len(event_input)==0:
        return #if nothing input, nothing happens 
    tree.insert(parent="", index="end", values= (time_input,event_input))
    timeEntry.delete(0,"end")#delete the input from begin to end after add event
    eventEntry.delete(0,"end")
    
def updateEvent():
    row_num = tree.focus()
    if row_num != "": #if nothing is there, then no need to change
        values= tree.item(row_num)["values"] #get the previous input
        timeEntry.delete(0,"end") #prevent previous inputs getting into new input
        eventEntry.delete(0,"end")
        timeEntry.insert(0,values[0]) #insert new input back in table
        eventEntry.insert(0,values[1])
        tree.delete(row_num)
    
def deleteEvent():
    rows_num= tree.selection() #selection allows user to delete event
    for row_num in rows_num:
        tree.delete(row_num)
    
def quitEvent():
    GUI.destroy() #algorithm terminates
    
def sortColumn(col):
    lst = []
    for st in tree.get_children(""):
        item = (tree.set(st, col), st) # [('9:00', 'E001'), ('8:00', 'E002')] st = subtree child_node
        lst.append(item)
    print(lst)

    newlist = []
    for i in lst:
        hour = i[0].split(":")[0] 
        minute = i[0].split(":")[1] 
        num = int(hour) * 60 + int(minute) #calculate time together, then sort the time(line 46).
        newlist.append((num,i[1]))

    newlist.sort()
    print(newlist)
    
    for index, item in enumerate(newlist):
        tree.move(item[1], "", index)


    
"Create window"
GUI = Tk()
GUI.title("Party Planner") #GUI name
GUI.geometry("500x300") #GUI size

tree = Treeview(GUI,columns=("Time", "Event"),show="headings", selectmode="extended")#Create a treeview widget
tree.heading("Time", text="Time")
tree.heading("Event", text="Event")
tree.pack()

frame= Frame(GUI) #Create the frame of the planner
frame.pack(pady= 10)#distance between each frame is 10 pixels from each other 

#create button and box for input time and event
timeLabel= Label(frame,text= "Time (hh:mm) ")
timeLabel.grid(row= 0, column= 0,padx=5)
timeEntry= Entry(frame,width= 10)
timeEntry.grid(row= 0, column= 1,padx=5)

eventLabel= Label(frame,text= "Event: ")
eventLabel.grid(row= 0, column= 2,padx=5)
eventEntry= Entry(frame,width= 10)
eventEntry.grid(row= 0, column= 3,padx=5)

addButton= Button(frame, text= "Add Event", command= addEvent)
addButton.grid(row= 1, column= 0,padx=5)#pad x means to seperate the buttons 5 pixels apart

updateButton= Button(frame, text= "Update Event", command= updateEvent)
updateButton.grid(row= 1, column= 1,padx=5)

deleteButton= Button(frame, text= "Delete Event", command= deleteEvent)
deleteButton.grid(row= 1, column= 2,padx=5)

quitButton= Button(frame, text= "Quit", command= quitEvent)
quitButton.grid(row= 1, column= 3, padx=5)

tree.heading("#1",text="Time", command=lambda col="Time": sortColumn(col))
GUI.mainloop() #showing the tree widget and window


