import tkinter as tk
from tkinter import font as tkFont
from tkinter import simpledialog
import NewVehicle_Capture
global txt_area
global imname

def capture():
    global imname
    name= simpledialog.askstring(title="Name",prompt="Enter image name")
  
    NewVehicle_Capture.captureImage(name)
    imname = name+'.jpg'
    txt_area.insert(tk.INSERT, "Image Captured Successfully")
    
    
def start():
    window=tk.Tk()
    window.title("ALPR System")
    window.geometry("600x600")

    helv36 = tkFont.Font(family='Helvetica', size=20, weight=tkFont.BOLD)

    button1 = tk.Button(window,text="Capture Image",width=20,height=2,bg="blue",fg="yellow", command=capture, font=helv36)
    button1.grid(row=1,column=0)

    label1= tk.Label(window,text = "Status").place(x =10, y = 250)
    global txt_area
    txt_area= tk.Text(window, height=5, width=50)
    txt_area.place(x =10, y = 275)
    window.mainloop()
    
