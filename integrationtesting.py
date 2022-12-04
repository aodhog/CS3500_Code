import road, sensor, identifier
def guiWritingRoadSegment(speed):
    #gui would usually receive speed as an input from the user through the gui 
    # but will instead take it as a parameter of the function for the test
    
    #writes that speed to road.txt
    road=open("road.txt", "w")
    road.write(f"{speed}\n")
    road.close()

def guiReadingIdentifierSegment():
    #initialises variables 
    impediment=None
    suspensionLevel=None
    brakeStrength=None

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
    return impediment, suspensionLevel, brakeStrength



def guiToRoadTest():
    #gui will write to road.txt and road should be able to read the speed inputed on road.txt
    try:
        #gui code must be copied in as a segment as it contains tkinter commands that prevent direct testing.
        #the segment in the function above is the same as gui but with the tkinter commands removed
        speed=33
        guiWritingRoadSegment(speed)

        #manual handling of raod.txt to check if it was written correctly.
        r = open("road.txt", "r")
        comparison=int(r.readline().split("\n")[0])
        r.close()
        assert(speed)==comparison
    except:
        print("GUI to road integration test failed")

def roadAndSensorTest():
    #continuation of first integration test
    #road will write to road.txt and sensor should be able to read road.txt and write to sensor.txt
    try:
        #run previous test
        guiToRoadTest()

        #runs both python files.
        road.road()
        sensor.sensor()

        #retrieve the first impediment
        s = open("sensor.txt", "r")
        sample=s.readline()
        s.close()

        #manual handling of road.txt to compare.
        comparison=""
        r = open("road.txt", "r")
        r.readline()
        line=r.readline()
        line=line.split("\n")[0]
        line=line.split(',')

        while line[0]=="L":
            line=r.readline()
            line=line.split("\n")[0]
            line=line.split(',')
            

        comparison= comparison+str(line)+": "
        line=r.readline()
        line=line.split("\n")[0]
        line=line.split(',')
        comparison+=str(line)+": "
        line=r.readline()
        line=line.split("\n")[0]
        line=line.split(',')
        comparison+=str(line)+"\n"
        r.close()
        assert(sample)==comparison
    except:
        print("road to sensor integration test failed")

def sensorToIdentifierTest():
    #continuation of second integration test. 
    #sensor will write to sensor.txt and identifier should be able to read sensor.txt and write to identifier.txt
    try:

        #runs road and sensor files again
        roadAndSensorTest()
        #runs identifier file
        identifier.impediment()

        #retrieve first 7 lines of identifier text file for comparison
        linesSample=[]
        i = open("identifier.txt", "r")
        i.readline()
        for line in range(7):
            linesSample.append(i.readline())
        i.close()

        #manual handling of sensor text file for comparison

        #get first impediment
        s = open("sensor.txt", "r")
        w=s.readline()
        w=w.split("\n")[0]
        w=w.split(': ')

        
                #gets the angles from all three impediment directions and puts them in a list
        angles=[int(w[0][7])*10+int(w[0][8]),
        int(w[1][7])*10+int(w[1][8]),
        int(w[2][7])*10+int(w[2][8])]
        comparison=[]
        #checks to see what the impediment is
        if "U" in w[0] and "L" in w[1] and "D" in w[2]:
            indentify="Speedbump"
            comparison.append(f"{indentify}\n")
            #special case as it goes up and down same for pothole
            for angle in angles:
                if angle==0:
                    comparison.append(f"{0}\n")
                    comparison.append(f"{0}\n")
                elif angles.index(angle)==0:
                    #adjusted suspension level that uses the 3/4 meters distance and formats it as a percentage
                    #this is in every if statement
                    suspension_level = round(( 3/4 * ( (angle*2) / 134) )*100)
                    #brake strength calculated as a percentage rounded
                    brake_strength = round(angle+1/90)
                    comparison.append(f"{suspension_level}\n")
                    comparison.append(f"{brake_strength}\n")
                else:
                    suspension_level = round(( -3/4 * ( (angle*2) / 134) )*100)
                    brake_strength = round(angle+1/90)
                    comparison.append(f"{suspension_level}\n")
                    comparison.append(f"{brake_strength}\n")

        elif "D" in w[0] and "D" in w[1] and "D" in w[2]:
            indentify="Large D Hill"
            comparison.append(f"{indentify}\n")
            for angle in angles:
                suspension_level = round(( -3/4 * ( (angle*2) / 134) )*100)
                brake_strength = round(angle+1/90)
                comparison.append(f"{suspension_level}\n")
                comparison.append(f"{brake_strength}\n")
        elif "D" in w[0] and "D" in w[1] and "L" in w[2]:
            indentify="Medium D Hill"
            comparison.append(f"{indentify}\n")
            for angle in angles:
                if angle==0:
                    comparison.append(f"{0}\n")
                    comparison.append(f"{0}\n")
                else:
                    suspension_level = round(( -3/4 * ( (angle*2) / 134) )*100)
                    brake_strength = round(angle+1/90)
                    comparison.append(f"{suspension_level}\n")
                    comparison.append(f"{brake_strength}\n")
        elif "D" in w[0] and "L" in w[1] and "L" in w[2]:
            indentify="Small D Hill"
            comparison.append(f"{indentify}\n")
            for angle in angles:
                if angle==0:
                    comparison.append(f"{0}\n")
                    comparison.append(f"{0}\n")
                else:
                    suspension_level = round(( -3/4 * ( (angle*2) / 134) )*100)
                    brake_strength = round(angle+1/90)
                    comparison.append(f"{suspension_level}\n")
                    comparison.append(f"{brake_strength}\n")
        elif "D" in w[0] and "L" in w[1] and "D" in w[2]:
            indentify="Dip"
            comparison.append(f"{indentify}\n")
            for angle in angles:
                if angle==0:
                    comparison.append(f"{0}\n")
                    comparison.append(f"{0}\n")
                else:
                    suspension_level = round(( -3/4 * ( (angle*2) / 134) )*100)
                    brake_strength = round(angle+1/90)
                    comparison.append(f"{suspension_level}\n")
                    comparison.append(f"{brake_strength}\n")
        elif "D" in w[0] and "L" in w[1] and "U" in w[2]:
            indentify="Pothole"
            comparison.append(f"{indentify}\n")
            for angle in angles:
                if angle==0:
                    comparison.append(f"{0}\n")
                    comparison.append(f"{0}\n")
                elif angles.index(angle)==0:
                    suspension_level = round(( -3/4 * ( (angle*2) / 134) )*100)
                    brake_strength = round(angle+1/90)
                    comparison.append(f"{suspension_level}\n")
                    comparison.append(f"{brake_strength}\n")
                else:
                    suspension_level = round(( 3/4 * ( (angle*2) / 134) )*100)
                    brake_strength = round(angle+1/90)
                    comparison.append(f"{suspension_level}\n")
                    comparison.append(f"{0}\n")
        elif "U" in w[0] and "L" in w[1] and "U" in w[2]:
            indentify="Lip"
            comparison.append(f"{indentify}\n")
            for angle in angles:
                if angle==0:
                    comparison.append(f"{0}\n")
                    comparison.append(f"{0}\n")
                else:
                    suspension_level = round(( 3/4 * ( (angle*2) / 134) )*100)
                    brake_strength = 0
                    comparison.append(f"{suspension_level}\n")
                    comparison.append(f"{brake_strength}\n")
        elif "U" in w[0] and "L" in w[1] and "L" in w[2]:
            indentify="Small U Hill"
            comparison.append(f"{indentify}\n")
            for angle in angles:
                if angle==0:
                    comparison.append(f"{0}\n")
                    comparison.append(f"{0}\n")
                else:
                    suspension_level = round(( 3/4 * ( (angle*2) / 134) )*100)
                    brake_strength = 0
                    comparison.append(f"{suspension_level}\n")
                    comparison.append(f"{brake_strength}\n")
        elif "U" in w[0] and "U" in w[1] and "L" in w[2]:
            indentify="Medium U Hill"
            comparison.append(f"{indentify}\n")
            for angle in angles:
                if angle==0:
                    comparison.append(f"{0}\n")
                    comparison.append(f"{0}\n")
                else:
                    suspension_level = round(( 3/4 * ( (angle*2) / 134) )*100)
                    brake_strength = 0
                    comparison.append(f"{suspension_level}\n")
                    comparison.append(f"{brake_strength}\n")
        elif "U" in w[0] and "U" in w[1] and "U" in w[2]:
            indentify="Large U Hill"
            comparison.append(f"{indentify}\n")
            for angle in angles:
                suspension_level = round(( 3/4 * ( (angle*2) / 134) )*100)
                brake_strength = 0
                comparison.append(f"{suspension_level}\n")
                comparison.append(f"{brake_strength}\n")
        assert(linesSample)==comparison
    except:
        print("sensor to identifier integration test failed")

def identifierToGuiTest():
    #continuation of seconthirdd integration test. 
    #identifier will write to identifier.txt and gui should be able to read identifier.txt
    try:
        #run first and second test
        sensorToIdentifierTest()
        
        #gui code must be copied in as a segment as it contains tkinter commands that prevent direct testing.
        #the segment in the function above is the same as gui but with the tkinter commands removed
        global ident
        ident = open("identifier.txt", "r")
        ident.readline()
        #using a list to represent the expected output rather than the gui
        sample=[]
        for x in range(4):
            impediment, suspensionLevel, brakeStrength = guiReadingIdentifierSegment()
            if x==0:
                sample.append(impediment)
            else:
                sample.append(suspensionLevel)
                sample.append(brakeStrength)
        ident.close()

        #manually get information for comparision
        i = open("identifier.txt", "r")
        i.readline()
        #gets impediment name
        line=i.readline()
        line=line.split("\n")[0]
        comparison=[line]
        #suspension and brakes 1
        line=i.readline()
        line=line.split("\n")[0]
        comparison.append(50+(int(line)/100)*50)
        line=i.readline()
        line=line.split("\n")[0]
        comparison.append(int(line))
         #suspension and brakes 2
        line=i.readline()
        line=line.split("\n")[0]
        comparison.append(50+(int(line)/100)*50)
        line=i.readline()
        line=line.split("\n")[0]
        comparison.append(int(line))
         #suspension and brakes 3
        line=i.readline()
        line=line.split("\n")[0]
        comparison.append(50+(int(line)/100)*50)
        line=i.readline()
        line=line.split("\n")[0]
        comparison.append(int(line))
        
        i.close()
        
        assert(sample)==comparison
    except:
        print("identifier to GUI integration test failed")


guiToRoadTest()
roadAndSensorTest()
sensorToIdentifierTest()
identifierToGuiTest()
