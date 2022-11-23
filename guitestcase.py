#gui test cases have to be done in isolation so that the gui isn't opened

def tryExceptTest():
    #segment of code from gui code file 
    #for distiguishing between the name of an impediment and its values
    identifier=open("identifier.txt", "r")
    line=identifier.readline()
    line=line.split("\n")[0]
    try:
        sl=round(float(line))
        suspensionLevel=50+(int(sl)/100)*50
        bs=round(float(identifier.readline()))
        brakeStrength=bs
        return suspensionLevel, brakeStrength
    except:
        impediment=line.split("\n")[0]
        return impediment, None

def emergencystoptest(suspensionLevel, brakeStrength, speed):
    #segment of code from gui code file for emergency stops
    if (suspensionLevel>100 or suspensionLevel<0 or brakeStrength>=100) and speed>0:
        brakeStrength=100
        suspensionLevel=50
        speed=0
    return suspensionLevel,brakeStrength, speed

def guitestcase1():
    #test that both the try and except parts of reading the identifier file are accessed correctly
    try:
        #write a standard impediment name to identifer text file to be read
        identifier=open("identifier.txt", "w")
        identifier.write("Medium D Hill")
        identifier.close()

        #run the try-except segment from gui code file
        first, second=tryExceptTest()
        #first thing to be read from file should be the impediment name
        assert(type(first))==str
        assert(second)==None

        #write to the identifier text file again except with standard measurments this time
        identifier=open("identifier.txt", "w")
        identifier.write("-8\n7\n")
        identifier.close()
        #run the try-except segment from gui code file again
        first, second=tryExceptTest()
        
        #both numbers should be read from the text file as a float and int
        assert(type(first))==float
        assert(type(second))==int

    except:
        print("GUI test case 1 failed")


def guitestcase2():
    #test to see if the emergency stop if statment functions as predicted
    try:
        #as a control we run the segment of code with no values that flag an emergency stop
        suspensionLevel, brakeStrength, speed=emergencystoptest(100,99,1)
       
       #numbers should not be unadjusted as no stop is nessasary
        assert( suspensionLevel==100 and brakeStrength==99 and speed==1)==True

        #same control test is performed for minimum suspension input
        suspensionLevel, brakeStrength, speed=emergencystoptest(0,99,1)
        assert( suspensionLevel==0 and brakeStrength==99 and speed==1)==True

        #same control test is performed for 0 speed
        suspensionLevel, brakeStrength, speed=emergencystoptest(100,99,0)
        assert( suspensionLevel==100 and brakeStrength==99 and speed==0)==True

        #runs the segment of code with a brake strength value that should flag emergency stop
        suspensionLevel, brakeStrength, speed=emergencystoptest(99,101,1)

        #emergency stop activates so values equal emergency stop values
        assert( suspensionLevel==50 and brakeStrength==100 and speed==0)==True

        #runs the segment of code with a maxmimum suspension value that should flag emergency stop
        suspensionLevel, brakeStrength, speed=emergencystoptest(101,99,1)

        #emergency stop activates so values equal emergency stop values
        assert( suspensionLevel==50 and brakeStrength==100 and speed==0)==True

        #runs the segment of code with a minimum suspension value that should flag emergency stop
        suspensionLevel, brakeStrength, speed=emergencystoptest(-1,99,1)

        #emergency stop activates so values equal emergency stop values
        assert( suspensionLevel==50 and brakeStrength==100 and speed==0)==True
    except:
        print("GUI test case 2 failed")
        
guitestcase1()
guitestcase2()