import identifier, stop

def identifiertestcase1():
    #test to see if the program ends if stop.Stop is true
    try:
        #set stop to True which means nothing should be added to identifier text file and program will end
        stop.Stop=True

        #call the impediment identifier function
        identifier.impediment()

        #get all lines from the identifier text
        identifiertxt=open("identifier.txt", "r")
        identifierlst=identifiertxt.readlines()
        identifiertxt.close()
        #if program was ended at line 27 in indentifer.py then nothing should be in identifier.txt 
        # So length will equal 1 
        #(\n is put in the file no matter what to ensure the gui reads the file properly)
        assert(len(identifierlst))==1
    except:
        print("identifier test case 1 failed")

def identifiertestcase2():
    #test to see if the program ends if the impediment reading from sensor.txt is empty
    try:
        #clears the sensor text file
        sensor=open("sensor.txt", "w")
        sensor.close()

        stop.Stop=False
        #call the impediment identifier function
        identifier.impediment()

        #get all lines from the identifier text
        identifiertxt=open("identifier.txt", "r")
        identifierlst=identifiertxt.readlines()
        identifiertxt.close()
        #if program was ended at line 27 in indentifer.py then nothing should be in identifier.txt 
        # So length will equal 1 
        #(\n is put in the file no matter what to ensure the gui reads the file properly)
        assert(len(identifierlst))==1
    except:
        print("identifier test case 2 failed")

def identifiertestcase3():
    #test to see if the program ends if the impediment reading from sensor.txt is contains an empty value
    try:
        #adds an incomplete impediment to sensor text file
        sensor=open("sensor.txt", "w")
        sensor.write("['U', '87']: ['L', '00']: ")
        sensor.close()

        stop.Stop=False
        #call the impediment identifier function
        identifier.impediment()

        #get all lines from the identifier text
        identifiertxt=open("identifier.txt", "r")
        identifierlst=identifiertxt.readlines()
        identifiertxt.close()
        #if program was ended at line 27 in indentifer.py then nothing should be in identifier.txt 
        # So length will equal 1 
        #(\n is put in the file no matter what to ensure the gui reads the file properly)
        assert(len(identifierlst))==1
    except:
        print("identifier test case 3 failed")

def identifiertestcase4():
    #test to see if 0 is written to identifier text file for both brake sand suspension if angle is 0
    try:
        #writes a Small U Hill to sensor text file to be read. (contains two L's with angle 0)
        sensor=open("sensor.txt", "w")
        sensor.write("['U', '30']: ['L', '00']: ['L', '00']\n")
        sensor.close()
        
        #run program
        identifier.impediment()

        #get all lines from the identifier text
        identifiertxt=open("identifier.txt", "r")
        identifierlst=identifiertxt.readlines()
        identifiertxt.close()

        #0 should come back as the value for part 2 and 3 of the impediment
        #therefore adding them together will give 0 and be easier to test
        zerotest=0
        for line in range(4,len(identifierlst)):
            zerotest+=int(identifierlst[line])
        assert(zerotest)==0
    except:
        print("identifier test case 4 failed")

def identifiertestcase5():
    #test to see if an impediment contains a D that it is written to the file as a negative
    try:
        #writes a Large D Hill to sensor text file to be read. (contains all negative suspension values)
        sensor=open("sensor.txt", "w")
        sensor.write("['D', '30']: ['D', '30']: ['D', '30']\n")
        sensor.close()
        
        #run program
        identifier.impediment()

        #get all lines from the identifier text
        identifiertxt=open("identifier.txt", "r")
        identifierlst=identifiertxt.readlines()
        identifiertxt.close()

        #Only suspension can be negative so we get every second value
        for line in range(2,len(identifierlst),2):
            #all suspension values should be negative
            assert(int(identifierlst[line]))<0
        
    except:
        print("identifier test case 5 failed")

def identifiertestcase6():
    #test to see if a speedbump that it is written to the file contains a negative value
    try:
        #writes a speedbump to sensor text file to be read. (contains negative value at the end)
        sensor=open("sensor.txt", "w")
        sensor.write("['U', '40']: ['L', '00']: ['D', '30']\n")
        sensor.close()
        
        #run program
        identifier.impediment()

        #get all lines from the identifier text
        identifiertxt=open("identifier.txt", "r")
        identifierlst=identifiertxt.readlines()
        identifiertxt.close()

        #check to see if the third suspension value is negative and no others
        for line in range(2,len(identifierlst)):
            if line==6:
                assert(int(identifierlst[line]))<0
            else:
                assert(int(identifierlst[line]))>=0
        
    except:
        print("identifier test case 6 failed")

def identifiertestcase7():
    #test to see if an impediment is not a speedbump or contains a negative, it sets brakeStrength to 0
    try:
        #writes all remaining non negative 
        sensor=open("sensor.txt", "w")
        sensor.write("['U', '40']: ['L', '00']: ['U', '30']\n")
        sensor.write("['U', '40']: ['L', '00']: ['L', '00']\n")
        sensor.write("['U', '40']: ['U', '40']: ['L', '00']\n")
        sensor.write("['U', '40']: ['U', '40']: ['U', '40']\n")
        sensor.close()
        
        #run program
        identifier.impediment()

        #get all lines from the identifier text
        identifiertxt=open("identifier.txt", "r")
        identifierlst=identifiertxt.readlines()
        identifiertxt.close()

        #check to see if the third suspension value is negative and no others
        for line in range(1,len(identifierlst)):
            #if statement to separate the name form the calculations
            if (line-1)%7==0:
                continue
            else:
                #both brakes and suspension should be positive
                assert(int(identifierlst[line]))>=0
        
    except:
        print("identifier test case 7 failed")


identifiertestcase1()
identifiertestcase2()
identifiertestcase3()
identifiertestcase4()
identifiertestcase5()
identifiertestcase6()
identifiertestcase7()
