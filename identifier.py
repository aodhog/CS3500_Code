import stop

#cleans the text file line
def readCleanLine(sensor):
    line=sensor.readline()
    if line=="":
       return None
    line=line.split("\n")[0]
    line=line.split(': ')
    return line


def impediment():

    #opens both files
    sensor = open("sensor.txt","r")
    identifiertxt=open("identifier.txt", "w")

    #gui requires a blank line to initialise
    identifiertxt.write("\n")

    cont=True
    while cont:
        line=readCleanLine(sensor)
        #checks the stop variable in the stop module
        #if w is None or blank then its ended as we haven't reached a full impediment
        if stop.Stop==True or line==None or '' in line:
            cont=False
            break
        
        
        #check impediment name
        #dictionary containing impediment code as key 
        # and then a list as the value which contains the name of the impediment and any minus signs needed in the impediment
        impediments={"ULD":["Speedbump", ["","","-"]], "DLU":["Pothole", ["-","",""]], 
                    "DLD":["Dip", ["-","","-"]], "ULU": ["Lip", ["","",""]], 
                    "ULL": ["Small U Hill", ["","",""]], "UUL": ["Medium U Hill", ["","",""]], "UUU": ["Large U Hill", ["","",""]], 
                    "DLL": ["Small D Hill", ["-","",""]], "DDL": ["Medium D Hill", ["-","-",""]], "DDD": ["Large D Hill", ["-","-","-"]]}
        impedimentCode=line[0][2]+line[1][2]+line[2][2]
        impediment=impediments[impedimentCode][0]
        identifiertxt.write(impediment+"\n")

        #get suspension and brake calculations
        
        #reads the angles ofr the imediment from the string
        angles=[int(line[0][7])*10+int(line[0][8]),
        int(line[1][7])*10+int(line[1][8]),
        int(line[2][7])*10+int(line[2][8])]

        #gets the adjustment needed for each angle
        for angle in angles:

            #this means its an L
            if angle==0:
                identifiertxt.write("0\n")
                identifiertxt.write("0\n")
                continue
            
            #Both U and D need a suspension so thats calculated
            suspension_level = round(( 3/4 * ( (angle*2) / 134) )*100)

            #only D and speedbumps need brakes 
            # if statement checks the dictionary for the impediment code, then goes to the second item in the values list
            #this is the list of negative signs, checks to see if its a negative sign, this means its a D.
            if  impediments[impedimentCode][1][angles.index(angle)]=="-" or impediment=="Speedbump":
                brake_strength = round(angle+1/90)
            else:
                #if its a U brakes are 0
                brake_strength = 0

            #writes the negative or no negative sign first then the calculation
            identifiertxt.write(f"{impediments[impedimentCode][1][angles.index(angle)]}{suspension_level}\n")
            #brakes are alwasy positive 
            identifiertxt.write(f"{brake_strength}\n")
    
    #closes both files
    identifiertxt.close()
    sensor.close()



