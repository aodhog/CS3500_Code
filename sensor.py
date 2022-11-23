from datetime import datetime
import stop

#makes the text line nice
def readCleanLine(road):
    line=road.readline()
    if line=="":
        return None
    line=line.split("\n")[0]
    line=line.split(',')
    return line


def sensor():
    #open file
    road = open("road.txt","r")
    sensortxt = open("sensor.txt", "w")
    #gets speed and calcs speed of scan
    speed=int(road.readline().split("\n")[0])
    if speed==0:
        return
    speedOfScan=round(3/(4*speed+1))
    #loops continually until the file is empty or progam ends

    #checks the stop variable in the stop file

    while stop.Stop==False:

        #reads first line 
        first=readCleanLine(road)
        #checks to see if its the end of the file
        if first==None:
            break
        time=datetime.now()
        #makes sure its not an L to start the impediment

        while first[0]=='L':
            if datetime.now().second==(time.second+speedOfScan or speedOfScan):
                time=datetime.now()
                #reads again
                first=readCleanLine(road)
                if first==None:
                    break
                

        #write all impediments to the sesnor text file 
        sensortxt.write(f"{first}: ")
        for i in range(2):
            #a stall tactic for the sensor
            wait=True
            while datetime.now().second!=(time.second+speedOfScan or speedOfScan)and wait==True:
                wait=True
            next=readCleanLine(road)
            if next==None:
                break

            if i==0:
                sensortxt.write(f"{next}: ")
            else:
                sensortxt.write(f"{next}\n")
            time=datetime.now()
    sensortxt.close()
    road.close()