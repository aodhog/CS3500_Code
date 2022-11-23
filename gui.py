from tkinter import *
from tkinter.ttk import Progressbar
import time
import sensor, road as r, identifier as i, stop
from threading import Thread

#functions at the top of the code by convention but the gui is really established below.

#the start function begins the program as a whole
def start():
    #gets the entered speed in the gui
    speed=entryBox.get()

    #writes that speed to road.txt
    road=open("road.txt", "w")
    road.write(f"{speed}\n")
    road.close()

    #starts running all files in order. gap isn't entirely neccessary but might be when we stop the code.
    #Threading is just a fancy term for running at the same time.
    Thread(target = r.road(), daemon=True).start() 
    time.sleep(0.01)
    Thread(target = sensor.sensor(),  daemon=True).start()
    Thread(target = i.impediment(),  daemon=True).start()


    #opnes the identifier text file and makes it global (can be changed from anywhere).
    global ident
    ident=open("identifier.txt", "r")
    #reads blank line and does nothing. I don't know why but the code doesn't work unless it's there.
    ident.readline()

    #calls the calculation function
    calc(int(speed))

    if stop.Stop==True:
        return

def calc(speed):
    if stop.Stop==True:
        return
    #establishes the new suspension and brakes as the previous so they don't reset at a new impediment
    suspensionLevel=suspension['value']
    brakeStrength=brake['value']

    #gets the next line
    line=ident.readline()
    #makes it pretty
    line=line.split("\n")[0]

    #try and except statement to test if its a new impediment.
    
    try:
        #checks to see if its a number
        sl=round(float(line))
        #calculates where to move the suspension to from last time
        suspensionLevel=50+(int(sl)/100)*50
        #reads in brake strength
        bs=round(float(ident.readline()))
        brakeStrength=bs
    except:
        #If its the name of the impediment then it's printed to the gui
        impediment=line.split("\n")[0]
        c.itemconfigure(impedimentL, text=impediment)

    #if the new suspension and brake strength is different, then go to the step function
    if suspensionLevel!=suspension['value'] or brakeStrength!=brake['value']:
        step(brakeStrength, suspensionLevel,speed)
    else:
        #wait a moment and then run the next calculation
        #time may need to be adjusted
        time.sleep(4/(speed+1))
        calc(speed)

    
#moves the suspension and brakes and works auxiliaries
def step(brakeStrength, suspensionLevel, speed):

    #diviser decides how big a jump the suspension and brakes move on the gui
    diviser=7
    
    #checks to see if the car should be emergency stopped
    if (suspensionLevel>100 or suspensionLevel<0 or brakeStrength>=100) and speed>0:
        c.itemconfig(handbrake, fill='red')
        c.itemconfig(warninglight, fill='red')
        brake['value']=110
        suspensionLevel=50
        speed=0

    #checks to see if the car is just stopped
    elif speed==0:
         c.itemconfig(handbrake, fill='red')
         return
    #turns off lights if not needed
    else:
        c.itemconfig(handbrake, fill='')
        c.itemconfig(warninglight, fill='')

    #tidies up the difference between the new and old suspension and brake values so its not janky
    suspensionLevel=suspensionLevel-(suspensionLevel-suspension['value'])%diviser
    brakeStrength=brakeStrength-(brakeStrength-brake['value'])%diviser

    #while loops to adjust suspenison and brakes up or down depending on what they need
    while suspension['value']<suspensionLevel:
        ws.update_idletasks()
        suspension['value'] += diviser
        #speed of the car determines how quickly the suspension or brakes are moved
        time.sleep(1/(speed+1))

    while suspension['value']>suspensionLevel:
        ws.update_idletasks()
        suspension['value'] -= diviser
        time.sleep(1/(speed+1))

    #Turns on brake slights if needed
    if brakeStrength>0:
        c.itemconfig(brakelights, fill='red')
    
    #adjusts brakes to full if needed
    if brakeStrength>=100:
        brakeStrength=110
        c.itemconfig(warninglight, fill='red')
        c.itemconfig(handbrake, fill='red')
   
    #while loops for brakes
    while brake['value']<brakeStrength:
        ws.update_idletasks()
        brake['value'] += diviser
        time.sleep(1/(speed+1))
    
    while brake['value']>brakeStrength:
        c.itemconfig(brakelights, fill='')
        ws.update_idletasks()
        brake['value'] -= diviser
        time.sleep(1/(speed+1))

    #delay and then calculate next impediment again
    time.sleep(1/(speed+1))

    calc(speed)


#tkinter set up for thre gui
ws = Tk()

#the window
ws.title('Automatic Suspension and Brake System')
ws.geometry('800x500')
ws.config(bg='#345')


#brakes bar
brake = Progressbar(
    ws,
    orient = HORIZONTAL,
    length = 280,
    mode = 'determinate'
    )

brake.place(x=40, y=27)

#its labels
brakelabel = Label(ws, text='Brakes')
brakelabel.place(x=40, y=5)

brake0 = Label(ws, text='0%')
brake0.place(x=30, y=50)

brake50 = Label(ws, text='50%')
brake50.place(x=160, y=50)

brake100 = Label(ws, text='100%')
brake100.place(x=300, y=50)

#suspension bar
suspension = Progressbar(
    ws,
    orient = VERTICAL,
    length = 280,
    mode = 'indeterminate'
    )

#sets suspension to 0 
suspension['value']=50
suspension.place(x=600, y=40)

#its labels
suspensionlabel = Label(ws, text='Suspension')
suspensionlabel.place(x=625, y=40)

suspension0 = Label(ws, text='-0.1')
suspension0.place(x=568, y=35)

suspension50 = Label(ws, text='0')
suspension50.place(x=580, y=165)

suspension100 = Label(ws, text='+0.1')
suspension100.place(x=568, y=310)

#Create a canvas object for our lights
c= Canvas(ws,width=400, height=40, bg='#345', bd=0, highlightthickness=0)
c.place(x=100, y=210)

#creates the lights
brakelights=c.create_oval(0,2,39,39, fill="")
warninglight=c.create_oval(50,2,90,39, fill="")
handbrake=c.create_oval(100,2,140,39, fill="")

#start button that calls the start function
Button(
    ws,
    text='Start',
    command=start
).place(x=100, y=150)


#speed box
entrytext = IntVar()
entryBox=Entry(ws, textvariable=entrytext)
entryBox.place(x=150, y=150)


#placing the lights
brakelightL = Label(ws, text='brakelights')
brakelightL.place(x=60, y=255)

warninglightL = Label(ws, text='warning-light')
warninglightL.place(x=130, y=255)

handbrakeL = Label(ws, text='handbrake')
handbrakeL.place(x=220, y=255)

#impediment name
impedimentL=c.create_text(300, 20,text='', font=20)

def gui():
#updates gui
    ws.mainloop()

gui()

