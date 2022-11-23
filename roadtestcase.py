import road,stop
from random import randint

def Lettertest(choice,previous,angle):
    #snippet of code from road.py to be tested
    #choice variable is removed as we want to test specific ones
    obstacle=[]
    current=randint(1,90)
    if choice=="L":
        previous=choice
        obstacle.append(choice)
        obstacle.append(0)
    elif (choice=="U" and previous=="D") or (choice=="D" and previous=="U"):
        True 
    elif choice==previous:
        current=angle
        obstacle.append(choice)
        obstacle.append(current)
    else:
        previous=choice
        angle=current
        obstacle.append(choice)
        obstacle.append(current)
    return obstacle 

def Obstaclelengthtest(obstacle):
    #opens the road text file
    roadtxt=open("road.txt", "a")
    
    #snippet of code from road.py to be tested
    if len(obstacle)>0:
            roadtxt.write(f"{obstacle[0]},")
            if obstacle[1]<=9:
                roadtxt.write(f"0{obstacle[1]}\n")
            else:
                roadtxt.write(f"{obstacle[1]}\n")
    roadtxt.close()
    return

def roadtestcase1():
    #tests that function ends when stop.Stop==True

    #resets road text from previous tests
    roadtxt=open("road.txt", "w")
    roadtxt.close()

    try:
        #set stop to True which means nothing should be added to road and program will end
        stop.Stop=True

        #call the road function to develop the road
        road.road()

        #get all lines from the road text
        roadtxt=open("road.txt", "r")
        roadlist=roadtxt.readlines()
        roadtxt.close()
        #if program was ended at line 17 in road.py then nothing should be in road.txt 
        # So length will equal 0
        assert(len(roadlist))==0
    except:
        print("road test case 1 failed")

def roadtestcase2():
    #tests that program produces an L with 00 angle into road.txt and then repeats while loop/ends 
    # (ends if i==10,000 or stop.Stop==True)

    #resets road text from previous tests
    roadtxt=open("road.txt", "w")
    roadtxt.close()

    try:
        #get the obstacle list that will be passed to the next if statement
        obstacle=Lettertest("L", None, None)

        #passes the obstacle list to the obstacle if statment for length
        Obstaclelengthtest(obstacle)
    
        #reads the road file
        roadtxt=open("road.txt", "r")
        roadlist=roadtxt.readlines()
        roadtxt.close()
        #if the test is successful then the first road feature should be an L with 00 angle
        assert(roadlist[0])=='L,00\n'
    except:
        print("road test case 2 failed")

def roadtestcase3():
    #test that if a U and a D are together that it repeats the loop without adding them

    #resets road text from previous tests
    roadtxt=open("road.txt", "w")
    roadtxt.close()

    try:
        #makes the first road feature a U with an angle
        obstacle=Lettertest("U", None, None)

        #writes the U road feature to road.txt
        Obstaclelengthtest(obstacle)
        
        #trys to make second road feature a D with an angle
        #this fails due to second elif statement and produces an empty obstacle list
        obstacle=Lettertest("D", "U", obstacle[1])

        #since obstacle list is empty, nothing is written to the file
        Obstaclelengthtest(obstacle)
        
        #reads text file to check if both U and D were added
        roadtxt=open("road.txt", "r")
        roadlist=roadtxt.readlines()
        roadtxt.close()
        #if roadlist is equal to one it means only U was added and not D
        assert(len(roadlist))==1

        #The same test can be done with D first and then U with identical code
        #this resets road text file
        roadtxt=open("road.txt", "w")
        roadtxt.close()
        
        obstacle=Lettertest("D", None, None)
        Obstaclelengthtest(obstacle)
        obstacle=Lettertest("U", "D", obstacle[1])
        Obstaclelengthtest(obstacle)
        roadtxt=open("road.txt", "r")
        roadlist=roadtxt.readlines()
        roadtxt.close()

        #if roadlist is equal to one it means only D was added and not U
        assert(len(roadlist))==1
    except:
        print("road test case 3 failed")

def roadtestcase4():
    #test that if current adn previous letter are the same then the angle stays the same too.

    try:
        #makes the first road feature a U with an angle
        obstacle=Lettertest("U", None, None)

        #adds the U road feature to a list for comparison
        obstacles=[obstacle]
        
        #trys to make second road feature a new with an angle
        #this changes the second U angle to match the first
        obstacle=Lettertest("U", "U", obstacle[1])

        #adds the U road feature to a list for comparison
        obstacles.append(obstacle)
       
        #if both obstacles are the same then the test was successful
        assert(obstacles[0]==obstacles[1])==True
    except:
        print("road test case 4 failed")

def roadtestcase5():
    #tests the program writes a new angle if a U or D follows an L
    
    #resets road text from previous tests
    roadtxt=open("road.txt", "w")
    roadtxt.close()

    try:
        #makes the first road feature an L with an angle
        obstacle=Lettertest("L", None, None)

        #adds the U road feature to a list for comparison
        obstacles=[obstacle]
        
        #trys to make second road feature a new with the same angle as previous
        #this changes the second U angle to match the first
        obstacle=Lettertest("U", "L", obstacle[1])

        #adds the U road feature to a list for comparison
        obstacles.append(obstacle)
        
        #if both obstacles are the same then the test was successful
        assert(obstacles[0]!=obstacles[1])==True
    except:
        print("road test case 5 failed")


roadtestcase1()
roadtestcase2()
roadtestcase3()
roadtestcase4()
roadtestcase5()