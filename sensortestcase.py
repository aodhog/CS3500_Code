import sensor, stop
from datetime import datetime


def stalltest(speedOfScan):
    #extract from sensor code
    #delays the scan until the correct timeframe
    wait=True
    time=datetime.now()
    while datetime.now().second!=(time.second+speedOfScan or speedOfScan)and wait==True:
        wait=True

    #variable to get the time the scan occurred
    scantime=datetime.now().second
    return scantime, time.second+speedOfScan

def ifElseWritetoFileTest(next):
    #opens sensor text file for editing 
    sensortxt=open("sensor.txt", "w")

    #if-else statement snippet from code 
    for i in range(2):
        if i==0:
            sensortxt.write(f"{next}: ")
        else:
            sensortxt.write(f"{next}\n")
    sensortxt.close()



def sensortestcase1():
    #test to see if the program ends if speed is equal to 0

    try:
        #initalise road text file with the speed of the car at 0
        roadtxt=open("road.txt", "w")
        roadtxt.write("0\n")
        roadtxt.close()

        #run sensor code file
        sensor.sensor()

        #reads the sensor text file which should be empty since the speed is 0 and nothing was scanned.
        sensortxt=open("sensor.txt", "r")
        sensorlist=sensortxt.readlines()

        assert(len(sensorlist))==0
    except:
        print("Sensor test case 1 failed")

def sensortestcase2():
    #tests to see if the program ends if stop is equal to True
    try:
        #initalise road text file with the speed of the car at 1
        roadtxt=open("road.txt", "w")
        roadtxt.write("1\n")
        roadtxt.close()

        #sets stop to true
        stop.Stop=True

        #runs sensos code file
        sensor.sensor()

        #reads the sensor text file whihc should be empty since stop was true.
        sensortxt=open("sensor.txt", "r")
        sensorlist=sensortxt.readlines()

        assert(len(sensorlist))==0
    except:
        print("Sensor test case 2 failed")

def sensortestcase3():
    #tests to see if the program ends if no road feature is scanned from the road text file
    try:
       #initalise road text file with the speed of the car at 1
        roadtxt=open("road.txt", "w")
        roadtxt.write("1\n")
        roadtxt.close()

        #run sensor code file
        sensor.sensor()

        #reads the sensor text file which should be empty since no road feature is in road.txt.
        sensortxt=open("sensor.txt", "r")
        sensorlist=sensortxt.readlines()

        assert(len(sensorlist))==0
    except:
        print("Sensor test case 3 failed")

def sensortestcase4():
    #tests to see if the program ends if no value follows an L
    try:
        #initalise road text file with the speed of the car at 1
        roadtxt=open("road.txt", "w")
        roadtxt.write("1\n")

        #makes first road variable an L
        roadtxt.write("L,00\n")
        roadtxt.close()

        #run sensor code file
        sensor.sensor()

        #reads the sensor text file which should be empty since no road feature is in road.txt.
        sensortxt=open("sensor.txt", "r")
        sensorlist=sensortxt.readlines()

        assert(len(sensorlist))==0
    except:
        print("Sensor test case 4 failed")

def sensortestcase5():
    #tests that the sensor only scans the road when the time is right
    try:
        #sets the speed of the scan to once a second
        #returns the time of scan, and the time the stall was initiated in seconds
        timeofscan, predictedTimeOfScan =stalltest(1)

        #if the time of scan is equal to the predicted time of scan or the speed of the scan itself,
        #(the second loops back around), then the while loop delay is successful
        assert(timeofscan==(predictedTimeOfScan or 1))==True
    except:
        print("Sensor test case 5 failed")

def sensortestcase6():
    #tests that both parts of the write to file if, else statement write to file correctly
    try:
        #runs the snippet of code from sensor code file inputting ["L", 00] to be added
        ifElseWritetoFileTest(["L", "00"])

        #opens the sensort text file to check the above functions output
        sensortxt=open("sensor.txt", "r")
        sensorlist=sensortxt.readlines()
        sensortxt.close()

        #if the if-else statement worked correctly then the first write should be ['L', '00']:
        #and the second write should be ['L', '00']\n
        assert(sensorlist[0])=="['L', '00']: ['L', '00']\n"
    except:
        print("Sensor test case 6 failed")

sensortestcase1()
sensortestcase2()
sensortestcase3()
sensortestcase4()
sensortestcase5()
sensortestcase6()